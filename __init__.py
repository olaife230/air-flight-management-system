"""
Data Storage Package Initialization.
"""
from .data_manager import DataManager
from .custom_exceptions import (
    StorageException,
    RecordNotFoundError,
    DataCorruptionError,
    DuplicateRecordError
)

__all__ = [
    "DataManager",
    "StorageException",
    "RecordNotFoundError",
    "DataCorruptionError",
    "DuplicateRecordError",
]