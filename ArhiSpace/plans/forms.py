from django import forms

class EstimarePretForm(forms.Form):
    suprafata = forms.FloatField(
        label="Suprafața (m²)",
        min_value=1,
        max_value=372,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Introdu suprafața în m²"
        })
    )