import os
import pytest
from logger import ConsoleLogger, FileLogger, LoggerFactory, Logger

def test_console_logger_creation():
    """
    Тест 1: Проверка создания консольного логгера через фабричный метод.
    """
    logger = LoggerFactory.create_logger("console")
    
    assert isinstance(logger, FileLogger)
    assert isinstance(logger, Logger)


def test_file_logger_creation_with_custom_path():
    """
    Тест 2: Проверка создания файлового логгера с пользовательским путём.
    """
    test_log_file = "test_custom.log"
    
    if os.path.exists(test_log_file):
        os.remove(test_log_file)
    
    logger = LoggerFactory.create_logger("file", file_path=test_log_file)
    
    assert isinstance(logger, FileLogger)
    
    test_message = "Тестовое сообщение для файла"
    logger.log(test_message, "INFO")
    
    assert os.path.exists(test_log_file)
    with open(test_log_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert test_message in content
    
    os.remove(test_log_file)


@pytest.mark.parametrize("logger_type,expected_class", [
    ("console", ConsoleLogger),
    ("file", FileLogger),
])
def test_factory_method_parametrized(logger_type, expected_class):
    """
    Тест 3 (дополнительный): Параметризованный тест, проверяющий создание обоих типов логгеров.
    """
    logger = LoggerFactory.create_logger(logger_type)
    assert isinstance(logger, expected_class)