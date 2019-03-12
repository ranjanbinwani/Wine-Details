from rest_framework import serializers

from . import models

class WineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WineDetail
        fields = ('id', 'country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery')

    def create(self, validated_data):

        wine = models.WineDetail(
            country=validated_data['country'],
            description=validated_data['description'],
            designation=validated_data['designation'],
            points=validated_data['points'],
            price=validated_data['price'],
            province=validated_data['province'],
            region_1=validated_data['region_1'],
            region_2=validated_data['region_2'],
            variety=validated_data['variety'],
            winery=validated_data['winery']
        )

        wine.save()

        return wine