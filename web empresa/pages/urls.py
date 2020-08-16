from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:page_id>/<slug:title_slug>/', views.page, name="page"),
]