# Copyright (C) Kapiche
# Author: Kris Rogers <kris@kapiche.com>
"""
This module implements the query framework for caterpillar.

The design intends that the ``BaseQuery`` class is extended to provide specific query functionality that can be used by
``caterpillar.searching.IndexSearcher``.

"""
import abc


class QueryResult(object):
    """
    Encapsulates result data for a single query.

    Fields:
    frame_ids -- A list of IDs for frames that match the query.
    term_weights -- A dict of *matched* query terms to their weightings.

    """
    def __init__(self, frame_ids, term_weights):
        self.frame_ids = frame_ids
        self.term_weights = term_weights


class QueryError(Exception):
    """Invalid query"""


class BaseQuery(object):
    """
    Each ``BaseQuery`` concrete class should represent an individual facet of the query API.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def evaluate(self, index):
        """
        Evaluate this query against the specified index.

        Raises ``QueryError`` on exception.

        """
        return  # pragma: no cover
