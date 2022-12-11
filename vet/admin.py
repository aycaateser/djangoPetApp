from django.contrib import admin

from django.contrib import admin
from .models.pet import PetModel
# from .models.owner import OwnerModel
from .models.contact import ContactModel
from .models.user import UserModel

admin.site.register(PetModel)
admin.site.register(ContactModel)
admin.site.register(UserModel)


class PetAdmin(admin.ModelAdmin):
    search_fields = ("pet_type", "pet_genus")
    list_display = ("pet_type", "pet_genus")


class OwnerModel(admin.ModelAdmin):
    list_display = ("name_surname", "")
    search_fields = ("")


class ContactModel(admin.ModelAdmin):
    list_display = ("name_surname", "")
    # search_fields = ("")


class UserModel(admin.ModelAdmin):
    list_display = ("username", "")
