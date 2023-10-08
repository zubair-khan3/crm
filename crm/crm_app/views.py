from django.shortcuts import render,redirect
from .models import Record
from django.contrib import messages
from .forms import AddRecord
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        record = Record.objects.all()
        
        paginator = Paginator(Record.objects.all(), 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        total_pages = page_obj.paginator.num_pages
        print(total_pages)

        return render(request, 'index.html',{'record': record, 'page_obj': page_obj, 'total_pages':range(1,total_pages +1)})
    else:
        messages.success(request, "You need to login")
        return render(request,'index.html')


def single_record(request,pk):
    
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        user_str = str(request.user)
        print("user type" , request.user,type(user_str))
        
        print("user type",type(customer_record.created_by))
        return render(request, 'single_record.html', {'customer_record':customer_record, 'user_str':user_str})
    else:
        messages.success(request, "You need to login")
        return render(request,'index.html')

def user_profile(request, pk):
    user_info = Record.objects.get(id=pk)
    return render(request, "user_profile.html",{'user_info': user_info})


def confirm_delete(request, pk):
    user_id = pk
    
    return render(request,'confirm_delete.html',{'user_id':user_id})

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request,"Data Deleted")
        return redirect('index') 
    else:
        messages.success(request,"You are not authorized ")
        return render(request,"index.html")
    


def add_record(request):
    form = AddRecord()
    if request.user.is_authenticated:
        if request.method== "POST":
            form = AddRecord(request.POST)
            if form.is_valid():
                form_save = form.save(commit=False)
                form_save.created_by = request.user
                form_save.save()
                messages.success(request,"Data Add")
                return redirect('index')

    return render(request, "add_record.html",{'form':form})

def update_record(request,pk):
    if request.user.is_authenticated:
        user_data = Record.objects.get(id=pk)
        
        form = AddRecord(request.POST or None, instance=user_data)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Updated")
            return redirect('index')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request, 'You need to login')
        return render(request,'index.html')



    return render(request,'update_record.html')

def search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            searched = request.POST['search']
            searched_date = Record.objects.filter(first_name__icontains =searched)

            return render(request,'search.html',{'searched':searched,'searched_data':searched_date})
    else:
        messages.success(request,"you need to login")
        return render(request,'index.html')
