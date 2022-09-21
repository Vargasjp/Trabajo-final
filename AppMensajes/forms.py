from django import forms
from ckeditor.widgets import CKEditorWidget

class DateImput(forms.DateInput):
    input_type = 'date'


class MensajesForm(forms.Form):
    mensaje=forms.CharField(widget=CKEditorWidget())

class BuscarMensajesForm(forms.Form):
    remitente=forms.CharField(max_length=50)
    recibido=forms.CharField(max_length=50)
    mensaje=forms.CharField(max_length=50)
    