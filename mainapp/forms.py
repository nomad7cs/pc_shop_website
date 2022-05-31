from django import forms
from mainapp.models import ComputerPart

class PcItemForm(ModelForm):
    # pc_item_name = forms.CharField(max_length=100)
    # description = forms.CharField(max_length=100)
    # price = forms.FloatField()
    # manufaturer = forms.forms.ModelChoiceField(queryset=User.objects.all())
    # model_name = forms.CharField(max_length=100)
    class Meta:
        model = ComputerPart
        fields = ['name', 'description', 'price', 'manufacturer', 'model_name',]
