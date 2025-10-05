# pylint: disable=no-member
# this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.views import APIView
# Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework.response import Response
# status gives us a list of official/possible response codes
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Series
from .serializers.common import SeriesSerializer
from .serializers.populated import PopulatedSeriesSerializer


class SeriesListView(APIView):
    def get(self, _request):
        series_list = Series.objects.all()
        serialized_series_list = SeriesSerializer(series_list, many=True)
        return Response(serialized_series_list.data, status=status.HTTP_200_OK)

    def post(self, request):
        series_to_add = SeriesSerializer(data=request.data)
        try:
            series_to_add.is_valid()
            series_to_add.save()
            return Response(series_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('ERROR')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


# shoould also return ALL the items in that series set
class SeriesDetailView(APIView):
    def get_a_series(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise NotFound(detail="🆘 Can't find that series!")

    def get(self, _request, pk):
        series = self.get_a_series(pk=pk)
        serialized_series = PopulatedSeriesSerializer(series)
        return Response(serialized_series.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        series_to_update = self.get_a_series(pk=pk)
        updated_series = SeriesSerializer(series_to_update, data=request.data)

        try:
            updated_series.is_valid()  # is_valid checks the validity of the newly created object
            updated_series.save()  # saves it if it's valid
            return Response(updated_series.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        series_to_delete = self.get_a_series(pk=pk)
        series_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
