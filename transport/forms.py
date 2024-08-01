from django import forms

from .models import Datatransport


class transportForm(forms.Form):
    category = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Category',
            }
        )
    )
    station = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Station Name',
            }
        )
    )
    latitude = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Latitude',
            }
        )
    )
    longitude = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Longitude',
            }
        )
    )
    altitude = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Altitude',
            }
        )
    )
    trayek = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Routes',
            }
        )
    )
    status = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Status',
            }
        )
    )
    stationtransit = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Is this transit station?',
            }
        )
    )