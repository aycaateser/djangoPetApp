from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label="email",max_length=100)
    name_surname = forms.CharField(label="Name Surname",max_length=25)
    message = forms.CharField(widget=forms.Textarea)

