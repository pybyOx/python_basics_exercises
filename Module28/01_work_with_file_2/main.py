import types
from typing import IO, Any, Optional, Type


class File:
    """ Контекст-менеджер, обеспечивающий открытие файла в указанном режиме и автоматическое закрытие.
    Если файл не найден, он создается и открывается для записи.
    """
    def __init__(self, my_path: str, mode: str) -> None:
        """Инициализирует экземпляр класса File
        Args:
            my_path (str): Путь к файлу.
            mode (str): Режим открытия файла (например, 'r' для чтения, 'w' для записи).
        """
        self._path = my_path
        self._mode = mode
        self._file = None

    @property
    def path(self) -> str:
        """Геттер, возвращающий путь к файлу"""
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        """Сеттер, устанавливающий путь к файлу"""
        self._path = value

    @property
    def mode(self) -> str:
        """Геттер, возвращающий режим открытия файла"""
        return self._mode

    @mode.setter
    def mode(self, value) -> None:
        """Сеттер, устанавливающий режим открытия файла"""
        self._mode = value

    @property
    def file(self) -> IO[Any]:
        """Геттер, возвращающий файловый объект"""
        return self._file

    @file.setter
    def file(self, value) -> None:
        """Сеттер, устанавливающий файловый объект"""
        self._file = value

    def __enter__(self) -> IO[Any]:
        """
        Выполняет необходимые операции при входе в контекстный менеджер.
        Открывает файл в указанном режиме.
        Если файл не найден, он создается и открывается для записи.
        :return: Возвращает открытый файловый объект.
        """
        try:
            self.file = open(self.path, self.mode, encoding='utf8')
            return self.file
        except FileNotFoundError:
            print('Файл создан (не существовал) и открыт в режиме записи.')
            self.file = open(self.path, 'w', encoding='utf8')
            return self.file

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[types.TracebackType]) -> Optional[bool]:
        """
        Выполняет закрытие файла при выходе из контекстного менеджера
        Args:
            exc_type: Тип исключения, если оно возникло
            exc_val: Значение исключения, если оно возникло
            exc_tb: Объект трассировки стека, если исключение возникло
        Returns:
            bool: `True`, если исключение относится к файловой системе и было обработано
        """
        self.file.close()
        if exc_type in [FileExistsError, FileNotFoundError, IsADirectoryError, PermissionError]:
            return True


with File("example.txt", "w") as file:
    file.write("Всем привет!")
