"""
Custom Exceptions for File Handling & Data Storage Operations.
Author: Prince Abang
"""


class StorageException(Exception):
    """Base exception class for storage and data handling errors."""
    pass


class RecordNotFoundError(StorageException):
    """Raised when a specific record is not found in the storage files."""
    pass


class DataCorruptionError(StorageException):
    """Raised when file content is unreadable or malformed."""
    pass


class DuplicateRecordError(StorageException):
    """Raised when attempting to save a record with an existing unique ID."""
    pass