from cowsay_app.models import message
from django.shortcuts import render
from cowsay_app.models import message
from cowsay_app.form import addmessageForm
import subprocess

# Create your views here.
def index_view(request):
    if request.method == 'POST':
        form = addmessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data    
            message.objects.create(text=data['text'])
            messages = subprocess.check_output(['cowsay', data['text']], universal_newlines=True)
            return render(request, 'index.html', {'messages': messages, 'form': form})
    
    form = addmessageForm()
    return render(request, 'index.html', {'form': form})

def history(request):
    latest_messages = message.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {'latest_messages':latest_messages})