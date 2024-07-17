# import operator
#
# name_to_number = {'Derek':7, 'Xaviar':80,'Bob':612,'Chantanelle':9}
# sorted_dict = sorted(name_to_number.items(),key=operator.itemgetter(1),reverse=True)
# for name,number in sorted_dict:
#     name_to_number[name] = number
#     max_length = max(len(name) for name in list(name_to_number.keys()))
#     print(f"{name:{max_length}} = {number}")

# word_to_count = {"apple": 8, "Kiwi": 4}
# words = ["apple","orange"]
# for word in words:
#     try:
#         word_to_count[word] += 1
#         words = print(word,word_to_count[word])
#     except KeyError:
#         word_to_count[word] = 1
#         print(word,word_to_count[word])
# print(word_to_count)

# word_to_count = {"apple": 8, "Kiwi": 4}
# words = ["apple","orange"]
# for word in words:
#     word_to_count[word] = word_to_count.get(word,0) +1
#     print(word,word_to_count[word])
# print(word_to_count)

"""languages = ["python","java","json"]

languages to length = {"python":6,"java":4,"json":4}"""

"""languages = ["python","java","json"]
values = [6,4,4]
language_to_count = zip(languages,values)
print(f"languages to length = {dict(language_to_count)}")"""
# def list_of_languages(language):
#     length_of_dict = {}
#     languages =["python","java","json"]
#     for language in languages:
#         length_of_dict[language] = len(languages)
#     return length_of_dict
# words = ["aye", "bee", "sea", "bee"]
# words.remove("bee")
# print(words.pop())
# things = list("one two three")
# print("{}-{}".format(*things))

# print("*".join([len(word) for word in "one*two*three".split('*')]))
# languages = ["python","java","json"]
# values = [6,4,4]
# language_to_count = zip(languages,values)
# print(f"languages to length = {dict(language_to_count)}")

# def add(x, y):
#     return x + y
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = map(add, list1, list2)
# print(list(result))
# values = [1, 2, 3, 2]
# values.remove(2)
# print(values)
# before = [1, 4, 0, -1]
# after = before.sort()
# print(after)
#
# def main():
#     filename = "wimbledon.csv"
#     data = read_file(filename)
#     champion_counts = count_champions(data)
#     countries = get_countries(data)
#     print("Wimbledon Champions:")
#     for champion, count in champion_counts.items():
#         print(f"{champion} {count}")
#     print("\nThese {} countries have won Wimbledon:".format(len(countries)))
#     print(", ".join(countries))
#
#
# def read_file(filename):
#     """
#     Read the CSV file and return the data as a list of lists.
#     """
#     try:
#         with open(filename, "r", encoding="utf-8-sig") as in_file:
#             data = [line.strip().split(",") for line in in_file]
#         return data
#     except FileNotFoundError:
#         print(f"Error: The file {filename} was not found.")
#         return []
#     except IOError:
#         print(f"Error: An error occurred while reading the file {filename}.")
#         return []
#
#
# def count_champions(data):
#     """
#     Count the number of wins by each champion.
#     """
#     champion_counts = {}
#     for row in data[1:]:  # Skip the header row
#         champion = row[2]
#         try:
#             champion_counts[champion] += 1
#         except KeyError:
#             champion_counts[champion] = 1
#     return champion_counts
#
#
# def get_countries(data):
#     """
#     Get the countries of the champions in alphabetical order.
#     """
#     countries = set()
#     for row in data[1:]:  # Skip the header row
#         country = row[1]
#         countries.add(country)
#     return sorted(countries)
#
#
# main()
#
email = "john.doe@example.com"
name_part = email.split('@')
print(name_part)