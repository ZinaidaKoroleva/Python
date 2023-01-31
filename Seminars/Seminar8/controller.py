import view

main_book = {}
names_list = []
schoolworks_list = []
def start():
    while True:
        number = view.menu()
        if number == 1:                      #1: Добавить нового студента
            name = view.get_student()
            if name not in names_list:
                names_list.append(name)
                main_book[name] = {}
                for less in schoolworks_list:
                    main_book[name][less] = []
            else:
                view.repit_error()
        elif number == 2:                     #2: Добавить предмет
            schoolwork = view.get_schoolwork()
            if schoolwork not in schoolworks_list:
                schoolworks_list.append(schoolwork)
                for name in names_list:
                    main_book[name][schoolwork] = []
            else:
                view.repit_error()
        elif number == 3:                   #3: Добавить оценку ученику по предмету
            name = view.get_student()
            if name not in names_list:
                view.input_error()
            schoolwork = view.get_schoolwork()
            if schoolwork not in schoolworks_list:
                view.input_error()
            mark = view.get_mark()
            main_book[name][schoolwork].append(mark)
        elif number == 4:                # 4: Показать список учеников
            print(main_book)
        elif number == 5:                # 5: Показать лист оценок конкретного ученика
            name = view.get_student()
            print((main_book[name]))
        elif number == 6:              #6:Выход
            break