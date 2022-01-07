from django.forms import ModelForm,TextInput
from .models import QrcodeLink


class LinkForm(ModelForm):
    class Meta:
        model=QrcodeLink
        fields=['link']
        widget={'link':TextInput(attrs={'class':'input','placeholder':'Enter Link here'})}
