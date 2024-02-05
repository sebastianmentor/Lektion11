from main import Person, PersonRegister
import unittest

class PersonTest(unittest.TestCase):
    def test_1_When_creating_person_name_and_personnumber_should_be_set(self):
        name = "Sebastian"
        sn = "19890704-6002"

        sut = Person(name, sn)

        # self.assertEqual(name, sut.Name)
        # self.assertEqual(sn, sut.PersonNumber)

    def test_2_that_a_person_are_who_he_says_to_be(self):

        name = "Sebastian"
        sn = "19890704-6002"
        sut = Person(name, sn)
        name2 = "Sebastian"
        sn2 = "19890704-6002"
        sut2 = Person(name2, sn2)
        
        self.assertEqual(sut, sut2)



class PersonRegisterTest(unittest.TestCase):
    def test_When_fetching_person_correct_person_should_be_returned(self):    
        #arrange    
        person1 = Person("Stefan", "19720803-0000")
        person2 = Person("Kalle", "19790101-0000")
        sut = PersonRegister()
        sut.add(person1)
        sut.add(person2)
        #act
        result = sut.getPerson("19720803-0000")
        #assert
        self.assertIs(person1, result)

    def test_When_fetching_person_and_person_does_not_exist_correct_errormessage_should_be_returned(self):    
        #arrange    
        person1 = Person("Stefan", "19720803-0000")
        person2 = Person("Kalle", "19790101-0000")
        sut = PersonRegister()
        sut.add(person1)
        sut.add(person2)
        #act
        result = sut.getPerson("19720803-1111")
        #assert
        self.assertEqual("Finns inte", result)

    def test_When_adding_person_and_person_already_exist_correct_errormessage_should_be_returned(self):    
        #arrange    
        person1 = Person("Stefan", "19720803-0000")
        person2 = Person("Kalle", "19720803-0000")
        sut = PersonRegister()
        sut.add(person1)

        #act
        result = sut.add(person2)

        #assert
        self.assertEqual("Duplicate key", result)

if __name__ == "__main__":
    unittest.main()