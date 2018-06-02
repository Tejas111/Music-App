from django.views import generic
from .models import album
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import UserForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class IndexView(generic.ListView):
    template_name= 't1/index.html'
    def get_queryset(self):
        return album.objects.all()

class DetailView(generic.DetailView):
    model = album
    template_name='t1/detail.html'

class AlbumCreate(CreateView):
    model = album
    fields = ['artist','title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = album
    fields = ['artist','title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = album
    success_url= reverse_lazy('t1:index') 

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False) # just commits doesn't save it
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = album.objects.filter(user=request.user)
                return render(request, 't1/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 't1/registration_form.html', context) 

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                Albums = album.objects.filter(user = request.user)
                return render(request, 't1/index.html', {'albums': Albums})
        else:
            return render(request, 't1/login.html', {'error_message': 'Your account has been disabled'})
    else:
        return render(request, 't1/login.html', {'error_message': 'Invalid login'})
    return render(request, 't1/login.html')


