
from django import forms


class MensajeForm(forms.Form):
    remitente=forms.CharField(max_length=40)
    recibido=forms.CharField(max_length=40)
    mensaje=forms.CharField(max_length=1200)
    fecha=forms.DateField()
    esLeido=forms.BooleanField()