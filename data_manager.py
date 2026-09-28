"""
Data Storage and File Handling Manager.
Author: Prince Abang
Primary Responsibility: File Handling & Data Storage
Collaborating On: Exception Handling & Validation
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from .custom_exceptions import RecordNotFoundError, DataCorruptionError, DuplicateRecordError


class DataManager:
    """
    Handles read, write, update, and search operations across JSON files.
    Ensures persistent storage and robust error handling for system data.
    """

    def __init__(self, data_directory: str = "data"):
        self.data_dir = Path(data_directory)
        self.flights_file = self.data_dir / "flights.json"
        self.passengers_file = self.data_dir / "passengers.json"
        self.bookings_file = self.data_dir / "bookings.json"
        
        # Ensure base data folder and files exist
        self._initialize_storage()

    def _initialize_storage(self) -> None:
        """Creates the data directory and default JSON files if they don't exist."""
        try:
            os.makedirs(self.data_dir, exist_ok=True)
            for file_path in [self.flights_file, self.passengers_file, self.bookings_file]:
                if not file_path.exists():
                    with open(file_path, "w", encoding="utf-8") as file:
                        json.dump([], file, indent=4)
        except OSError as e:
            print(f"[Error] Failed to initialize file storage directory: {e}")
            raise

    def load_data(self, file_path: Path) -> List[Dict[str, Any]]:
        """Reads and loads JSON data from a given file safely."""
        if not file_path.exists():
            raise FileNotFoundError(f"Storage file '{file_path.name}' is missing.")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise DataCorruptionError(f"Corrupted or invalid JSON format in '{file_path.name}': {e}")
        except PermissionError:
            raise PermissionError(f"Access denied when reading '{file_path.name}'. Check file permissions.")
        except Exception as e:
            raise DataCorruptionError(f"Unexpected error loading '{file_path.name}': {e}")

    def save_data(self, file_path: Path, data: List[Dict[str, Any]]) -> bool:
        """Saves a Python list/dict structure into a JSON file."""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            return True
        except PermissionError:
            print(f"[Error] Permission denied while saving to '{file_path.name}'.")
            return False
        except Exception as e:
            print(f"[Error] Failed to save data to '{file_path.name}': {e}")
            return False

    def add_record(self, file_path: Path, record: Dict[str, Any], id_field: str) -> bool:
        """Appends a new record to the target file after validating ID uniqueness."""
        records = self.load_data(file_path)

        # Check for existing duplicate record
        for existing in records:
            if existing.get(id_field) == record.get(id_field):
                raise DuplicateRecordError(
                    f"Record with {id_field} '{record.get(id_field)}' already exists."
                )

        records.append(record)
        return self.save_data(file_path, records)

    def find_record(self, file_path: Path, id_field: str, value: Any) -> Optional[Dict[str, Any]]:
        """Finds and returns a single record by key and matching value."""
        records = self.load_data(file_path)
        for record in records:
            if record.get(id_field) == value:
                return record
        return None

    def update_record(self, file_path: Path, id_field: str, target_id: Any, updated_fields: Dict[str, Any]) -> bool:
        """Updates specific fields of an existing record in the file."""
        records = self.load_data(file_path)
        found = False

        for record in records:
            if record.get(id_field) == target_id:
                record.update(updated_fields)
                found = True
                break

        if not found:
            raise RecordNotFoundError(f"Record with {id_field} '{target_id}' not found.")

        return self.save_data(file_path, records)

    def delete_record(self, file_path: Path, id_field: str, target_id: Any) -> bool:
        """Removes a record from the file by matching ID."""
        records = self.load_data(file_path)
        initial_length = len(records)
        records = [rec for rec in records if rec.get(id_field) != target_id]

        if len(records) == initial_length:
            raise RecordNotFoundError(f"Record with {id_field} '{target_id}' not found to delete.")

        return self.save_data(file_path, records)