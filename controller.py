import function as funk
import description


def run():
    input_user = ''
    while input_user != '7':
        description.menu()
        input_user = input().strip()
        if input_user == '1':
            funk.show('all')
        if input_user == '2':
            funk.add()
        if input_user == '3':
            funk.show('all')
            funk.id_edit_del_show('del')
        if input_user == '4':
            funk.show('all')
            funk.id_edit_del_show('edit')
        if input_user == '5':
            funk.show('date')
        if input_user == '6':
            funk.show('id')
            funk.id_edit_del_show('show')
        if input_user == '7':
            description.goodbuy()
            break