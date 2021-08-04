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
from nucoroapiv2.controllers.auth_controller import AuthController


class AuthControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(AuthControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = AuthController(cls.config, cls.response_catcher)

    # Request a password reset
    def test_user_request_password_reset(self):
        # Parameters for the API call
        email = None

        # Perform the API call through the SDK function
        result = self.controller.user_request_password_reset(email)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


