#!/usr/bin/env python
# encoding: utf-8

"""
File: tfidf.py
Author: Harry Schwartz
Date: Dec 2010

The simplest TF-IDF library imaginable.

Add your documents as two-element lists [docname, [list_of_words_in_the_document] ] with addDocument (docname, list_of_words).  Get a list of all the [docname, similarity_score] pairs relative to a document by calling similarities ( [list_of_words] ).

See README.txt for a usage example.
"""

import sys
import os

class tfidf:
	def __init__(self):
		self.weighted = False
		self.documents = []
		self.corpusDict = {}
	
	def addDocument (self, docName, listOfWords):
		# building a dictionary
		docDict = {}
		for w in listOfWords:
			if docDict.has_key (w):
				docDict [w] = docDict [w] + 1.0
			else:
				docDict [w] = 1.0
			if self.corpusDict.has_key (w):
				self.corpusDict [w] = self.corpusDict [w] + 1.0
			else:
				self.corpusDict [w] = 1.0
				
		# normalizing the dictionary
		length = float (len (listOfWords))
		for k in docDict:
			docDict [k] = docDict [k] / length
		
		# add the normalized document to the corpus
		self.documents.append ( [docName, docDict] )
		
	def similarities (self, listOfWords):
		"""Returns a list of all the [docname, similarity_score] pairs relative to a list of words."""
		
		# building the query dictionary
		queryDict = {}
		for w in listOfWords:
			if queryDict.has_key (w):
				queryDict [w] = queryDict [w] + 1.0
			else:
				queryDict [w] = 1.0
				
		# normalizing the query
		length = float (len (listOfWords))
		for k in queryDict:
			queryDict [k] = queryDict [k] / length
		
		# computing the list of similarities
		sims = []
		for doc in self.documents:
			score = 0.0
			docDict = doc [1]
			for k in queryDict:
				if docDict.has_key (k):
					score += (queryDict [k] / self.corpusDict [k]) + (docDict [k] / self.corpusDict [k])
			sims.append ([doc [0], score])
			
		return sims
