"""myapp project exception classes."""

class myappError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class myappConfigError(myappError):
    """Config related errors."""
    pass

class myappRuntimeError(myappError):
    """Generic runtime errors."""
    pass

class myappArgumentError(myappError):
    """Argument related errors."""
    pass
