# -*- coding: utf-8 -*-
import networkx as nx

def satisfiable(formula):
  #Build the implication graph
  G = nx.DiGraph()
  for (a,b) in formula.iterclauses():
	G.add_edge(-a,b)
	G.add_edge(-b,a)
  
  