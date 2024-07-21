import csv
from guitar import Guitar

def main():
    """Manage guitar inventory."""
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)
    add_guitars(guitars)
    save_guitars("guitars.csv", guitars)

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename,'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name,year,cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


def add_guitars(guitars):
    """Add new guitars to the list."""
    print("\nAdd new guitars")
    adding_guitars = True
    guitars_added = 0

    while adding_guitars:
        name = input("Please enter the name (or press Enter to finish): ").strip()
        if name:
            year_valid = False
            while not year_valid:
                year_input = input("Year: ").strip()
                if year_input:
                    try:
                        year = int(year_input)
                        if year > 0:
                            year_valid = True
                        else:
                            print("Year must be a positive integer. Please try again.")
                    except ValueError:
                        print("Invalid year. Please enter a valid positive integer.")
                else:
                    print("Year cannot be empty. Please enter a valid year.")

            cost_valid = False
            while not cost_valid:
                cost_input = input("Cost: $").strip()
                if cost_input:
                    try:
                        cost = float(cost_input)
                        if cost > 0:
                            cost_valid = True
                        else:
                            print("Cost must be a positive number. Please try again.")
                    except ValueError:
                        print("Invalid cost. Please enter a valid positive number.")
                else:
                    print("Cost cannot be empty. Please enter a valid cost.")

            guitars.append(Guitar(name, year, cost))
            guitars_added += 1
            print(f"Added: {name} ({year}) : ${cost:.2f}")
        else:
            adding_guitars = False

    print(f"\nAdded {guitars_added} guitar(s) to the list.")
def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename,'w',newline = '') as outfile:
        writer = csv.writer(outfile)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == "__main__":
    main()