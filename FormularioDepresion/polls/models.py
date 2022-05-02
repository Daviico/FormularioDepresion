from pyexpat import model
from tkinter import CASCADE
from django.db import models

class Pregunta(models.Model): 
    pregunta_detalle = models.CharField(max_length=200)

    def __str__(self):
        return self.pregunta_detalle


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_detalle = models.CharField(max_length=200)

    def __str__(self):
        return self.respuesta_detalle


class Encuestado(models.Model):
    id_encuestado = models.IntegerField(default=0, primary_key=True)
    
    def __str__(self):
        return self.id_encuestado



class Encuesta(models.Model):
    encuestado = models.ForeignKey(Encuestado, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.encuestado, self.respuesta