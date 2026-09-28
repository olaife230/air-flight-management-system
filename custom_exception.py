from data_storage.data_manager import DataManager
from data_storage.custom_exceptions import DuplicateRecordError, RecordNotFoundError, DataCorruptionError

if __name__ == "__main__":
    manager = DataManager()

    # --- 1. Testing Flight Record Addition ---
    sample_flight = {
        "flight_id": "FL101",
        "route": "Lagos -> Abuja",
        "seats_available": 45,
        "date": "2026-10-15"
    }

    try:
        print("Adding Flight Record...")
        manager.add_record(manager.flights_file, sample_flight, id_field="flight_id")
        print("Flight saved successfully!")
    except DuplicateRecordError as e:
        print(f"Validation Warning: {e}")
    except DataCorruptionError as e:
        print(f"Storage Error: {e}")

    # --- 2. Testing Search Operation ---
    print("\nSearching Flight Record...")
    flight = manager.find_record(manager.flights_file, "flight_id", "FL101")
    print("Found Flight:", flight)

    # --- 3. Testing Record Update ---
    try:
        print("\nUpdating Seat Availability...")
        manager.update_record(
            manager.flights_file, 
            id_field="flight_id", 
            target_id="FL101", 
            updated_fields={"seats_available": 44}
        )
        print("Updated successfully!")
    except RecordNotFoundError as e:
        print(f"Error: {e}")