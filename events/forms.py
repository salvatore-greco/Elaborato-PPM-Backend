from django.forms import ModelForm

from events.models import Events


class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = False

    class Meta:
        model = Events
        fields = ['name', 'place_name', 'place_address', 'price', 'date']