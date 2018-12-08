from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.core.mail import send_mail, BadHeaderError
from .forms import ContatoForm

def home(request):
    data= {}
    return render(request, 'website/home.html', data)

'''
def enviar_contato(request):
    data= {}
    if request.method == 'GET':
        return redirect('url_home')
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = 'Contato enviado pelo site jeto.Pro'
            de_email = 'victor.meireles.dev@gmail.com'
            mensagem = "Nome: "+form.cleaned_data['nome']+" E-mail: "+form.cleaned_data['email']+" Telefone: "+form.cleaned_data['telefone']+" Mensagem: "+form.cleaned_data['mensagem']
            mensagem_html = "Nome: "+form.cleaned_data['nome']+"<br/> E-mail: "+form.cleaned_data['email']+" <br/> Telefone: "+form.cleaned_data['telefone']+" <br/> Mensagem: "+form.cleaned_data['mensagem']
            try:
                send_mail(assunto, mensagem, de_email, ['victordinami@gmail.com','victor.meireles.dev@gmail.com'], html_message=mensagem_html)
            except BadHeaderError:
                data['erro'] = 'Erro ao enviar. Tente novamente mais tarde.'
                return render(request, 'website/home.html', data)
            data['sucesso'] = 'Contato enviado com sucesso! Em breve lhe responderemos.'
            return render(request, 'website/home.html', data)
        else:
            data['erro'] = 'Erro! Preencha todos os campos corretamente e tente novamente.'
            return render(request, 'website/home.html', data)
'''
def enviar_contato(request):
    data= {}
    data['erro'] = 'Erro! Preencha todos os campos corretamente e tente novamente.'
    return render(request, 'website/home.html', data)