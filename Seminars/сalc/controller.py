import view
import summ
import div
import div_fl
import mult
import sub
import div_int

def calc ():
    type_of_num = int(view.get_value(1))
    value_a = view.get_value(type_of_num)
    value_znak = view.get_sign()
    value_b = view.get_value(type_of_num)
    if value_znak == '+':
        view.view_result(summ.sum(value_a, value_b))
    if value_znak == '-':
        view.view_result(sub.sub(value_a, value_b))
    if value_znak == '*':
        view.view_result(mult.mult(value_a, value_b))
    if value_znak == '/':
        view.view_result(div.div(value_a, value_b))
    if type_of_num == 1:
        if value_znak == '//':
            view.view_result(div_int.div(value_a, value_b))
        if value_znak == '%':
            view.view_result(div_fl.div(value_a, value_b))
    if type_of_num != 1 and (value_znak=='//' or value_znak=='%'):
        print('Ошибка операции')
