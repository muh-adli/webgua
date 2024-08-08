from django import forms
import pyproj

def get_crs_list(): 
    crs_info_list = pyproj.database.query_crs_info(auth_name=None, pj_types=None) 
    CRS_CHOICES = ["EPSG:" + info[1] for info in crs_info_list] 
    return sorted(CRS_CHOICES) 

class formUTM(forms.Form):
    input_x = forms.FloatField(required=False)
    input_y = forms.FloatField(required=False)
    input_crs = forms.CharField(required=False, max_length = 15)

class formWGS(forms.Form):
    input_lat = forms.FloatField(required=False)
    input_long = forms.FloatField(required=False)