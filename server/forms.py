from .models import InputData
from django.forms import ModelForm, TextInput, Textarea

class InputDataForm(ModelForm):
    class Meta:
        model = InputData
        fields = ['name', 'addr', 'ip', 'nFuzz', 'avar', 'opis']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование',
            }),
            'addr': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адресс Цели',

            }),
            'ip': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ip Хоста',

            }),
            'nFuzz': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Число fuzz',

            }),
            'avar': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Завершение при аварии',

            }),
            'opis': Textarea(attrs={
                'rows': 6, 
                'cols': 40,
                'class': 'form-control',
                'placeholder': 'Описание',

            }),
            
        }