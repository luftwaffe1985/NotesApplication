import Note


def create_note(number):
    title = check_len_text_input(
        input('Enter a name of the note: '), number)
    body = check_len_text_input(
        input('Enter a description: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nThis is an application for making notes called 'NotesApplication'. " 
          "It has the following fuctions:\n\n1 - print all notes from the file"
          "\n2 - add a note\n3 - remove a note\n4 - edit a note"
          "\n5 - sort all notes by date\n6 - show the required note by id"
          "\n7 - exit\n\nChoose the function : ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Text length must be more than {n} symbols\n')
        text = input('Enter a text: ')
    else:
        return text


def goodbye():
    print("Good bye!")
