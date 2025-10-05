# pylint: disable=no-member
# this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.views import APIView
# Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework.response import Response
# status gives us a list of official/possible response codes
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Franchise
from .serializers.common import FranchiseSerializer
from .serializers.populated import PopulatedFranchiseSerializer


class FranchiseListView(APIView):
    def get(self, _request):
        franchise_list = Franchise.objects.all()
        serialized_franchise_list = FranchiseSerializer(
            franchise_list, many=True)
        return Response(serialized_franchise_list.data, status=status.HTTP_200_OK)

    def post(self, request):
        franchise_to_add = FranchiseSerializer(data=request.data)
        try:
            franchise_to_add.is_valid()
            franchise_to_add.save()
            return Response(franchise_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('ERROR')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class FranchiseDetailView(APIView):
    def get_item(self, pk):
        try:
            return Franchise.objects.get(pk=pk)
        except Franchise.DoesNotExist:
            raise NotFound(detail="🆘 Can't find that item!")

    def get(self, _request, pk):
        franchise = self.get_item(pk=pk)
        serialized_franchise = PopulatedFranchiseSerializer(franchise)
        return Response(serialized_franchise.data, status=status.HTTP_200_OK)
