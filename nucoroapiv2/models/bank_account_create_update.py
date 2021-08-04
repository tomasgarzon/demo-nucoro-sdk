# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class BankAccountCreateUpdate(object):

    """Implementation of the 'BankAccountCreateUpdate' model.

    TODO: type model description here.

    Attributes:
        uuid (uuid|string): TODO: type description here.
        account_number (string): TODO: type description here.
        account_sort_code (string): TODO: type description here.
        account_holder_name (string): TODO: type description here.
        joint (bool): TODO: type description here.
        bank_name (string): TODO: type description here.
        iban (string): TODO: type description here.
        swift_code (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uuid": 'uuid',
        "account_number": 'account_number',
        "account_sort_code": 'account_sort_code',
        "account_holder_name": 'account_holder_name',
        "joint": 'joint',
        "bank_name": 'bank_name',
        "iban": 'iban',
        "swift_code": 'swift_code'
    }

    def __init__(self,
                 uuid=None,
                 account_number=None,
                 account_sort_code=None,
                 account_holder_name=None,
                 joint=None,
                 bank_name=None,
                 iban=None,
                 swift_code=None):
        """Constructor for the BankAccountCreateUpdate class"""

        # Initialize members of the class
        self.uuid = uuid
        self.account_number = account_number
        self.account_sort_code = account_sort_code
        self.account_holder_name = account_holder_name
        self.joint = joint
        self.bank_name = bank_name
        self.iban = iban
        self.swift_code = swift_code

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
        uuid = dictionary.get('uuid')
        account_number = dictionary.get('account_number')
        account_sort_code = dictionary.get('account_sort_code')
        account_holder_name = dictionary.get('account_holder_name')
        joint = dictionary.get('joint')
        bank_name = dictionary.get('bank_name')
        iban = dictionary.get('iban')
        swift_code = dictionary.get('swift_code')

        # Return an object of this model
        return cls(uuid,
                   account_number,
                   account_sort_code,
                   account_holder_name,
                   joint,
                   bank_name,
                   iban,
                   swift_code)
