import view
import export
import sort
def modul():
    while True:
        start_menu = view.menu()
        if start_menu == 1:
            date = view.get_date()
            export.file_create(date)
            view.success()
        elif start_menu == 2:
            export.print_phonebook()
        elif start_menu == 3:
            choice = view.menu_sort()
            if choice == 2:
                sort.sort_id()
                view.success()
            elif choice == 1:
                sort.sort_name()
                view.success()
            else:
                view.input_error()
        elif start_menu == 4:
            export.print_names()
        elif start_menu == 5:
            break
        else:
            view.input_error()
