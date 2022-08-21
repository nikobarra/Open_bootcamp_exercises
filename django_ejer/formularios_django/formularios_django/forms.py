from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='ingrese su nombre', max_length=100, help_text='100 caracteres maximo')
    url = forms.URLField(label='ingrese su url', initial='http://')
    comment = forms.CharField(label='ingrese su comentario')

