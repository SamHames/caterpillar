What is Caterpillar?
====================

Caterpillar is a pure python text indexing and analytics library. Some features include:

* pluggable key/value object store for storage (currently only implementation is SQLite)
* transaction layer for reading/writing (along with associated locking semantics)
* supports searching indexes with some built in scoring algorithm implementations (including TF/IDF)
* stores additional data structures for analytics above and beyond traditional information retrieval data structures
* has a plugin architecture for quickly accessing the data structures and performing custom analytics
* has 100% test coverage


Quick Example
=============
Quick example of using caterpillar below:

    import os
    import tempfile
    
    from caterpillar.processing.index import IndexWriter, IndexConfig
    from caterpillar.processing.schema import TEXT, Schema, NUMERIC
    from caterpillar.storage.sqlite import SqliteStorage
    
    index_dir = os.path.join(tempfile.mkdtemp(), "examples")
    with open('caterpillar/test_resources/moby.txt', 'r') as f:
        data = f.read()
        with IndexWriter(index_dir, IndexConfig(SqliteStorage, Schema(text=TEXT, some_number=NUMERIC))) as writer:
            writer.add_document(text=data, some_number=1)
    
Installation
============

    pip install caterpillar
    
Roadmap
=======
We are working on porting our issues from our internal issue tracker over to a more visible system. But, for the time
being, here is a general roadmap:

* Move to (possibly only) Python 3 (see below).
* Revamp schema and field design.
* Add a memory storage implementation.
* Revamp query design.
* Remove the NLTK dependency (great library, but only used for tokenisation).
* Switch index structures over to a more efficient data structure (possibly numpy arrays or similar).
    
The current plan is to move to using GitHub issues with HuBoard, but stay tuned.
    
Python Version
==============
Currently Python 2.7+ only. Work is underway to support Python 3+. **WARNING**: Caterpillar *might* become Python 3+ 
**only** in the future. Stay tuned.

BDFLs
=====
* [Kris Rogers](https://github.com/krisrogers/)
* [Ryan Stuart](https://github.com/rstuart85/)

Contributors
============
Anyone who is willing! In other words none yet, but we are more then accepting of contributions.

Contributing
============
Not code will be merged unless it has 100% test coverage and passes pep8. We code with a line length of 120 characters 
and we use [py.test](http://pytest.org/) for testing. Tests are in a *test* sub-folder in each package.
