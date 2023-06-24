from django.db import models
from django.contrib.auth.models import User

class Aktyor(models.Model):
    ism = models.CharField(max_length=45)
    davlat = models.CharField(max_length=50)
    tugilgan_yil = models.DateField()
    jins = models.CharField(max_length=30)
    def __str__(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=50)
    janr = models.CharField(max_length=40)
    yil = models.DateField()
    davomiyligi = models.DurationField()
    aktyor = models.ManyToManyField(Aktyor)
    reting = models.FloatField()
    def __str__(self):
        return self.nom

class Izoh(models.Model):
    matn = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sana = models.DateField()
    baho = models.PositiveSmallIntegerField()
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    def __str__(self):
        return self.matn