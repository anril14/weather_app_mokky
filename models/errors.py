class HTTPError(Exception):
    def __init__(self, error_msg: str, status_code: int):
        super().__init__(error_msg)
        self.error_msg = error_msg
        self.status_code = status_code

    def encode(self, encoding: str = 'utf-8', errors: str = 'strict') -> bytes:
        return self.error_msg.encode(encoding, errors)

