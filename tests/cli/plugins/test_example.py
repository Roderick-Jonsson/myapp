"""Tests for Example Plugin."""

from myapp.utils import test

class ExamplePluginTestCase(test.myappTestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')
