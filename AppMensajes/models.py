from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Mensajes(models.Model):
    remitente=models.ForeignKey(User, related_name='remitente', on_delete=models.CASCADE)
    recibido=models.ForeignKey(User, related_name='recibido', on_delete=models.CASCADE)
    mensaje=models.CharField(max_length=1200)
    fecha=models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.mensaje

    class Meta:
        ordering = ('fecha',)