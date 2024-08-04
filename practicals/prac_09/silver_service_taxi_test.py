
from silver_service_taxi import SilverServiceTaxi

def main():
    """Test the fare calculation for SilverServiceTaxi."""
    mysilvertaxi = SilverServiceTaxi("Luxury Taxi", 200, 2)
    mysilvertaxi.drive(18)
    expected_fare = 48.78
    actual_fare = mysilvertaxi.get_fare()
    assert actual_fare == expected_fare, f"Expected fare: {expected_fare}, but got: {actual_fare}"

# Run the tests
if __name__ == "__main__":
    main()
    print("All tests passed!")
