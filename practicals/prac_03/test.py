"""filename = input("Enter your file name:")
in_file = open(filename,'r')
for line in in_file:
    if line.startswith('#'):
        print(line, end=' ')
in_file.close()

FILENAME = 'TEXT.TXT'
in_file = open(FILENAME)
text = in_file.readline()
text = in_file.readline()
"""

"""s = "\t Python,Monty \n"
print(s[1],".", sep="")
print(s.strip(), ".", sep="")
s = s.replace(' ', '*')
print(s)
print(s.lstrip(), ".", sep="")
print(s.strip().split(','))
print(s.strip().split(' '))"""
"""
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


with open(name) as out_file:
    print(name,file = out_file)"""

# print(10/0)

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("zero cannot")

# in_file = open("anc.txt", "r")


# try:
#     in_file = open()
#     t


"""is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Invalid")
    finally:
        print("Nice try!")
print("Valid result is:", result)"""

"""value = int(input("> "))
result = f"{value}" * value
thing = result[value]"""

def load_number(filename):
    try:
        infile = open(filename, "r")
        number = int(infile.read())
    except ValueError:
        print(f"Invalid contents in {filename}")
    except FileNotFoundError:
        print(f"{filename} not found")
        number = 6
    else:
        infile.close()
    return number

