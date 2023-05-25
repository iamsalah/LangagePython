class Person:
    def __init__(self, origin):
        self.origin = origin
    
    def display_origin(self):
        print("Origine:", self.origin)

choice = input("Entrez la première lettre de l'origine ethnique (A pour africain, S pour asiatique, E pour européen) : ")

origin = ""
if choice.lower() == 'a':
    origin = "Africain"
elif choice.lower() == 's':
    origin = "Asiatique"
elif choice.lower() == 'e':
    origin = "Européen"
else:
    origin = "Non reconnu"

person = Person(origin)
person.display_origin()
