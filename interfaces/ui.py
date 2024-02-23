from abc import ABC, abstractmethod


class UIPort(ABC):

    @abstractmethod
    def setup_ui(self):
        pass

    @abstractmethod
    def display_list_files(self, files: list[str]) -> None:
        pass

    @abstractmethod
    def display_content_file(self, content: str) -> None:
        pass

    @abstractmethod
    def ask_path_directory(self) -> str:
        pass
