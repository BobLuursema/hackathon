from django.utils.deprecation import MiddlewareMixin
class CorsMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET'
        #response['Content-Type'] = 'application/json'
        #response['Accept'] = 'application/json'
        return response