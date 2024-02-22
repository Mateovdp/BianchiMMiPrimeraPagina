from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=20) 
    apellido=models.CharField(max_length=20) 
    documento=models.IntegerField() 
    localidad=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} DNI:{self.documento}"
