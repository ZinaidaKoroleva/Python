def sort_id():
    with open('Phonebook.txt', 'r+') as file:
        data = file.readlines()
        data_list = []
        for line in data:
            elem = line.split(" ")
            data_list.append(elem)
        data_list = sorted(data_list, key = lambda x: x[0])
        file.seek(0)
        for i in data_list:
            file.write(" ".join(i))
    return data

def sort_name():
    with open('Phonebook.txt', 'r+') as file:
        data = file.readlines()
        data_list = []
        for line in data:
            elem = line.split(" ")
            data_list.append(elem)
        data_list = sorted(data_list, key = lambda x: x[1])
        file.seek(0)
        for i in data_list:
            file.write(" ".join(i))
    return data