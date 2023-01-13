import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'REST.settings')
django.setup()

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


class EX:
    def __init__(self, first_name, old):
        self.first_name = first_name
        self.old = old


class EXSerialazer(serializers.Serializer):
    first_name = serializers.CharField(max_length=128)
    old = serializers.IntegerField()

    def validate_old(self, value):
        if value <= 0:
            raise serializers.ValidationError("Возраст не может быть отрицательным")
        return value

    def validate(self, attrs):
        if attrs["first_name"] == 'Dima' and attrs["old"] != 20:
            raise serializers.ValidationError("Диме 20 лет уже!!")
        return attrs
    def create(self, validated_data):
        return EX(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.old = validated_data.get('old', instance.old)
        return instance


data = {'first_name': 'Dima', 'old': 20}
serializer = EXSerialazer(data=data)
serializer.is_valid()
author = serializer.save()
print(author.first_name)

new_data = {'old': 20}
serializer = EXSerialazer(author, data=new_data, partial=True)
serializer.is_valid()
serializer.save()
print(author.first_name, author.old)
