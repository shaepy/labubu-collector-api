# pylint: disable=no-member
# this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.views import APIView
# Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework.response import Response
# status gives us a list of official/possible response codes
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Item
from .serializers.common import ItemSerializer
from .serializers.populated import PopulatedItemSerializer


class ItemListView(APIView):
    def get(self, _request):
        books = Item.objects.all()
        serialized_books = ItemSerializer(books, many=True)
        return Response(serialized_books.data, status=status.HTTP_200_OK)

    def post(self, request):
        item_to_add = ItemSerializer(data=request.data)
        try:
            item_to_add.is_valid()
            item_to_add.save()
            return Response(item_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('ERROR')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ItemDetailView(APIView):
    def get_item(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise NotFound(detail="🆘 Can't find that item!")

    def get(self, _request, pk):
        item = self.get_item(pk=pk)
        serialized_item = PopulatedItemSerializer(item)
        return Response(serialized_item.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        item_to_update = self.get_item(pk=pk)
        updated_item = ItemSerializer(item_to_update, data=request.data)

        try:
            updated_item.is_valid()  # is_valid checks the validity of the newly created object
            updated_item.save()  # saves it if it's valid
            return Response(updated_item.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        item_to_delete = self.get_item(pk=pk)
        item_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
