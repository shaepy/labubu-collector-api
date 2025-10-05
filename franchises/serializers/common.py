from rest_framework import serializers
from franchises.models import Franchise
from series.serializers.common import SeriesSerializer


class FranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchise
        fields = '__all__'