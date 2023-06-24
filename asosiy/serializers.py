from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Kino
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Aktyor, Kino, Izoh

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class AktyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktyor
        fields = '__all__'

class KinoSerializer(serializers.ModelSerializer):
    aktyor = AktyoSerializer(many=True)
    class Meta:
        model = Kino
        fields = '__all__'

class KinoSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    kino = KinoSerializer(read_only=True)
    class Meta:
        model = Izoh
        fields = ['id', 'matn', 'user', 'sana', 'baho', 'kino']

class IzohSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = ['id', 'matn', 'user', 'sana', 'baho', 'kino']

class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    davlat = serializers.CharField(max_length=30)
    jins = serializers.CharField(max_length=10)
    tugilgan_yil = serializers.DateField()





