from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class HelloAPIView(APIView):
    def get(self,request):
        d={
            "xabar": "Salom Dunyo",
            "sana":"2023-06-22"
        }
        return Response(d)

    def post(selfself, request):
        malumot = request.data
        d = {
            "xabar": "Post qabul qilindi",
            "post_malumoti": malumot
        }
        return Response(d)

class AktyorlarAPIView(APIView):
    def get(self,request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar, many =True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = AktyorSerializer(data = malumot)
        if serializer.is_valid():
            Aktyor.objects.create(
                ism = serializer.validated_data.get('ism'),
                davlat = serializer.validated_data.get('davlat'),
                tugilgan_yil = serializer.validated_data.get('tugilgan_yil'),
                jins = serializer.validated_data.get('jins'),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AktyorAPIView(APIView):
    def get(self,request,pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)

class IzohlarAPIView(APIView):
    def get(self,request):
        izohlar = Izoh.objects.all()
        serializer = IzohSerializer(izohlar, many =True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = IzohSaveSerializer(data = malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IzohAPIView(APIView):
    def get(self,request,pk):
        izoh = Izoh.objects.get(id=pk)
        serializer = IzohSerializer(izoh)
        return Response(serializer.data)

class AktyorOchirAPIView(APIView):
    def delete(self,request,pk):
        aktyor = Aktyor.objects.get( pk=pk)
        aktyor.delete()
        return Response({"habar" : "Aktyor malumoti ochirildi"})

class KinolarAPIView(APIView):
    def get(self, request):
        kinolar = Kino .objects.all()
        serializer = KinoSerializer(kinolar, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self,request):
        kino = request.data
        serializer = KinoSaveSerializer(data=kino)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KinoDetalView(APIView):
    def get(self , request, pk):
        kino = Kino.objects.get(id=pk)
        serializer = KinoSerializer(kino)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        Kino.objects.get(id=pk).delete()
        return Response({"xabar":"Kino ma'lumoti o'chirildi."}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        kino = Kino.objects.get(id = pk)
        malumot = request.data
        serializer = KinoSaveSerializer(kino, data = malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)