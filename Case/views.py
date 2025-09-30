from django.shortcuts import render, redirect
from Case.utils import bot_classifica,gerar_resposta
from Case.models import Resultado
from django.contrib import messages
from Case.forms import EmailForm


def index(request):
    form = EmailForm
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            email_save = form.save(commit=False)
            if not email_save.file:                
                resultado = Resultado()
                if Resultado.objects.exists():
                    resultado.id = Resultado.objects.count() + 1
                else:
                    resultado.id = 1
                resultado.classificacao = bot_classifica(email_save.text)
                if resultado.classificacao == "Produtivo":
                    resultado.resposta = gerar_resposta(email_save.text, True)
                else:
                    resultado.resposta = gerar_resposta(email_save.text, False)
                resultado.save()
                return redirect('resultado', resultado.id)
            else:
                try:
                    conteudo = email_save.file.read().decode('utf-8')
                    resultado = Resultado()
                    if Resultado.objects.exists():
                        resultado.id = Resultado.objects.count() + 1
                    else:
                        resultado.id = 1
                    resultado.classificacao = bot_classifica(conteudo)
                    if resultado.classificacao == "Produtivo":
                        resultado.resposta = gerar_resposta(conteudo, True)
                    else:
                        resultado.resposta = gerar_resposta(conteudo, False)
                    resultado.save()
                    return redirect('resultado', resultado.id)
                except:
                    messages.error(request, 'Porfavor, adicione um documento com um email válido!')
        else:
            if 'file' in form.errors:
                if any('extens' in e.lower() for e in form.errors['file']):
                    messages.error(request, 'Apenas documentos pdf e txt são aceitos!')
                else:
                    messages.error(request, 'Apenas um dos campos deve ser preenchido')
            elif '__all__' in form.errors:
                messages.error(request, 'Apenas um dos campos deve ser preenchido')
    return render(request, 'index.html', {'form':form})

def resultado(request, id):
    resultado = Resultado.objects.filter(id = id).get()
    return render(request, 'resultado.html', {'resultado' : resultado})