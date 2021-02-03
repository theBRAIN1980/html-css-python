class Student:
    def __init__(self, cursuri):
        self.cursuri = list(cursuri)
        self.note = dict()
    
    def add_new_course(self, curs):
        self.cursuri.append(curs_nou)


    def __add__(self, curs_nou):
        self.cursuri.append(curs_nou)
        return Student(self.cursuri)

    def __str__(self):
        str_cursuri = ""
        for curs in self.cursuri:
            str_cursuri = str_cursuri + curs
        return "Lista Cursuri" + str_cursuri

class Curs:
    def __init__(self, nume_curs, departament):
        self.nume_curs = nume_curs
        self.departament = departament

    def __eq__(self, alt_curs):
        return self.nume_curs == alt_curs.nume_curs

curs1 = Curs("Pyhton OOP", "Python")
curs2 = Curs("Python Fundamentals", "Python")
curs3 = Curs("Pyhton OOP", "Java")

student = Student([])
student = student + curs1


# if curs1 == curs3:
#     print("Asta-i Frate!")

# else:
#     print("Nu-i asta frate!")

