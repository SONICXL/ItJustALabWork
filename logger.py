import os
from abc import ABC, abstractmethod
from datetime import datetime

# --- Абстрактный продукт ---
class Logger(ABC):
    @abstractmethod
    def log(self, message: str, level: str = "INFO") -> None:
        pass

    def _format_message(self, message: str, level: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] [{level}] {message}"


# --- Конкретные продукты ---
class ConsoleLogger(Logger):
    def log(self, message: str, level: str = "INFO") -> None:
        formatted_message = self._format_message(message, level)
        print(formatted_message)


class FileLogger(Logger):
    def __init__(self, file_path: str = "app.log"):
        self.file_path = file_path

    def log(self, message: str, level: str = "INFO") -> None:
        formatted_message = self._format_message(message, level)
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(formatted_message + "\n")


# --- Фабричный метод ---
class LoggerFactory:
    @staticmethod
    def create_logger(logger_type: str, **kwargs) -> Logger:
        if logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "file":
            file_path = kwargs.get("file_path", "app.log")
            return FileLogger(file_path)
        else:
            raise ValueError(f"Неизвестный тип логгера: {logger_type}")