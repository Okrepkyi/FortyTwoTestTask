from apps.hello.models import PersonModel
from django.test import TestCase


class FirstViewTest(TestCase):

	def test_ticket1_view(self):
		PersonModel.objects.create(name='Oleksandr',
									surname='Okrepkyi',
									date='1987-10-22',
									bio='Geologist / Future Python developer',
									jabber='Moveton',
									email='okrepkyj@gmail.com',
									skype='kre.kre.',
									other='Linkedin - oleksandr Okrepkyi')
		user = PersonModel.objects.all()
		self.assertEqual(user.count(), 1)
