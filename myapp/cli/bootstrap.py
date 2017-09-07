"""myapp project bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as myappBaseController.

from myapp.cli.controllers.base import myappBaseController

def load(app):
    app.handler.register(myappBaseController)
