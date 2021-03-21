from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.views import APIView

from django.http.response import JsonResponse

class WishListView(APIView):

    # Retrieve Wish List
    def get(self,request):
