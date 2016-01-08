from django.test import TestCase
from apps.hello.models import PersonModel


class PersonModelTest(TestCase):

    def create_person_model(self, name="Ababagalamag", 
    						surname="Agamalagabab", 
    						date="1987-10-22", 
    						bio="", 
    						jabber="",
    						email="",
    						skype="",
    						other=""):
    
        return PersonModel.objects.create(name=name, 
        									surname=surname, 
        									date=date, bio=bio, 
        									jabber=jabber, 
        									email=email, 
        									skype=skype, 
        									other=other)

    def test_person_model(self):
        instance = self.create_person_model()
        self.assertEqual(instance.__str__(), instance.name)
