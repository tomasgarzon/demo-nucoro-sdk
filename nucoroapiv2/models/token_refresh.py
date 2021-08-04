# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TokenRefresh(object):

    """Implementation of the 'TokenRefresh' model.

    TODO: type model description here.

    Attributes:
        refresh (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "refresh": 'refresh'
    }

    def __init__(self,
                 refresh=None):
        """Constructor for the TokenRefresh class"""

        # Initialize members of the class
        self.refresh = refresh

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
        refresh = dictionary.get('refresh')

        # Return an object of this model
        return cls(refresh)
