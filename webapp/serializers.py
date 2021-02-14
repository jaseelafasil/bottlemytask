from .models import *
from rest_framework import serializers, fields

class Activityserializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('start_time','end_time')
class Memberserializer(serializers.ModelSerializer):
    activity_periods = Activityserializer(many=True)
    class Meta:
        model = Member
        fields =('id','real_name','tz','activity_periods')

    def create(self, validated_data):
        activity_data = validated_data.pop('activity_periods')
        member = Member.objects.create(**validated_data)
        for activity_data in activity_data:
            Activity.objects.create(memberid=member, **activity_data)
        return member


