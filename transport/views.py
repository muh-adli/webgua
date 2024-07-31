from django.shortcuts import render
from .models import Datatransport

from django.db.models import Count

import plotly.graph_objs as go
import plotly.io as pio
import json

# Create your views here.
def transHome(request):
    title = "Transport"

    # Query data to get counts for each category
    qs = Datatransport.objects.values('category').annotate(count=Count('id'))
    
    # Prepare data for Plotly
    category_counts = {}
    for item in qs:
        category = item['category']
        if category:
            category_counts[category] = category_counts.get(category, 0) + item['count']
    
    # Create Plotly pie chart
    pie_chart = go.Figure(data=[go.Pie(labels=list(category_counts.keys()), values=list(category_counts.values()))])
    pie_chart.update_layout(title='Transport Category Distribution')
    
    # Convert plot to JSON
    plot_json = pio.to_json(pie_chart)
     
    context = {
        'title': title,
        'plot_json': plot_json,
    }
    return render(request, 'transport/transHome.html', context)

def transMap(request):
    title = "Transport"

    context = {
        'title': title,
    }
    return render(request, 'transport/transMap.html', context)