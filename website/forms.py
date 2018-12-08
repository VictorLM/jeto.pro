from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefone = forms.CharField(required=False)
    mensagem = forms.CharField(widget=forms.Textarea, required=True)