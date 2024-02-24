class ArchiFileException(Exception):
    pass


class FileNotFoundException(ArchiFileException):
    def __init__(self, path):
        self.message = f"File not found in {path}"
        if path is None:
            self.message = "path is not define"
        super().__init__(self.message)
