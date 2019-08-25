#!/usr/bin/env python

import sys, unittest, os

# Get configuration
from .config import env_config


class BaseTestCase(unittest.TestCase):

    """
        Base Test Case which is inherited through all tests in order to
        provide proper webdriver workflow to set up and
        tear down test case groups.
    """

    # some configuration defaults if the environment is started from Pycharm/Terminal
    BASE_LINK = "http://localhost:3030"

    try:
        BASE_LINK = env_config.get('url')
    except SystemExit:
        pass

    try:
        browser_env = os.environ["BROWSER_ENV"]
    except KeyError:
        # browser_env is empty if not running in terminal, therefore Chrome is added as default
        browser_env = "chrome"

    def get_base_link(self):
        try:
            return env_config.get('url')
        except SystemExit:
            return self.BASE_LINK

    def setUp(self):
        pass

    def tearDown(self):
        pass
