from django.http.response import JsonResponse
from maps.models import Walkroad
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, 'maps/index.html')

def map(request):
    return render(request, 'maps/map.html')

def post(request):
    walkroads = Walkroad.objects.all()
    return render(request, 'maps/post.html', {
        'walkroads': walkroads,
    })

def show(request, id):
    walkroad = Walkroad.objects.get(id=id)
    return render(request, 'maps/show.html', { 
        'walkroad': walkroad,
        'path': walkroad.path
        })

def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        start = request.POST['start']
        finish = request.POST['finish']
        tmi = request.POST['tmi']
        distance = request.POST['distance']
        time = request.POST['time']
        path = request.POST['path']

        walkroad = Walkroad.objects.create(
            author = request.user,
            title = title,
            description = description,
            start = start,
            finish = finish,
            tmi = tmi,
            distance = distance,
            time = time,
            path = path,
            )
        
        print(walkroad)
        return JsonResponse({
            'id': walkroad.id
        })

    return render(request, 'maps/new.html')
        