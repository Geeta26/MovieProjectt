from django.shortcuts import render
from TestApp.forms import MovieForm
from TestApp.models import Movie

# Create your views here.
def home_view(request):
    return render(request,'testApp/home.html')


def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return home_view(request)
    return render(request, 'testApp/add.html', {'form': form})

def list_movie_view(request):
    movies_list = Movie.objects.all()
    return render(request, 'testApp/list.html', {'movies_list': movies_list})