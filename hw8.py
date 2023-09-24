def write_all(name):
    with open(name, 'r', encoding='utf8') as txt_data:
        for line in txt_data:
            print(line.strip())

def write_data(name):
    str_n1 = input('Surname: ')
    str_n2 = input('Name: ')
    str_n3 = input('Second Name: ')
    str_tel = input('Phone number: ')
    new_str = '\n' + str_n1 + ', ' + str_n2 + ', ' + str_n3 + ', ' + str_tel
    with open(name, 'a', encoding='utf8') as txt_data:
        txt_data.write((new_str))
def find_data(name):
    any_data = 0
    item = input('part of surname/name/second name/phone: / Be careful: if you enter too small piece you will find too many inputs: ')
    with open(name, 'r', encoding='utf8') as txt_data:        
        for line in txt_data:
            if item.lower() in line.lower():
                print(line.strip())
                any_data = 1
        if any_data == 0:
            print('There is no such data')
def find_data_item(name):
    any_data = 0
    item = input('What are you looking for (input number:\n1: surname\n2: name\n3: second name\n4: phone number: \n')
    item_data = input('Input search: ')
    with open(name, 'r', encoding='utf8') as txt_data:
        for line in txt_data:
            line_list = line.split(', ')
            if int(item) == 1:
                if item_data.lower() == line_list[0].lower():
                    print(line.strip())
                    any_data = 1
            elif int(item) == 2:
                if item_data.lower() == line_list[1].lower():
                    print(line.strip())
                    any_data = 1
            elif int(item) == 3:
                if item_data.lower() == line_list[2].lower():
                    print(line.strip())
                    any_data = 1
            elif int(item) == 4:
                if item_data.lower() == line_list[3].lower():
                    print(line.strip())
                    any_data = 1
            else:
                print("No such item")
        if any_data == 0:
            print('There is no such data')

def ed_data(name):
    with open(name, 'r', encoding='utf8') as txt_data:
        lines_data = [line.strip() for line in txt_data]
        for i in range(len(lines_data)):
            print(str(i+1) + ': ' + lines_data[i])
    item = input('Input what line you want to edit: ')
    item_fit = input('What are you looking for (input number:\n1: surname\n2: name\n3: second name\n4: phone number: \n')
    item_data = input('Input new data: ')
    with open(name, 'w', encoding='utf8') as txt_data:
        for i in range(len(lines_data)):
            if int(item) - 1 != i:
                txt_data.write((lines_data[i] + '\n'))
            else:
                str_edit = lines_data[i].split(', ')
                new_str = ''
                for j in range(len(str_edit)):
                    if (int(item_fit) - 1 != j) & (j != len(str_edit) - 1):
                        new_str = new_str + str_edit[j] + ', '
                    elif (int(item_fit) - 1 != j) & (j == len(str_edit) - 1):
                        new_str = new_str + str_edit[j] + '\n'
                    elif (int(item_fit) - 1 == j) & (j != len(str_edit) - 1):
                        new_str = new_str + item_data + ', '
                    elif (int(item_fit) - 1 == j) & (j == len(str_edit) - 1):
                        new_str = new_str + item_data + '\n'
                txt_data.write((new_str))
    with open(name, 'r', encoding='utf8') as txt_data:
        lines_data_new = [line.strip() for line in txt_data]
        for i in range(len(lines_data_new)):
            print(str(i+1) + ': ' + lines_data_new[i])

def delete_data(name):
    with open(name, 'r', encoding='utf8') as txt_data:
        lines_data = [line.strip() for line in txt_data]
        for i in range(len(lines_data)):
            print(str(i+1) + ': ' + lines_data[i])
    item = input('Input what line you want to delete: ')
    with open(name, 'w', encoding='utf8') as txt_data:
        for i in range(len(lines_data)):
            if int(item) - 1 != i:
                txt_data.write((lines_data[i] + '\n'))
    with open(name, 'r', encoding='utf8') as txt_data:
        lines_data_new = [line.strip() for line in txt_data]
        for i in range(len(lines_data_new)):
            print(str(i+1) + ': ' + lines_data_new[i])


select_feature = input('What do you want to do:\n1: show the data\n2: add new person\n3: find data by entering some charts\n4: find data if you know name|surname etc.\n5: change the data\n6: delete one person from data\n')
if int(select_feature) == 1:
    write_all('data.txt')
elif int(select_feature) == 2:
    write_data('data.txt')
elif int(select_feature) == 3:
    find_data('data.txt')
elif int(select_feature) == 4:
    find_data_item('data.txt')
elif int(select_feature) == 5:
    ed_data('data.txt')
elif int(select_feature) == 6:
    delete_data('data.txt')
else:
    print("No such item")