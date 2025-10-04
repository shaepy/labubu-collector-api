from items.serializers.common import ItemSerializer
from series.serializers.populated import PopulatedSeriesSerializer


class PopulatedItemSerializer(ItemSerializer):
    series = PopulatedSeriesSerializer()
