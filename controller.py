import function
import ui


def run():
    input_from_user = ''
    while input_from_user != '7':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            function.show('all')
        if input_from_user == '2':
            function.add()
        if input_from_user == '3':
            function.show('all')
            function.id_edit_del_show('del')
        if input_from_user == '4':
            function.show('all')
            function.id_edit_del_show('edit')
        if input_from_user == '5':
            function.show('date')
        if input_from_user == '6':
            function.show('id')
            function.id_edit_del_show('show')
        if input_from_user == '7':
            ui.goodbye()
            break
