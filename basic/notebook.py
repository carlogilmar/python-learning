
# Case Study: Notebook

import datetime
last_id = 0

class Note:
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        self._find_note(note_id).tags = tags

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                         "1" : self.show_notes,
                         "2" : self.search_notes,
                         "3" : self.add_note,
                         "4" : self.modify_note,
                         "5" : self._notes,
                       }

    def display_menu(self):
        print (" 1.- Show all notes \n2.- Search notes \n3.- Add note \n4.-Modify note \n5.- Quit")

    def run(self):
        while True:
            self.display_menu()
            choise = input("Enter option: ")
            action = self.choices.get(choise)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    #TODO: Falta terminar el ejercicio




