from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.sites import requests
from django.core.cache.backends import redis
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from vet.forms.add_owner import AddOwnerForm
from vet.models.pet import PetModel
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from vet.forms.contact import ContactForm
from vet.forms.add_pet import AddPetModelForm
from vet.models.contact import ContactModel
from vet.models.user import UserModel
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout


def home(request):
    for_search = request.GET.get("for_search")
    print("for_Search", for_search)
    pets = PetModel.objects.all()
    if for_search:
        pets = pets.filter(
            Q(pet_name__icontains=for_search) | Q(pet_genus__icontains=for_search)
        ).distinct()
    sorgu = request.GET.get('sorgu')
    print(sorgu, "sorguuuuu")
    paginator = Paginator(pets, 3)
    print(pets)
    return render(request, 'homepage.html', context={
        "pets": paginator.get_page(sorgu)
    })


def detail(request, slug):
    pet = get_object_or_404(PetModel, slug=slug)
    types = pet.pet_type.all()
    return render(request, "detail.html", context={
        'pet': pet,
        'types': types
    })


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = ContactModel()
            contact.email = form.cleaned_data["email"]
            contact.name_surname = form.cleaned_data["name_surname"]
            contact.message = form.cleaned_data["message"]
            contact.save()
            return redirect(home)
    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)


def register(request):
    if request.method == "POST":
        print(request.POST)
        user_email = request.POST.get('user_email')
        password = request.POST.get('password')
        name_surname = request.POST.get('name_surname')
        phone_number = request.POST.get('phone_number')
        request.session["user_email"] = user_email
        new_user = UserModel(user_email=user_email, password=password, name_surname=name_surname,
                             phone_number=phone_number)
        new_user.password = make_password(new_user.password)
        new_user.save()
        return redirect("login")
    return render(request, "registerpage.html")


def addpet(request):
    if request.method == "POST":
        print(request.POST.__dict__)
        upload = request.FILES['picture']
        user_id = request.session.get("user_id")
        user = UserModel.objects.filter(id=user_id).first()
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        picture = fss.url(file)
        pet_type = request.POST.get('pet_type')
        pet_genus = request.POST.get('pet_genus')
        pet_name = request.POST.get('pet_name')
        pet_age = request.POST.get('pet_age')
        explanation = request.POST.get('explanation')
        print(explanation)
        new_pet = PetModel(picture=picture, pet_type=pet_type, pet_genus=pet_genus, pet_name=pet_name, pet_age=pet_age,
                           explanation=explanation)
        new_pet.save()
        user.pet = new_pet
        user.save()
        return redirect("")
    return render(request, "add_pet.html")


def editprofile(request):
    if request.method == "POST":
        print("dıjsaıd")
        user_id = request.session.get("user_id")
        user_email = request.session.get("user_email")
        name_surname = request.POST.get('name_surname')
        phone_number = request.POST.get('phone_number')
        user = UserModel.objects.filter(id=user_id).first()
        if user:
            user.user_email = user_email
            user.name_surname = name_surname
            user.phone_number = phone_number
            user.save()
            return redirect("")
    return render(request, "edit_user.html")


def change_password(request):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        user = UserModel.objects.filter(id=user_id).first()
        if user and check_password(password,
                                   user.password):
            if password == new_password:
                messages.warning(request, "aynı sifre")
            else:
                user.password = make_password(new_password)
                user.save()
                print("sifre basarıyla degisti")
                messages.success(request, "sifre basarıyla degistirildi")
                print("sifre basarıyla degisti")

        else:
            messages.warning(request, "sifre yanlıs")
    return render(request, "change_password.html")


# def login(request):
#
#     import ipdb
#     ipdb.set_trace()
#     if request.method == 'POST':
#         user = UserModel.objects.filter(username=request.post.get('username')).first()
#         if user:
#             if user.password == request.post.password:
#                 key = uuid.uuid4()
#                 value = user.id
#                 redis.set(key, value, timeout=1000000)
#                 redirect()
#             else:
#                 return render()
#         else:
#             return render()
#
#     return render(request, 'loginpage.html')


def login_request(request):
    if request.method == "POST":
        user_email = request.POST["user_email"]
        password = request.POST["password"]
        user = UserModel.objects.filter(user_email=user_email).first()
        if user is not None:
            if check_password(password, user.password):
                messages.success(request, "Login is Successful")
                request.session["user_id"] = user.id
                print(request.session.__dict__)
                return redirect("")
            else:
                messages.info(request, "deneme kullanıcı adı veya parola yanlısss")
                return render(request, "loginpage.html", {
                    "error": "username or password is wrong"
                })
        else:
            messages.info(request, "kullanıcı bulunamadı")
            return render(request, "loginpage.html", {
                "error": "username not found"
            })
    return render(request, "loginpage.html", context={})


def logout_request(request):
    print(request.session["user_id"])
    try:
        del request.session["user_id"]
    except KeyError:
        pass
    return redirect("/login")
