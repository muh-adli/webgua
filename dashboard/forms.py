import pyproj

def get_crs_list(): 
    crs_info_list = pyproj.database.query_crs_info(auth_name=None, pj_types=None) 
    CRS_CHOICES = ["EPSG:" + info[1] for info in crs_info_list] 
    return sorted(CRS_CHOICES) 