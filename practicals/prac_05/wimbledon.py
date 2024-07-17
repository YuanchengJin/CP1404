def main():
    # Read the Wimbledon champions data, return sorted result.
    filename = "wimbledon.csv"
    data = read_file(filename)
    champion_counts = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, count in champion_counts.items():
        print(f"{champion} {count}")

    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(countries))


def read_file(filename):
    # Read the CSV file and return the data as a list of lists.
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            data = [line.strip().split(",") for line in in_file]
        return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except IOError:
        print(f"Error: An error occurred while reading the file {filename}.")
        return []


def count_champions(data):
    # Count the number of wins by each champion.
    champion_counts = {}
    for row in data[1:]:
        champion = row[2]
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts


def get_countries(data):
    # Get the countries of the champions in alphabetical order.
    countries = set()
    for row in data[1:]:  # Skip the header row
        country = row[1]
        countries.add(country)
    return sorted(countries)

main()
