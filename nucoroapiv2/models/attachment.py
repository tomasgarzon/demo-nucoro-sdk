# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Attachment(object):

    """Implementation of the 'Attachment' model.

    TODO: type model description here.

    Attributes:
        attachment_extension (string): TODO: type description here.
        attachment_filename (string): TODO: type description here.
        uuid (uuid|string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attachment_extension": 'attachment_extension',
        "attachment_filename": 'attachment_filename',
        "uuid": 'uuid'
    }

    def __init__(self,
                 attachment_extension=None,
                 attachment_filename=None,
                 uuid=None):
        """Constructor for the Attachment class"""

        # Initialize members of the class
        self.attachment_extension = attachment_extension
        self.attachment_filename = attachment_filename
        self.uuid = uuid

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
        attachment_extension = dictionary.get('attachment_extension')
        attachment_filename = dictionary.get('attachment_filename')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(attachment_extension,
                   attachment_filename,
                   uuid)
