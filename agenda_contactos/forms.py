from django import forms  
from agenda_contactos.models import AgendaContacto  

class AgendaContactoForm(forms.ModelForm):  
    class Meta:  
        model = AgendaContacto  
        fields = "__all__" 
