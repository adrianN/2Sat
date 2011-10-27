﻿# -*- coding: utf-8 -*-

from random import choice, randint

class Formula(object):
  """A 2-Sat Formula. Variables are integers, 0 is not allowed. Negative numbers are negated literals"""
  def __init__(self):
	self.f = []
	
  def add_clause(self,(a,b)):
	self.f.append((a,b))
  
  def iterclause(self):
	return iter(self.f)
	
  def num_clauses(self):
	return len(self.f)
	
  def __str__(self):
	return str(self.f)
	
def uniform(c1,c2):
  return choice((c1,c2))

def random_clause(n):
  sign = (-1,1)
  cl = (choice(sign)*randint(1,n),choice(sign)*randint(1,n))
  return cl
  
def random_formula(n, m, repeat = True, choice=uniform):
  if not repeat:
	assert(m<3*n)
  f = Formula()
  seen = set()
  for i in xrange(m):
	(a,b) = choice(random_clause(n), random_clause(n))
	if a>b: (a,b) = (b,a)
	while not repeat and (a,b) not in seen:
	  (a,b) = choice(random_clause(n), random_clause(n))
	  if a>b: (a,b) = (b,a)
	seen.add((a,b))
	f.add_clause((a,b))
  return f

