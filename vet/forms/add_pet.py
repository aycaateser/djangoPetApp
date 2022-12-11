from django import forms
from vet.models.pet import PetModel


class AddPetModelForm(forms.ModelForm):
    class Meta:
        model = PetModel
        # exclude = ('owner', 'slug')
        fields = "__all__"
