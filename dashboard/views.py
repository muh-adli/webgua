# Django core
from django.shortcuts import render
from django.views.generic import ListView

# Django models and table
from .models import DataGoaWgs84
from .tables import tableDataGoa
from .forms import *

# Libraries
import json
import pyproj

# Create your views here.
def index(request):
    title = "Homepage"
    
    context = {
        'title' : title,
    }
    
    return render(request, "index.html", context)

def homepage(request):
    title = "Home"
    context = {
        'title' : title,
    }
    return render(request, "homepage.html", context)

def coorConvert(request):
    title = "Coordinate Converter"
    CRS_CHOICES = get_crs_list()
    wgs84 = pyproj.CRS('EPSG:4326')
    utm = pyproj.CRS('EPSG:32749') 
    context = {
        'title' : title,
        'crs_choices': CRS_CHOICES
    }
    context['formUTM']= formUTM()
    context['formWGS']= formWGS()
    if request.POST:
        if request.POST['typeform'] == "utm":
            print ("utm")
            x = float(request.POST.get('input_x'))
            y = float(request.POST.get('input_y'))
            transformer = pyproj.Transformer.from_crs(utm,wgs84, always_xy=True)
            long, lat = transformer.transform(x, y)
            print(f"UTM Coordinates: {lat}, {long}")
            resultWGS ={
                'input_lat' : lat,
                'input_long' : long,
            }
            resultUTM = {
                'input_x' : x,
                'input_y' : y
            }
            print (formUTM(resultUTM))
            context['formUTM']= formUTM(resultUTM)
            context['formWGS']= formWGS(resultWGS)
            
        elif request.POST['typeform'] == "wgs":
            print ("wgs")
            input_latitude = float(request.POST.get('input_lat'))
            input_longitude = float(request.POST.get('input_long'))
            print (input_latitude)
            print (input_longitude)
            transformer = pyproj.Transformer.from_crs(wgs84, utm, always_xy=True)
            x_output, y_output = transformer.transform(input_longitude, input_latitude)
            print(f"UTM Coordinates: {x_output}, {y_output}")
            resultWGS ={
                'input_lat' : input_latitude,
                'input_long' : input_longitude,
            }
            resultUTM = {
                'input_x' : x_output,
                'input_y' : y_output
            }
            print (formUTM(resultUTM))
            context['formUTM']= formUTM(resultUTM)
            context['formWGS']= formWGS(resultWGS)
        else:
            print ("eror")



        # print("masuk post")
        # print(f"""
        #     ini isi wgs
        #     {request.POST.get('input_long'), request.POST.get('input_lat')}
        #     ini isi utm
        #     {request.POST.get('input_x'), request.POST.get('input_y')}
        # """)

        # input_latitude = float(request.POST.get('input_lat'))
        # input_longitude = float(request.POST.get('input_long'))
        # input_x = float(request.POST.get('input_x'))
        # input_y = float(request.POST.get('input_y'))

        # # if input_latitude
        # transformer = pyproj.Transformer.from_crs(wgs84, utm, always_xy=True)
        # x_output, y_output = transformer.transform(input_longitude, input_latitude)
        # print(f"UTM Coordinates: {x_output}, {y_output}")
        # results = {
        #     'input_x' : x_output,
        #     'input_y' : y_output,
        #     'input_lat' : input_latitude,
        #     'input_long' : input_longitude,
        #     'input_crs' : "crs"
        # }
        # print(results)
        # for a, b in results.items():
            # print (b)
        # result = coordinateForm(results)
        # context = {
        #     'form': result
        # }
        # return render(request, "coorconv/coorconv.html", context)

    #     elif form_type=="utm":
    #         input_x = float(request.POST.get('X'))
    #         input_y = float(request.POST.get('Y'))
    #         print("INI INPUTNYA LATLONG")
    #         transformer = pyproj.Transformer.from_crs(utm,wgs84, always_xy=True)
    #         long, lat = transformer.transform(input_x, input_y)
    #         print(f"UTM Coordinates: {lat}, {long}")
    #         context['output_x'] = input_x
    #         context['output_y'] = input_y
    #         context['output_lat'] = lat
    #         context['output_long'] = long


    # else:
    #     context['crs_choices']: CRS_CHOICES


    return render(request, "coorconv/coorconv.html", context)


def guamap(request):
    title = "Map Goa"
    
    # qs = DataGoaWgs84.objects.all()
    
    # # Prepare arrays for latitudes and longitudes
    # latitudes = []
    # longitudes = []

    # for goa in qs:
    #     latitudes.append(goa.latitude)
    #     longitudes.append(goa.longitude)
        
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
        # 'latitudes': latitudes,
        # 'longitudes': longitudes,
    }
    
    return render(request, "map/goa copy.html", context)

def tabel(request):
    qs = DataGoaWgs84.objects.all()[:10]
    
    # Prepare arrays for latitudes and longitudes
    nama_objek = []
    latitude = []
    longitude = []
    print(qs)
    for goa in qs:
        nama_objek.append(goa.nama_objek)
        latitude.append(goa.latitude)
        longitude.append(goa.longitude)
    
    listobj = {nama: {'latitude': latitude, 'longitude': longitude} 
           for nama, latitude, longitude in zip(nama_objek, latitude, longitude)}

    table = tableDataGoa(qs)

    context= {
        'data' : qs,
        'table' : table
    }
    print (listobj)
    return render (request, "map/tabel.html", context)
        
def tabelEdit(request, objek):
    qs = DataGoaWgs84.objects.all().filter(nama_objek=objek)
    
    # Prepare arrays for latitudes and longitudes
    nama_objek = []
    latitude = []
    longitude = []
    print(qs)
    for goa in qs:
        nama_objek.append(goa.nama_objek)
        latitude.append(goa.latitude)
        longitude.append(goa.longitude)
    
    listobj = {nama: {'latitude': latitude, 'longitude': longitude} 
           for nama, latitude, longitude in zip(nama_objek, latitude, longitude)}

    table = tableDataGoa(qs)

    context= {
        'data' : qs,
        'table' : table
    }
    print (listobj)
    return render (request, "map/tabel.html", context)
