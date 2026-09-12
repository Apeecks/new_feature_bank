import logging
from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор логирования начала, конца, результатов и ошибок"""

    def function(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger = logging.getLogger()

            if filename is not None:
                logging.basicConfig(
                    level=logging.INFO,
                    filename=filename,
                    filemode="a",
                    encoding="utf-8",
                    format="%(levelname)s - %(message)s",
                )
            else:
                logging.basicConfig(level=logging.INFO, format="%(levelname)s -%(message)s")

            try:
                logger.info(f"Start {func.__name__}")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.info(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return function
