from django import forms
from .models import Arriendo

class FormCrear(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = '__all__'

    # Transformación automática de la dirección a MAYÚSCULAS
    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if direccion:
            return direccion.strip().upper()
        return direccion

    def clean(self):
        cleaned_data = super().clean()
        
        # 1. Si no viene tipo_inmueble en el formulario (caso FormEditar), lo obtenemos de la instancia guardada
        tipo_inmueble = cleaned_data.get('tipo_inmueble')
        if not tipo_inmueble and self.instance and self.instance.pk:
            tipo_inmueble = self.instance.tipo_inmueble

        # 2. Si tampoco viene direccion (caso FormEditar), la recuperamos de la instancia
        direccion = cleaned_data.get('direccion')
        if not direccion and self.instance and self.instance.pk:
            direccion = self.instance.direccion

        numero_depto = cleaned_data.get('numero_depto')
        precio = cleaned_data.get('precio')
        gastos_comunes = cleaned_data.get('gastos_comunes')

        # A) Validaciones de montos
        if precio is not None and precio <= 0:
            self.add_error('precio', "El precio del arriendo debe ser mayor a $0.")

        if gastos_comunes is not None and gastos_comunes <= 0:
            self.add_error('gastos_comunes', "Los gastos comunes no pueden ser un valor negativo o igual a cero.")

        # B) Exigencia de N° Depto si el tipo es DEPARTAMENTO (verificando que tipo_inmueble no sea None)
        if tipo_inmueble and tipo_inmueble.upper() == 'DEPARTAMENTO':
            if not numero_depto:
                self.add_error('numero_depto', "Debe especificar el número o bloque del departamento.")

        # C) Control de duplicidad
        if direccion:
            coincidencias = Arriendo.objects.filter(
                direccion=direccion, 
                numero_depto=numero_depto
            )
            
            if self.instance and self.instance.pk:
                coincidencias = coincidencias.exclude(pk=self.instance.pk)

            if coincidencias.exists():
                self.add_error(
                    'numero_depto', 
                    f"Ya existe un registro en '{direccion}' " + 
                    (f"depto {numero_depto}" if numero_depto else "") + "."
                )

        return cleaned_data


class FormEditar(FormCrear):
    class Meta:
        model = Arriendo
        fields = ['descripcion', 'numero_depto', 'precio', 'gastos_comunes', 'disponible', 'correo_contacto']