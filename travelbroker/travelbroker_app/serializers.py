from rest_framework import serializers
from travelbroker_app.models import Passengers

class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passengers
        fields = ('id', 'Firstname', 'Lastname', 'Travel_point')
