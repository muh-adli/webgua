import django_tables2 as tables

## Importing Models
from .models import Datatransport

## Create your tables here
class DatatransportTable(tables.Table):
    # call the column and rename the column
    category = tables.Column(verbose_name='Category')
    status = tables.Column(verbose_name='Status')
    station = tables.Column(verbose_name='Station')
    trayek = tables.Column(verbose_name='Trayek')
    stationtransit = tables.Column(verbose_name='Transit')

    class Meta:
        model = Datatransport
        template_name = 'django_tables2/bootstrap.html'  # You can use any template you prefer
        fields = ('category', 'station', 'trayek', 'status', 'stationtransit')
