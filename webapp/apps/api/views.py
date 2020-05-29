from rest_framework.views import APIView
from mew.core.utils import APIResponse

from api.services import mewTestService


# Create your views here.
class mewTest(APIView):

    def get(self, request):
        """
        Get all folders of project with filters
        :param request:
        :return:
        """
        response = mewTestService().test_function(request)
        return APIResponse.send(response)
