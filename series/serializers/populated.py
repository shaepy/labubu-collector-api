from series.serializers.common import SeriesSerializer
from franchises.serializers.common import FranchiseSerializer
from items.serializers.common import ItemSerializer

class PopulatedSeriesSerializer(SeriesSerializer):
    franchise = FranchiseSerializer()
    items = ItemSerializer(many=True)
