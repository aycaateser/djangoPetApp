from django.db import models

from vet.models.pet import PetModel


class UserModel(models.Model):
    user_email = models.EmailField(max_length=30, null=False)
    password = models.CharField(max_length=100, null=False)
    name_surname = models.CharField(max_length=30, null=False)
    phone_number = models.CharField(max_length=30, null=False,default='some_value')
    pet = models.ForeignKey(PetModel, related_name="owner", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username
