from django import forms #modulo form
from .models import Arriendo #importamos modelo arriendo

class FormCrear(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = '__all__' # indica a django: que campos se van a incluir
    def clean(self):
        cleaned_data = super().clean() #obtenemos el diccionario completo de datos procesados

        precio = cleaned_data.get('precio')
        gastos_comunes = cleaned_data.get('gastos_comunes')
        cuartos = cleaned_data.get('cuartos')
        banos = cleaned_data.get('banos')

        if precio is not None and gastos_comunes is not None and cuartos is not None and banos is not None:
            if precio <= 0 or gastos_comunes <= 0 or cuartos <=0 or banos <=0:
                raise forms.ValidationError("los campos precio, gasto comun, cuartos  y baño deben ser mayor a cero")
        else:
            raise forms.ValidationError("todos los campos son obligatorios")
        return cleaned_data
class FormEditar(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['descripcion','precio','gastos_comunes','disponible','correo_contacto'] #especificamos los campos que se pueden editar
    def clean(self):
                cleaned_data = super().clean() #obtenemos el diccionario completo de datos procesados
        
                precio = cleaned_data.get('precio')
                gastos_comunes = cleaned_data.get('gastos_comunes')
        
                if precio is not None and gastos_comunes is not None:
                    if precio <= 0 or gastos_comunes <= 0:
                        raise forms.ValidationError("los campos precio, gasto comun deben ser mayor a cero")
                else:
                    raise forms.ValidationError("todos los campos son obligatorios")
                return cleaned_data