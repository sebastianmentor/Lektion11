class Person:
    def __init__(self,name:str,personNumber:str):
        self.Name = name
        self.PersonNumber = personNumber
        
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Person):
            return self.Name == __value.Name and self.PersonNumber == __value.PersonNumber
        return False 


class PersonRegister:        
    def __init__(self):
        self.persons = dict()

    def getPerson(self,personNummer):
        if not personNummer in self.persons:
            return "Finns inte"
        else:
            return self.persons[personNummer]

    def add(self,person):
        if person.PersonNumber in self.persons:
            return "Duplicate key"
        self.persons[person.PersonNumber] = person