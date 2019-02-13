import types

class Person:
    def __init__(self, name):
        self._name = name

person_a = Person("person_a")
person_b = Person("person_b")


def get_name(self):
    return self._name

Person.get_name = get_name


person_a_name = person_a.get_name()
person_b_name = person_b.get_name()

print(person_a_name)
print(person_b_name)

del Person.get_name


person_a.get_name = types.MethodType(get_name, person_a)
print(person_a.get_name())
# print(person_b.get_name())

# https://www.ianlewis.org/jp/python-add-class-method
