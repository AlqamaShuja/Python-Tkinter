class Person:
    # class attribute
    # species = "Ashraf-ul-Maakhloqaat"
    count = 0
    def __init__(self, age, country, id, name=None):
        self.name = name
        self.age = age
        self.country = country
        self.__id = id
        Person.count += 1

    def showDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCountry: {self.country}\nId: {self.__id}")


p1 = Person(name="Hussain", age=12, country="Pakistan", id=234)
p2 = Person(name="Hussain", age=12, country="Pakistan", id=234)
p3 = Person(name="Hussain", age=12, country="Pakistan", id=234)
# print(p3.__class__.count)
# p1.showDetails()
print(p1.__id)

# class Student(Person):
#     def __init__(self, name, age, country, id, class_, schoolName):
#         Person.__init__(self, name, age, country, id)
#         self.class_ = class_
#         self.schoolName = schoolName
#
#     def showDetails(self):
#         # super(Student, self).showDetails()
#         super().showDetails()
#         print(f"Class: {self.class_}\nSchool Name: {self.schoolName}")
#
#
#
#
# std1 = Student("Ali", 12, "Pakistan", 234, "XII", "Hayat ul Islam")
# # std1.showSchoolDetails()
# std1.showDetails()