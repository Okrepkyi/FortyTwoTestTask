from apps.hello.views import person_view
from django.core.urlresolvers import resolve
from django.test import TestCase
from selenium import webdriver


class PersonPageTest(TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_url_resolves_to_person_page(self):
		page = resolve("/")
		self.assertEqual(page.func, person_view)

	def test_page_content(self):
		self.browser.get('http://localhost:8000')

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('42 Coffee Cups Test Assignment', header_text)

		body_text = self.browser.find_element_by_tag_name('body').text
		self.assertTrue("Name" in body_text) 
		self.assertTrue("Surname" in body_text)
		self.assertTrue("Date of birth" in body_text)
		self.assertTrue("Bio" in body_text)
		self.assertTrue("Jabber" in body_text)
		self.assertTrue("Email" in body_text)
		self.assertTrue("Skype" in body_text)
		self.assertTrue("Other" in body_text)
