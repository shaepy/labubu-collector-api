from items.serializers.common import ItemSerializer
from series.serializers.common import SeriesSerializer


class PopulatedItemSerializer(ItemSerializer):
    series = SeriesSerializer()
