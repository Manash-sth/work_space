from rest_framework.views import APIView
from rest_framework.response import Response

class TestApi(APIView):
    def get(self, rrequest):
        return Response({"auth": "HelloWorld"})