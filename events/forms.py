from django.forms import ModelForm
from django import forms

from events.models import Events
from django.db import models




class EventForm(ModelForm):
    date = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
            time_format="%H:%M"
        )
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False

    class Meta:
        model = Events
        fields = ['name', 'place_name', 'place_address', 'price', 'date']
        widgets = {
            'date': forms.SplitDateTimeWidget(
                date_attrs={'type': 'date'},
                time_attrs={'type': 'time'},
                time_format="%H:%M"
            )
        }
