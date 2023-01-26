import view
import export
import sort
def modul():
    start_menu = view.menu()
    if start_menu == 1:
        date = view.get_date()
        export.file_create(date)
        view.success()
    elif start_menu == 2:
        export.print_phonebook()
    elif start_menu == 3:
        choice = view.menu_sort()
        if choice == 1:
            sort.sort_id()
        elif choice == 2:
            sort.sort_name()
        else:
            view.input_error()
    else:
        view.input_error()
