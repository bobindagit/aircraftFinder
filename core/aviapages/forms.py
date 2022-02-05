from django import forms


class AircraftFinder(forms.Form):
    find_string = forms.CharField(label='', min_length=2, max_length=200)
    types = (
        ('serial', 'SERIAL'),
        ('tail', 'TAIL NUMBER'),
    )
    find_type = forms.ChoiceField(choices=types)


class AircraftInfo(forms.Form):
    aircraft_name = forms.CharField(label='Aircraft name')
