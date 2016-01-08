from django.core.urlresolvers import resolve
from django.test import TestCase
from apps.hello.views import person_view


class PersonPageTest(TestCase):

	def test_url_resolves_to_person_page(self):
		page = resolve("/")
		self.assertEqual(page.func, person_view)
