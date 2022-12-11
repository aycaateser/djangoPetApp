from datetime import timezone

from django.db import models


class PetModel(models.Model):
    picture = models.ImageField(upload_to="animal_picture", null=True)
    pet_type = models.CharField(max_length=30, null=False)
    pet_genus = models.CharField(max_length=30, null=False)
    pet_name = models.CharField(max_length=30, null=False)
    pet_age = models.IntegerField(blank=True, null=False)
    explanation = models.CharField(max_length=30, null=False)

    # created_date = models.DateTimeField(auto_now_add=True, verbose_name="olusturulma tarihi")



    def __str__(self):
        return self.pet_type