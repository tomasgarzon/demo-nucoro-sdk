# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from nucoroapiv2.models.document import Document


class PaginatedDocumentList(object):

    """Implementation of the 'PaginatedDocumentList' model.

    TODO: type model description here.

    Attributes:
        count (int): TODO: type description here.
        next (string): TODO: type description here.
        previous (string): TODO: type description here.
        results (list of Document): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "next": 'next',
        "previous": 'previous',
        "results": 'results'
    }

    def __init__(self,
                 count=None,
                 next=None,
                 previous=None,
                 results=None):
        """Constructor for the PaginatedDocumentList class"""

        # Initialize members of the class
        self.count = count
        self.next = next
        self.previous = previous
        self.results = results

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        count = dictionary.get('count')
        next = dictionary.get('next')
        previous = dictionary.get('previous')
        results = None
        if dictionary.get('results') is not None:
            results = [Document.from_dictionary(x) for x in dictionary.get('results')]

        # Return an object of this model
        return cls(count,
                   next,
                   previous,
                   results)
