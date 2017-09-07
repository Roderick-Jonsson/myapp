"""myapp project base controller."""

from cement.ext.ext_argparse import ArgparseController, expose

class myappBaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = 'none'
        extensions = ['mustache', 'json']
        output_handler = 'mustache'
        arguments = [
            (['-f', '--foo'],
             dict(help='the notorious foo option', dest='foo', action='store',
                  metavar='TEXT') ),
            ]

    @expose(hide=True)
    def default(self):
        print("Inside myappBaseController.default().")

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        data = dict(foo='bar')
        self.app.render(data, 'letest.m')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``myapp.cli.templates``, or ``/var/lib/myapp/templates/``.
        #
