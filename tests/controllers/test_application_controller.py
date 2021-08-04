# -*- coding: utf-8 -*-

"""
nucoroapiv2

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from nucoroapiv2.api_helper import APIHelper
from nucoroapiv2.controllers.application_controller import ApplicationController


class ApplicationControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ApplicationControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = ApplicationController(cls.config, cls.response_catcher)

    # List client for a Relationship manager
    def test_client_list(self):
        # Parameters for the API call
        external_custodian_id = None
        extra_data = None
        limit = None
        offset = None
        ordering = None
        search = None
        status = None

        # Perform the API call through the SDK function
        result = self.controller.client_list(external_custodian_id, extra_data, limit, offset, ordering, search, status)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


