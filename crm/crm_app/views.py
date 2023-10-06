from django.shortcuts import render
from .models import Record
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        record = Record.objects.all()
        return render(request, 'index.html',{'record': record})
    else:
        messages.success(request, "You need to login")
        return render(request,'index.html')


def single_record(request,pk):

    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You need to login")
        return render(request,'index.html')