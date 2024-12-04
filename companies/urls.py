from django.urls import path
from .views import company_detail, company_list, upload_csv

urlpatterns = [
    # Route to get details of a specific company
    path('companies/<int:company_id>/', company_detail, name='company-detail'),
    
    # Route to list all companies
    path('companies/', company_list, name='company-list'),
    
    # Route to handle CSV file upload (for updating or adding financial data)
    path('companies/upload/', upload_csv, name='company-upload'),
]