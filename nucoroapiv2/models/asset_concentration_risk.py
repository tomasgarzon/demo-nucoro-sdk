# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AssetConcentrationRisk(object):

    """Implementation of the 'AssetConcentrationRisk' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        asset_class (string): TODO: type description here.
        uuid (string): TODO: type description here.
        value (float): TODO: type description here.
        weight (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "asset_class": 'asset_class',
        "uuid": 'uuid',
        "value": 'value',
        "weight": 'weight'
    }

    def __init__(self,
                 name=None,
                 asset_class=None,
                 uuid=None,
                 value=None,
                 weight=None):
        """Constructor for the AssetConcentrationRisk class"""

        # Initialize members of the class
        self.name = name
        self.asset_class = asset_class
        self.uuid = uuid
        self.value = value
        self.weight = weight

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
        name = dictionary.get('name')
        asset_class = dictionary.get('asset_class')
        uuid = dictionary.get('uuid')
        value = dictionary.get('value')
        weight = dictionary.get('weight')

        # Return an object of this model
        return cls(name,
                   asset_class,
                   uuid,
                   value,
                   weight)
