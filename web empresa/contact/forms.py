from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", min_length=3, max_length=100, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nombre'
        }
    ))
    email = forms.EmailField(label="Email", min_length=3, max_length=100, required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))
    content = forms.CharField(label="Contenido", min_length=10, max_length=1000, required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'Escribe tu mensaje'
        }
    ))