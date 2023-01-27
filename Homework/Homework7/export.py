import view
def file_create(date):
    with open('Phonebook.txt', 'a') as file:
        file.writelines(date + '\n')

def print_phonebook():
    with open('Phonebook.txt', 'r') as file:
        print(file.read())

def print_names():
    with open('Phonebook.txt', 'r') as file:
        for line in file.readlines():
            elem = line.split(" ")
            print(elem[1],elem[2])

