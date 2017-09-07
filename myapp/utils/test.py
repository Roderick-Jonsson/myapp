"""Testing utilities for myapp project."""

from myapp.cli.main import myappTestApp
from cement.utils.test import *

class myappTestCase(CementTestCase):
    app_class = myappTestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(myappTestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(myappTestCase, self).tearDown()

