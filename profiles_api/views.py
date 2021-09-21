from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
        output = 'hello world!'
        return(Response({'message':'This is demo message', 'output':output}))