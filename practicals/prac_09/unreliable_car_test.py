from unreliable_car import UnreliableCar

def main():
    # Create a new UnreliableCar object
    unreliable_car = UnreliableCar("Old Car", 100, 50)

    # Try driving the unreliable car 40 kilometers
    distance_driven = unreliable_car.drive(40)
    print(f"Distance driven: {distance_driven} km")

    # Print details of the unreliable car
    print(unreliable_car)

    # Try driving a few more times
    for _ in range(5):
        distance_driven = unreliable_car.drive(40)
        print(f"Distance driven: {distance_driven} km")
        print(unreliable_car)

if __name__ == "__main__":
    main()

