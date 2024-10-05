from django import forms
from .models import ArchivoExcel

#SubirArchivoForm
#forms.ModelForm Es la clase base que provee Django para crear formularios basados en modelos
class uploadFileForm(forms.ModelForm):
    
    class Meta:
        #ArchivoExel es una instancia llamado a models.py
        model = ArchivoExcel
        fields = ('nombre','archivo')

def clean_archivo(self):
    archivo = self.cleaned_data.get('archivo')
    if not archivo.name.endswith('.xlsx'):
        raise forms.ValidationError("Solo se permiten archivos Excel.")
    return archivo
