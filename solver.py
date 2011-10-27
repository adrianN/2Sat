# -*- coding: utf-8 -*-
from networkx import DiGraph
from networkx.algorithms.components.strongly_connected import strongly_connected_components

def _graph(formula):
  """Build the implication graph"""
  G = DiGraph()
  for (a,b) in formula.iterclause():
	G.add_edge(-a,b)
	G.add_edge(-b,a)
  
  return G

def satisfiable(formula):
  G = _graph(formula)
  
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