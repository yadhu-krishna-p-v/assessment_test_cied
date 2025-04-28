from django.urls import path
from apps.medicines.views import MedicineListView, MedicineCrudAPIView

urlpatterns = [
    path('medicines/', MedicineListView.as_view(), name='medicine_list_api'),
    path('medicines/<int:pk>/', MedicineCrudAPIView.as_view(), name='medicine_crud_api'),
]