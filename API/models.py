from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class ApiDatagoa(models.Model):
    id = models.BigAutoField(primary_key=True)
    kode_desa = models.CharField(max_length=50, blank=True, null=True)
    kode_karts = models.CharField(max_length=50, blank=True, null=True)
    nama_objek = models.CharField(max_length=50, blank=True, null=True)
    jenis = models.CharField(max_length=20, blank=True, null=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField(blank=True, null=True)
    provinsi = models.CharField(max_length=50, blank=True, null=True)
    kabupaten = models.CharField(max_length=50, blank=True, null=True)
    kecamatan = models.CharField(max_length=50, blank=True, null=True)
    desa = models.CharField(max_length=50, blank=True, null=True)
    dukuh = models.CharField(max_length=50, blank=True, null=True)
    tempat_unik = models.CharField(max_length=100, blank=True, null=True)
    letak = models.CharField(max_length=50, blank=True, null=True)
    akses = models.CharField(max_length=50, blank=True, null=True)
    biota = models.CharField(max_length=50, blank=True, null=True)
    potensi = models.CharField(max_length=50, blank=True, null=True)
    pemanfaatan = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=500, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'API_datagoa'

class DataGoaView(models.Model):
    kode_desa = models.CharField(max_length=50, blank=True, null=True)
    kode_karts = models.CharField(max_length=50, blank=True, null=True)
    nama_objek = models.CharField(max_length=50, blank=True, null=True)
    jenis = models.CharField(max_length=20, blank=True, null=True)
    geom_4326 = models.PointField(blank=True, null=True)
    provinsi = models.CharField(max_length=50, blank=True, null=True)
    kabupaten = models.CharField(max_length=50, blank=True, null=True)
    kecamatan = models.CharField(max_length=50, blank=True, null=True)
    desa = models.CharField(max_length=50, blank=True, null=True)
    dukuh = models.CharField(max_length=50, blank=True, null=True)
    tempat_unik = models.CharField(max_length=100, blank=True, null=True)
    letak = models.CharField(max_length=50, blank=True, null=True)
    akses = models.CharField(max_length=50, blank=True, null=True)
    biota = models.CharField(max_length=50, blank=True, null=True)
    potensi = models.CharField(max_length=50, blank=True, null=True)
    pemanfaatan = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'data_goa_view'




class Aff(models.Model):
    hewan = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aff'

class DataGoa(models.Model):
    kode_desa = models.CharField(max_length=50, blank=True, null=True)
    kode_karts = models.CharField(max_length=50, blank=True, null=True)
    nama_objek = models.CharField(max_length=50, blank=True, null=True)
    jenis = models.CharField(max_length=20, blank=True, null=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField(blank=True, null=True)
    provinsi = models.CharField(max_length=50, blank=True, null=True)
    kabupaten = models.CharField(max_length=50, blank=True, null=True)
    kecamatan = models.CharField(max_length=50, blank=True, null=True)
    desa = models.CharField(max_length=50, blank=True, null=True)
    dukuh = models.CharField(max_length=50, blank=True, null=True)
    tempat_unik = models.CharField(max_length=100, blank=True, null=True)
    letak = models.CharField(max_length=50, blank=True, null=True)
    akses = models.CharField(max_length=50, blank=True, null=True)
    biota = models.CharField(max_length=50, blank=True, null=True)
    potensi = models.CharField(max_length=50, blank=True, null=True)
    pemanfaatan = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_goa'