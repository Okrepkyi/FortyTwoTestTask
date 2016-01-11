from .models import Request


class FirstMiddleware(object):

	def process_response(self, request, response):		
		data = Request(request_method=request.META['REQUEST_METHOD'],
						uri=request.path,
						server_protocol=request.META['SERVER_PROTOCOL'],
						status_code = response.status_code,
						content_length=len(response.content)
						)
		data.save()
		return response