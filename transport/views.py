from django.shortcuts import render
from django.db.models import Count

from .models import Datatransport
from .tables import DatatransportTable
from .forms import transportForm

import plotly.graph_objs as go
import plotly.io as pio
import json

# Create your views here.
def transHome(request):
    title = "Transport"

    # Query data to get counts for each category
    qs = Datatransport.objects.all()
    qs_counts = Datatransport.objects.values('category').annotate(count=Count('id'))
    qs_latlong = Datatransport.objects.values('longitude','latitude')
    
    longitudes = [float(coord['longitude']) for coord in qs_latlong]
    latitudes = [float(coord['latitude']) for coord in qs_latlong]

    # Prepare data for Plotly
    category_counts = {}
    for item in qs_counts:
        category = item['category']
        if category:
            category_counts[category] = category_counts.get(category, 0) + item['count']
    
    # Create Plotly pie chart
    pie_chart = go.Figure(
        data=[
            go.Pie(
                labels=list(
                    category_counts.keys()
                    ),
                values=list(
                    category_counts.values()
                    )
            )
        ]
    )
    
    # Convert plot to JSON
    plot_json = pio.to_json(pie_chart)

    # render the table with the queryset
    table = DatatransportTable(qs[:5])
     
    context = {
        'title': title,
        'plot_json': plot_json,
        'table': table,
        'longitudes': longitudes,
        'latitudes': latitudes,
    }
    return render(request, 'transport/transHome.html', context)

def transMap(request):
    title = "Transport"

    context = {
        'title': title,
    }
    return render(request, 'transport/transMap.html', context)

def transData(request):
    title = "Edit Data"

    form = transportForm()


    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'transport/transEdit.html', context)