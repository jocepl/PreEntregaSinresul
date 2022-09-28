from django.db import models

# Create your models here.

class colabs(models.Model):

    colab_legajo = models.IntegerField()
    colab_nombre = models.CharField(max_length=40)
    colab_apellido = models.CharField(max_length=40)
    colab_edad = models.IntegerField()
    colab_categoria_venta = models.CharField(max_length=60)

class buyers(models.Model):

    b_nombre = models.CharField(max_length=40)
    b_apellido = models.CharField(max_length=40)
    b_email = models.EmailField()
    b_direccion = models.CharField(max_length=70)
    b_tlf = models.IntegerField()

class sellers(models.Model):

    seller_nombre = models.CharField(max_length=40)
    seller_categoria = models.CharField(max_length=50)
    seller_email = models.EmailField()