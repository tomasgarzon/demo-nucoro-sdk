# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from nucoroapiv2.api_helper import APIHelper


class PatchedPortfolioUpdate(object):

    """Implementation of the 'PatchedPortfolioUpdate' model.

    A ModelSerializer that takes additional arguments for
    "fields", "omit" and "expand" in order to
    control which fields are displayed, and whether to replace simple
    values with complex, nested serializations

    Attributes:
        uuid (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        portfolio_type (string): TODO: type description here.
        risk_level (int): TODO: type description here.
        time_horizon (int): TODO: type description here.
        status (Status2efEnum): TODO: type description here.
        currency (string): TODO: type description here.
        created (datetime): TODO: type description here.
        activated (datetime): TODO: type description here.
        advisor (string): TODO: type description here.
        advice_engine (string): TODO: type description here.
        extra_data (dict): TODO: type description here.
        client (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uuid": 'uuid',
        "name": 'name',
        "portfolio_type": 'portfolio_type',
        "risk_level": 'risk_level',
        "time_horizon": 'time_horizon',
        "status": 'status',
        "currency": 'currency',
        "created": 'created',
        "activated": 'activated',
        "advisor": 'advisor',
        "advice_engine": 'advice_engine',
        "extra_data": 'extra_data',
        "client": 'client'
    }

    def __init__(self,
                 uuid=None,
                 name=None,
                 portfolio_type=None,
                 risk_level=None,
                 time_horizon=None,
                 status=None,
                 currency=None,
                 created=None,
                 activated=None,
                 advisor=None,
                 advice_engine=None,
                 extra_data=None,
                 client=None):
        """Constructor for the PatchedPortfolioUpdate class"""

        # Initialize members of the class
        self.uuid = uuid
        self.name = name
        self.portfolio_type = portfolio_type
        self.risk_level = risk_level
        self.time_horizon = time_horizon
        self.status = status
        self.currency = currency
        self.created = APIHelper.RFC3339DateTime(created) if created else None
        self.activated = APIHelper.RFC3339DateTime(activated) if activated else None
        self.advisor = advisor
        self.advice_engine = advice_engine
        self.extra_data = extra_data
        self.client = client

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
        name = dictionary.get('name')
        portfolio_type = dictionary.get('portfolio_type')
        risk_level = dictionary.get('risk_level')
        time_horizon = dictionary.get('time_horizon')
        status = dictionary.get('status')
        currency = dictionary.get('currency')
        created = APIHelper.RFC3339DateTime.from_value(dictionary.get("created")).datetime if dictionary.get("created") else None
        activated = APIHelper.RFC3339DateTime.from_value(dictionary.get("activated")).datetime if dictionary.get("activated") else None
        advisor = dictionary.get('advisor')
        advice_engine = dictionary.get('advice_engine')
        extra_data = dictionary.get('extra_data')
        client = dictionary.get('client')

        # Return an object of this model
        return cls(uuid,
                   name,
                   portfolio_type,
                   risk_level,
                   time_horizon,
                   status,
                   currency,
                   created,
                   activated,
                   advisor,
                   advice_engine,
                   extra_data,
                   client)
