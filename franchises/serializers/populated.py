from franchises.serializers.common import FranchiseSerializer
from series.serializers.common import SeriesSerializer


class PopulatedFranchiseSerializer(FranchiseSerializer):
    series = SeriesSerializer(many=True)
