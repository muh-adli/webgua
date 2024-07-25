# Django core
from django.shortcuts import render

# Django models
from .models import DataGoaWgs84

# Libraries
import json

# Create your views here.
def index(request):
    title = "Homepage"
    
    context = {
        'title' : title,
    }
    
    return render(request, "index copy.html", context)

def guamap(request):
    title = "Map Goa"
    
    qs = DataGoaWgs84.objects.all()
    
    # Prepare arrays for latitudes and longitudes
    latitudes = []
    longitudes = []

    for goa in qs:
        latitudes.append(goa.latitude)
        longitudes.append(goa.longitude)
        
    # features = []

    # for goa in qs:
    #     feature = {
    #         "type": "Feature",
    #         "geometry": {
    #             "type": "Point",
    #             "coordinates": [goa.longitude, goa.latitude]
    #         },
    #         "properties": {
    #             "kode_desa": goa.kode_desa,
    #             "kode_karts": goa.kode_karts,
    #             "nama_objek": goa.nama_objek,
    #             "jenis": goa.jenis,
    #             "x": goa.x,
    #             "y": goa.y,
    #             "z": goa.z,
    #             "provinsi": goa.provinsi,
    #             "kabupaten": goa.kabupaten,
    #             "kecamatan": goa.kecamatan,
    #             "desa": goa.desa,
    #             "dukuh": goa.dukuh,
    #             "tempat_unik": goa.tempat_unik,
    #             "letak": goa.letak,
    #             "akses": goa.akses,
    #             "biota": goa.biota,
    #             "potensi": goa.potensi,
    #             "pemanfaatan": goa.pemanfaatan,
    #             "keterangan": goa.keterangan,
    #         }
    #     }
    #     features.append(feature)

    # geojson = {
    #     "type": "FeatureCollection",
    #     "features": features
    # }

    context = {
        'title': title,
        # 'datagoa': json.dumps(geojson),  # Convert GeoJSON to a JSON string
        'latitudes': latitudes,
        'longitudes': longitudes,
    }
    
    return render(request, "map/goa copy.html", context)