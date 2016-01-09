from models import HttpRequests


class HttpRequestsMiddleware(object):

	def requests_middleware(self, request, response):
		request_data = HttpRequests(method=request.META["REQUEST_METHOD"],
									uri=request.path,
									protocol=request.META["SERVER_PROTOCOL"],
									status_code=response.status_code,
									content_length=len(response.content))
		data.save()