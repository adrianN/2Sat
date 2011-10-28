# -*- coding: utf-8 -*-
from networkx import DiGraph
from networkx.algorithms.components.strongly_connected import strongly_connected_components
from networkx.algorithms.shortest_paths import *

def _graph(formula):
  """Build the implication graph"""
  G = DiGraph()
  for (a,b) in formula.iterclause():
	G.add_edge(-a,b)
	G.add_edge(-b,a)
  
  return G

def satisfiable(formula):
  try:
	contradictory_variables(formula).next()
	return False
  except:
	return True
  

  
def contradictory_variables(formula, G = None):
  if not G:
	G = _graph(formula)
  
  #check if a and -a in the same component
  for component in strongly_connected_components(G):
	seen = set()
	for literal in component:
	  v = abs(literal)
	  if v in seen:
		yield v
	  else:
		seen.add(v)
  
def evil_path_lengths(formula):
  G = _graph(formula)
  dist = all_pairs_shortest_path_length(G)
  for v in contradictory_variables(formula,G):
	yield (v, dist[-v][v], dist[v][-v])