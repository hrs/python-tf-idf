The simplest TF-IDF library imaginable.

### Usage

Add your documents as two-element lists `[doc_name,
[list_of_words_in_the_document]]` with `add_document(doc_name, list_of_words)`.

```python
table.add_document("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])
```

Get a list of all the `[doc_name, similarity_score]` pairs relative to a list of
words by calling `similarities([list_of_words])`. Resulting similarities will
always be between `0.0` and `1.0`, inclusive.

```python
table.similarities(["alpha", "bravo", "charlie"])
```

So, for example:

```python
from tfidf import TfIdf

table = TfIdf()
table.add_document("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])
table.add_document("bar", ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
table.add_document("baz", ["kilo", "lima", "mike", "november"])

print table.similarities(["alpha", "bravo", "charlie"]) # => [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]
```

### Run the tests

The tests use the standard library's `unittest` module, so there's no need to
install anything. Just run:

```shell
$ python test_tfidf.py
```

### Disclaimer

This library is a pretty clean example of how TF-IDF operates. However, it's
totally unconcerned with efficiency (it's just an exercise to brush up my Python
skills), so you probably don't want to be using it in production. If you're
looking for a more heavy-duty Python library to do information retrieval and
topic modeling, I'd suggest taking a look at [Gensim][].

[Gensim]: http://radimrehurek.com/gensim/
