from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display available taxis."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi from the list of available taxis."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(taxi):
    """Drive the selected taxi and calculate the fare."""
    try:
        distance = float(input("Drive how far? "))
        fare = taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
        return 0


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0.0
    running = True

    while running:
        print("Bill to date: $0.00")
        print("q)uit, c)hoose taxi, d)rive")
        option = input(">>> ").lower()

        if option == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            running = False
        elif option == 'c':
            current_taxi = choose_taxi(taxis)
            if current_taxi is not None:
                print(f"Current taxi: {current_taxi}")
        elif option == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                fare = drive_taxi(current_taxi)
                total_bill += fare
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
