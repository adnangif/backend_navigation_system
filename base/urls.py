from django.urls import path
from . import views

urlpatterns = [
    # path('',view=views.get_instruction, name='get'),
    path('eval/',views.evaluate_qr,name='evaluate'),
    path('',views.upload_image ,name='upload'),
]
