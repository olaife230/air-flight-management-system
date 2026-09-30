import streamlit as st
from flight_manager import Flight, FlightManager

st.title("Air Flight Management and Reservation System")
st.write("Search for a flight")

flight_manager = FlightManager()

flight_manager.add_flight(
    Flight("FL001", "Lagos", "Abuja", "09:00", "10:15", 40)
)
flight_manager.add_flight(
    Flight("FL002", "Lagos", "Port Harcourt", "11:30", "12:45", 35)
)
flight_manager.add_flight(
    Flight("FL003", "Abuja", "Lagos", "14:00", "15:15", 40)
)

cities = ["Lagos", "Abuja", "Port Harcourt"]

origin = st.selectbox("From", cities)
destination = st.selectbox("To", cities)

if st.button("Search flights"):
    matching_flights = flight_manager.search_flights(origin, destination)

    if matching_flights:
        st.subheader("Available flights")

        for flight in matching_flights:
            st.write(f"Flight: {flight.flight_number}")
            st.write(f"Departure: {flight.departure_time}")
            st.write(f"Arrival: {flight.arrival_time}")
            st.write(f"Total seats: {flight.total_seats}")
            st.write("---")
    else:
        st.warning("No flights found for that route.")