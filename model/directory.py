import os


class Directory:
    def __init__(self, path: str | None = None):
        self.name = path

    def get_files(self) -> list[str]:
        if not self.name:
            self.name = os.getcwd()

        extensions = (".txt", ".py", ".csv")

        filenames = []
        for filename in os.listdir(self.name):
            _, ext = os.path.splitext(filename)
            if ext in extensions:
                filenames.append(filename)
        return filenames
