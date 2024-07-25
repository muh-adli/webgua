from django.utils.html import format_html

import django_tables2 as tables

from .models import DataGoaWgs84

# Tulis table django-tables2 disini
class tableDataGoa(tables.Table):
    edit = tables.Column(
        empty_values=(), 
        orderable=False, 
        verbose_name='Edit'
    )

    def render_edit(self, record):
        return format_html(
            f'<a href="/{record.nama_objek}">{record.nama_objek}</a>'
            )


    class Meta:
        model = DataGoaWgs84
        fields = ("nama_objek","longitude","latitude", "dukuh")
        attrs = {
            'class': 'table table-striped table-bordered',
            'thead': {'class': 'thead-dark'},
            'th': {'class': 'th-class'},
            'tr': {'class': 'tr-class'},
            'td': {'class': 'td-class'},
        }