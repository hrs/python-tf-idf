The simplest TF-IDF library imaginable.

Add your documents as two-element lists [docname, [list_of_words_in_the_document] ] with addDocument (docname, list_of_words).
Ex:
	table.addDocument ("foo", ["a", "b", "c", "d", "e", "f", "g", "h"])


Get a list of all the [docname, similarity_score] pairs relative to a document by calling similarities ( [list_of_words] ).  Resulting similarities will always 
Ex:
	table.similarities (["a", "b", "c"])


********** Example Code: **********

	import tfidf
	
	(...)
	
	table = tfidf.tfidf ()
	table.addDocument ("foo", ["a", "b", "c", "d", "e", "f", "g", "h"])
	table.addDocument ("bar", ["a", "b", "c", "i", "j", "k"])
	table.addDocument ("baz", ["k", "l", "m", "n"])

	print table.similarities (["a", "b", "c"])

********** Output: **********

	>  [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]