from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmployeeView.as_view()),
    path('Emp/<int:pk>', views.EmployeeUpdateview.as_view()),
]