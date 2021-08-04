# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from nucoroapiv2.api_helper import APIHelper
from nucoroapiv2.models.risk_choice import RiskChoice


class Question(object):

    """Implementation of the 'Question' model.

    TODO: type model description here.

    Attributes:
        code (string): TODO: type description here.
        order (int): TODO: type description here.
        description (string): TODO: type description here.
        choices (list of RiskChoice): TODO: type description here.
        created (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "order": 'order',
        "description": 'description',
        "choices": 'choices',
        "created": 'created'
    }

    def __init__(self,
                 code=None,
                 order=None,
                 description=None,
                 choices=None,
                 created=None):
        """Constructor for the Question class"""

        # Initialize members of the class
        self.code = code
        self.order = order
        self.description = description
        self.choices = choices
        self.created = APIHelper.RFC3339DateTime(created) if created else None

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
        code = dictionary.get('code')
        order = dictionary.get('order')
        description = dictionary.get('description')
        choices = None
        if dictionary.get('choices') is not None:
            choices = [RiskChoice.from_dictionary(x) for x in dictionary.get('choices')]
        created = APIHelper.RFC3339DateTime.from_value(dictionary.get("created")).datetime if dictionary.get("created") else None

        # Return an object of this model
        return cls(code,
                   order,
                   description,
                   choices,
                   created)
