from rest_framework.views import APIView
from rest_framework.response import Response


class TestAPIView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        users = [
            {"id": 1, "first_name": "Jhon", "last_name:": "Wick", "age": 41},
            {"id": 2, "first_name": "Elon", "last_name:": "Mask", "age": 47},
            {"id": 3, "first_name": "Nikola", "last_name:": "Tesla", "age": 45}
        ]
        return Response(users)
