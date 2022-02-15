from django.urls import path

from .views import *

urlpatterns = [
    path('', homeview, name='home'),
    path('about/', aboutview, name='about'),
    path('news/', newsview, name='news'),
    path('<int:pk>/', detailview, name='detail'),
    path('xodimlar/', hodim_view, name='xodim'),
    path('price/', price_about, name='price'),
]
