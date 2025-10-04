from series.serializers.common import SeriesSerializer
from franchises.serializers.common import FranchiseSerializer


class PopulatedSeriesSerializer(SeriesSerializer):
    franchise = FranchiseSerializer()
