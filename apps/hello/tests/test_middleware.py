from apps.hello.models import Request
from django.core.urlresolvers import reverse
from django.test import TestCase


class MiddlewareTest(TestCase):

    def test_middleware(self):
        response = self.client.get("/request_list/")
        self.assertEqual(response.status_code, 200)