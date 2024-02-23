import os


class FileText:
    def __init__(self, path: str | None = None) -> None:
        self.path = path

    def read_content(self) -> str:
        if not self.path:
            raise

        with open(self.path, "r") as f:
            content = f.read()

        return content

    def construct_from_directory(self, directory_name, filename):
        self.path = os.path.join(directory_name, filename)
