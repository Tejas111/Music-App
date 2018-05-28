from django.views import generic
from .models import album

class IndexView(generic.ListView):
    template_name= 't1/index.html'
    def get_queryset(self):
        return album.objects.all()

class DetailView(generic.DetailView):
    model = album
    template_name='t1/index.html'

