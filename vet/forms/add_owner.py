from django import forms
# from vet.models.owner import OwnerModel


class AddOwnerForm(forms.Form):
    # class Meta:
    #     model = OwnerModel
    #     fields = "__all__"
    name_surname = forms.CharField(max_length=200)
    contact_infos = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=200)
    email_field = forms.EmailField(max_length=200)
    pet = forms.CharField(max_length=200)
