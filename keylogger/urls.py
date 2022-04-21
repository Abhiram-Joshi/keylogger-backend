from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^parental_control/$", views.ParentalControl.as_view(), name="evaluate_key_presses"),
    re_path(r"^form_based_keylogger/$", views.FormBasedKeylogger.as_view(), name="form_based_keylogger"),
]