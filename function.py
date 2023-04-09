import file_operation
import Note
import ui

number = 5  # minimum symbols number


def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Note added...')


def show(text):
    global date
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Enter date as dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic:
        print('No notes exist...')


def id_edit_del_show(text):
    id = input('Enter id of the required note: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Note changed...')
            if text == 'del':
                array.remove(notes)
                print('Note removed...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic:
        print('No such note, try to enter the right id')
    file_operation.write_file(array, 'a')
