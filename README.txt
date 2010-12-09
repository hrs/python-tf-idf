The simplest TF-IDF library imaginable.

Add your documents as two-element lists [docname, [list_of_words_in_the_document] ] with addDocument (docname, list_of_words).
Ex:
	table.addDocument ("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])


Get a list of all the [docname, similarity_score] pairs relative to a list of words by calling similarities ( [list_of_words] ).  Resulting similarities will always be between 0.0 and 1.0, inclusive.
Ex:
	table.similarities (["alpha", "bravo", "charlie"])

********** Example Code: **********

	import tfidf
	
	(...)
	
	table = tfidf.tfidf ()
	table.addDocument ("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])
	table.addDocument ("bar", ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
	table.addDocument ("baz", ["kilo", "lima", "mike", "november"])

	print table.similarities (["alpha", "bravo", "charlie"])

********** Output: **********

	>  [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]