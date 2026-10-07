from django.db import models

# Creacion de modelo / clases
class Arriendo (models.Model):

    opcion_inmueble = [
        ('CASA','Casa'),
        ('DEPARTAMENTO', 'Departamento')
    ]
    
    descripcion = models.TextField()
    tipo_inmueble = models.CharField(max_length=50, choices=opcion_inmueble,default='DEPARTAMENTO')
    direccion = models.CharField(max_length=200)
    precio = models.IntegerField()
    gastos_comunes = models.IntegerField()
    cuartos = models.IntegerField()
    banos = models.IntegerField()
    disponible = models.BooleanField(default=True)
    correo_contacto = models.EmailField()
