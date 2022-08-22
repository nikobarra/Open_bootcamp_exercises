from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='ingrese su nombre', max_length=100, help_text='100 caracteres maximo')
    url = forms.URLField(label='ingrese su url', initial='http://')
    comment = forms.CharField(label='ingrese su comentario')


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    message = forms.CharField (label='Mensaje',widget=forms.Textarea(attrs={'class':'form-control'}))
    
    #validacion de formulario con metodo clean 
    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'Juan':
            raise forms.ValidationError('No puede ser Juan')
        return name
    
