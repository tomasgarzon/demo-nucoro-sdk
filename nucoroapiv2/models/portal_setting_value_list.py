# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from nucoroapiv2.api_helper import APIHelper


class PortalSettingValueList(object):

    """Implementation of the 'PortalSettingValueList' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        uuid (uuid|string): TODO: type description here.
        created (datetime): TODO: type description here.
        updated (datetime): TODO: type description here.
        value (string): TODO: type description here.
        portal (int): TODO: type description here.
        key (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "uuid": 'uuid',
        "created": 'created',
        "updated": 'updated',
        "value": 'value',
        "portal": 'portal',
        "key": 'key'
    }

    def __init__(self,
                 id=None,
                 uuid=None,
                 created=None,
                 updated=None,
                 value=None,
                 portal=None,
                 key=None):
        """Constructor for the PortalSettingValueList class"""

        # Initialize members of the class
        self.id = id
        self.uuid = uuid
        self.created = APIHelper.RFC3339DateTime(created) if created else None
        self.updated = APIHelper.RFC3339DateTime(updated) if updated else None
        self.value = value
        self.portal = portal
        self.key = key

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
        id = dictionary.get('id')
        uuid = dictionary.get('uuid')
        created = APIHelper.RFC3339DateTime.from_value(dictionary.get("created")).datetime if dictionary.get("created") else None
        updated = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated")).datetime if dictionary.get("updated") else None
        value = dictionary.get('value')
        portal = dictionary.get('portal')
        key = dictionary.get('key')

        # Return an object of this model
        return cls(id,
                   uuid,
                   created,
                   updated,
                   value,
                   portal,
                   key)
