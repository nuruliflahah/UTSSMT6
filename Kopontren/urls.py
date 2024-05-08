from django.urls import path
from . import views

urlpatterns = [
    path("kasir/", views.KasirListCreate.as_view(), name="Kasir-view-create")

]