from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework_simplejwt.authentication import BaseJSONWebTokenAuthentication

class JSONWebTokenAuthenticationQS(JSONWebTokenAuthentication):
    def get_jwt_value(self, request):
         return request.query_params.get('jwt')