from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car
from .serializers import CarSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponseRedirect

# API VIEWS
class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

class CarDetailAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarSerializer

class UserCreateView(View):
    form_class = UserCreationForm
    template_name = "garage/user_create.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('car_list'))
        else:
            return render(request, self.template_name, {"form":form})

class ProfileView(View):
    def get(self, request):
        print(request.user)
        return render(request, 'garage/profile_view.html', {'profile':request.user})
# HTML VIEWS

class CarListView(ListView):
    model = Car

class CarDetailView(DetailView):
    model = Car

class CarCreateView(CreateView):
    model = Car
    fields = ['model', 'make', 'engine', 'interior_color','body_color', 'year', 'image', 'speed']
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    fields = ['model', 'make', 'engine', 'interior_color', 'body_color', 'year', 'image', 'speed']
    template_name_suffix = "_update_form"

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')

# class FilterCarsColorView(ListView):
#     model = Car
#     template_name = "garage/carbycolor.html"

#     def get_queryset(self):
#         print("----", self.request.GET.get("color"))
#         car_color = self.request.GET.get("color").capitalize()
#         if car_color in ["White","Black","Red","Orange"]:
#             queryset = Car.objects.filter(color=car_color)
#             print(queryset)
#             return queryset

class FilterCarMakeView(ListView):
    model = Car
    template_name = "garage/carbymake.html"

    def get_queryset(self):
        car_make = self.request.GET.get("make").capitalize()
        if car_make in ["Honda", "Bugatti", "Subaru", "Porsche"]:
            queryset = Car.objects.filter(make=car_make)
            print (queryset)
            return queryset