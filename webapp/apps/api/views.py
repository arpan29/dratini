from rest_framework.views import APIView
from mew.core.utils import APIResponse

from api.services import MyService


# Create your views here.
class MyView(APIView):

    def get(self, request):
        """
        Get all folders of project with filters
        :param request:
        :return:
        """
        response = MyService().test_function(request)
        return APIResponse.send(response)
