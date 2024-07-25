from django.shortcuts import render

# Create your views here.
def index(request):
    title = "index"
    
    context = {
        'title' : title,
    }
    
    return render(request, "index copy.html", context)

def guamap(request):
    title = "index"
    
    context = {
        'title' : title,
    }
    
    return render(request, "map/goa.html", context)