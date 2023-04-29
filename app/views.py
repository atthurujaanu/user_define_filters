from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'HAi Hello hoW ArE You'}
    return render(request,'filters.html',d)