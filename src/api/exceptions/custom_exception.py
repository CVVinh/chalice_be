class ApplicationException(Exception):
    def __init__(self, code=None, message=None, params=None, field=None):
        super().__init__(code, message, params, field)
        self.code = code
        self.params = params
        self.field = field
        self.message = message


class UnauthorizedException(Exception):
    def __init__(self, params=None, field=None):
        super().__init__()
        self.params = params
        self.field = field


