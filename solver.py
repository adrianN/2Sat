# -*- coding: utf-8 -*-
import networkx as nx
from networkx.algorithms.components.strongly_connected import strongly_connected_components

def satisfiable(formula):
  #Build the implication graph
  G = nx.DiGraph()
  for (a,b) in formula.iterclauses():
	G.add_edge(-a,b)
	G.add_edge(-b,a)
  
  #check if a and -a in the same component
  for component in strongly_connected_components(G):
	seen = set()
	for literal in component:
	  v = abs(literal)
	  if v in seen:
		return False
	  else:
		seen.add(v)
  
  #components clean
  return True
  
  