class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time, total_seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats

    def __str__(self):
        return (
            f"{self.flight_number}: {self.origin} to {self.destination}, "
            f"departs {self.departure_time}, arrives {self.arrival_time}, "
            f"{self.total_seats} seats"
        )


class FlightManager:
    def __init__(self):
        self.flights = []

    def search_flights(self, origin, destination):
        matching_flights = []

        for flight in self.flights:
            if (
                flight.origin.lower() == origin.lower()
                and flight.destination.lower() == destination.lower()
            ):
                matching_flights.append(flight)

        return matching_flights

    def show_flights(self):
        return self.flights

    def get_flight_by_number(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight

        return None

    def add_flight(self, flight):
        if flight.total_seats <= 0:
            raise ValueError("Total seats must be greater than zero.")

        for existing_flight in self.flights:
            if existing_flight.flight_number == flight.flight_number:
                raise ValueError("That flight number is already in use.")

        self.flights.append(flight)