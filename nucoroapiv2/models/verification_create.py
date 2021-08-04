# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from nucoroapiv2.api_helper import APIHelper


class VerificationCreate(object):

    """Implementation of the 'VerificationCreate' model.

    TODO: type model description here.

    Attributes:
        uuid (uuid|string): TODO: type description here.
        verify_type (VerifyTypeEnum): TODO: type description here.
        status (StatusBd7Enum): TODO: type description here.
        result (ResultEnum): TODO: type description here.
        created (datetime): TODO: type description here.
        updated (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uuid": 'uuid',
        "verify_type": 'verify_type',
        "created": 'created',
        "updated": 'updated',
        "status": 'status',
        "result": 'result'
    }

    def __init__(self,
                 uuid=None,
                 verify_type=None,
                 created=None,
                 updated=None,
                 status=None,
                 result=None):
        """Constructor for the VerificationCreate class"""

        # Initialize members of the class
        self.uuid = uuid
        self.verify_type = verify_type
        self.status = status
        self.result = result
        self.created = APIHelper.RFC3339DateTime(created) if created else None
        self.updated = APIHelper.RFC3339DateTime(updated) if updated else None

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
        verify_type = dictionary.get('verify_type')
        created = APIHelper.RFC3339DateTime.from_value(dictionary.get("created")).datetime if dictionary.get("created") else None
        updated = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated")).datetime if dictionary.get("updated") else None
        status = dictionary.get('status')
        result = dictionary.get('result')

        # Return an object of this model
        return cls(uuid,
                   verify_type,
                   created,
                   updated,
                   status,
                   result)
