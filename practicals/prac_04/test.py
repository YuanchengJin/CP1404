
# numbers = input("number and comma..").split()
# scores = []
# for i in range(len(numbers)):
#     numbers[i] = numbers[i].title()
# while numbers != []:
#     text = ', '.join(numbers)
#     scores.append(words)
#     print(scores)
#     numbers = input("name and number..").split()
# print("Thank you")
"""
names = ["Ada","Alan","Bill","John"]
print(",".join(names))
name_to_remove = input("What do you want to remove?")
while name_to_remove  in names:

    try:
        names.remove(name_to_remove)
        print(names)
        name_to_remove = input("What do you want to remove?")
    except ValueError:
    print("error message")
    name_to_remove = input("What do you want to remove?")
print（names）
    """

# things = [True,1.2,"Good",[1,10]]
# print(things[0][0])
# print(things[-2])
# print("%".join([things[2][1:-1]]))
# print([str(t)[0]for t in things])
# print([len(str(t))for t in things])
# print([t for t in things if isinstance(t,int)])
# sum_of_number = 0
# with open ("numbers.txt", 'r') as in_file:
#     for number in in_file:
#         sum_of_number += float(number)
# print(sum_of_number)
#
# with open ("numbers.txt", 'r') as in_file:
#     numbers = in_file.readlines()
#     sum_of_number = sum(int(number) for number in numbers)
#     print(sum_of_number)




# number = 0


# def get_numbers():
#     number = input("get")).split()
    # numbers = []
    # for i in range((len(numbers))):
    #     numbers[i] = float(numbers[i])
    #     numbers.append(number)
    # return numbers

# data = [['Derek',7],['Xavjer',90],['Bob',612],['Chantanelie',9]]

# for name,score in data:
#     print(f"{name:<12} = {score}")
# for i in range (len(data)):
#     name = data[i][0]
#     number = data[i][1]
#     print(f'{name} = {number}')

# name_width = max((len(pair[0]) for pair in data))
# score_width = max((len(str(pair[1])) for pair in data))
#
# for pair in data:
#     name,score =pair
#     print(f"{name:{name_width}} = {score}")

# from operator import itemgetter

# data = [['Derek',7],['Xavierl',80],['Bob',612],['Chantanelle',9]]
#
# name_width = max((len(pair[0]) for pair in data))
# score_width = max((len(str(pair[1])) for pair in data))
# data.sort(key=itemgetter(0),reverse = True)
# for pair in data:
#     name,score = pair
#     print(f"{name:{name_width}} = {score:{score_width}}")
# print()


# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
# def get_numbers():
#     text = input("input: ").split(',')
#     return text
#
# def square_numbers(numbers):
#     for i in range (len(numbers)):
#         numbers[i] = float(numbers[i]) ** 2
# def display_numbers(numbers):
#     print("..".join(str(number) for number in sorted(numbers, reverse=True)))
#
# main()


# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
# def get_numbers():
#     text = input("Please: ").split(",")
#     return text
#
# def square_numbers(numbers):
#     for i in range (len(numbers)):
#         numbers[i] = float(numbers[i]) ** 2
#
# def display_numbers(numbers):
#     print("..".join(str(number)for number in sorted(numbers,reverse=True)))
#
# main()
#
# with open('numbers.txt') as in_file:
    lines = [line.strip() for line in in_file.readlines()]
    # lines = [line.strip() for line in in_file.readlines()]
    # print(lines)
