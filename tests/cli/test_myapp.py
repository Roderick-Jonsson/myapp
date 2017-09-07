"""CLI tests for myapp."""

from myapp.utils import test

class CliTestCase(test.myappTestCase):
    def test_myapp_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')
