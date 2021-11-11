from rest_framework import serializers
from .models import StudentUser
class StudentUSerserializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.CharField(max_length=100)
    mobile = serializers.CharField(max_length=10)
    image = serializers.CharField(max_length=10)
    gender = serializers.CharField(max_length=10)
    type = serializers.CharField(max_length=10)
    resume = serializers.CharField(max_length=10)

    def create(self, validate_data):
        return StudentUser.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.user = validated_data.get('user', instance.user)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.image = validated_data.get('image', instance.image)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.type = validated_data.get('type', instance.type)
        instance.resume = validated_data.get('resume', instance.resume)
        instance.save()
        return instance