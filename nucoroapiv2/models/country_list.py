# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CountryList(object):

    """Implementation of the 'CountryList' model.

    TODO: type model description here.

    Attributes:
        code (string): TODO: type description here.
        iso_3 (string): TODO: type description here.
        name (string): TODO: type description here.
        long_name (string): TODO: type description here.
        eea_country (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "iso_3": 'iso3',
        "name": 'name',
        "long_name": 'long_name',
        "eea_country": 'eea_country'
    }

    def __init__(self,
                 code=None,
                 iso_3=None,
                 name=None,
                 long_name=None,
                 eea_country=None):
        """Constructor for the CountryList class"""

        # Initialize members of the class
        self.code = code
        self.iso_3 = iso_3
        self.name = name
        self.long_name = long_name
        self.eea_country = eea_country

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
        iso_3 = dictionary.get('iso3')
        name = dictionary.get('name')
        long_name = dictionary.get('long_name')
        eea_country = dictionary.get('eea_country')

        # Return an object of this model
        return cls(code,
                   iso_3,
                   name,
                   long_name,
                   eea_country)
