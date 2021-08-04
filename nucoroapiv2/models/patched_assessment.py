# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from nucoroapiv2.api_helper import APIHelper
from nucoroapiv2.models.risk_choice_question_code import RiskChoiceQuestionCode


class PatchedAssessment(object):

    """Implementation of the 'PatchedAssessment' model.

    TODO: type model description here.

    Attributes:
        uuid (uuid|string): TODO: type description here.
        completed (datetime): TODO: type description here.
        choices (list of RiskChoiceQuestionCode): TODO: type description
            here.
        status (AssessmentStatusEnum): TODO: type description here.
        risk_level (int): TODO: type description here.
        created (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uuid": 'uuid',
        "completed": 'completed',
        "choices": 'choices',
        "status": 'status',
        "risk_level": 'risk_level',
        "created": 'created'
    }

    def __init__(self,
                 uuid=None,
                 completed=None,
                 choices=None,
                 status=None,
                 risk_level=None,
                 created=None):
        """Constructor for the PatchedAssessment class"""

        # Initialize members of the class
        self.uuid = uuid
        self.completed = APIHelper.RFC3339DateTime(completed) if completed else None
        self.choices = choices
        self.status = status
        self.risk_level = risk_level
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
        uuid = dictionary.get('uuid')
        completed = APIHelper.RFC3339DateTime.from_value(dictionary.get("completed")).datetime if dictionary.get("completed") else None
        choices = None
        if dictionary.get('choices') is not None:
            choices = [RiskChoiceQuestionCode.from_dictionary(x) for x in dictionary.get('choices')]
        status = dictionary.get('status')
        risk_level = dictionary.get('risk_level')
        created = APIHelper.RFC3339DateTime.from_value(dictionary.get("created")).datetime if dictionary.get("created") else None

        # Return an object of this model
        return cls(uuid,
                   completed,
                   choices,
                   status,
                   risk_level,
                   created)
