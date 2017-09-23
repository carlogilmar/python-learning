print ("Dia 2 de python")

# Herencia: Agregando comportamiento a una clase
class MySubclass(object):
    pass

class Contact:
    all_contacts=[]
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send '{}' order to '{}'".format(order, self.name))

# Polimorfismo: Agregando diferentes comportamientos

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file Format")
        self.filename = filename

class Mp3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))

class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename
    def play(self):
        print("playing {} as flac".format(self.filename))

#
