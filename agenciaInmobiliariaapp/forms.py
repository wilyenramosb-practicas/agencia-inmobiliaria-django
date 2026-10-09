import re
from django import forms
from .models import Arriendo

class FormCrear(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = '__all__'  # Todos los campos para la creación

    # 1. Transformación automática del campo dirección a MAYÚSCULAS
    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if direccion:
            return direccion.strip().upper()
        return direccion

    # 2. Validaciones de negocio y lógica cruzada
    def clean(self):
        cleaned_data = super().clean()
        
        tipo_inmueble = cleaned_data.get('tipo_inmueble')
        direccion = cleaned_data.get('direccion')
        precio = cleaned_data.get('precio')
        gastos_comunes = cleaned_data.get('gastos_comunes')

        # Validar precio y gastos comunes
        if precio is not None and precio <= 0:
            self.add_error('precio', "El precio del arriendo debe ser mayor a $0.")

        if gastos_comunes is not None and gastos_comunes < 0:
            self.add_error('gastos_comunes', "Los gastos comunes no pueden ser un valor negativo.")

        # Reglas para Dirección y Tipo de Inmueble
        if tipo_inmueble and direccion:
            
            # Exigir número/unidad si es un DEPARTAMENTO
            if tipo_inmueble.upper() == 'DEPARTAMENTO':
                tiene_unidad = re.search(r'(DEPTO|DPTO|PISO|N°|NUMERO|\b\d{2,4}\b)', direccion)
                if not tiene_unidad:
                    self.add_error(
                        'direccion', 
                        "Para un departamento es obligatorio incluir el número de unidad en la dirección (Ej: 'AV. BRASIL 123, DEPTO 402')."
                    )

            # Control de duplicidad en la BD
            coincidencias = Arriendo.objects.filter(direccion=direccion)
            if self.instance and self.instance.pk:
                coincidencias = coincidencias.exclude(pk=self.instance.pk)

            if tipo_inmueble.upper() == 'CASA' and coincidencias.exists():
                self.add_error('direccion', f"La casa registrada en '{direccion}' ya existe en la base de datos.")

        return cleaned_data


class FormEditar(FormCrear):
    class Meta:
        model = Arriendo
        # Especificamos únicamente los campos permitidos para la edición
        fields = ['descripcion', 'precio', 'gastos_comunes', 'disponible', 'correo_contacto']

    # Hereda automáticamente las funciones clean_direccion() y clean() de FormCrear