# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PasswordReset(object):

    """Implementation of the 'PasswordReset' model.

    TODO: type model description here.

    Attributes:
        email (string): TODO: type description here.
        token (string): TODO: type description here.
        password (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email": 'email',
        "token": 'token',
        "password": 'password'
    }

    def __init__(self,
                 email=None,
                 token=None,
                 password=None):
        """Constructor for the PasswordReset class"""

        # Initialize members of the class
        self.email = email
        self.token = token
        self.password = password

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
        email = dictionary.get('email')
        token = dictionary.get('token')
        password = dictionary.get('password')

        # Return an object of this model
        return cls(email,
                   token,
                   password)
