import csv
from io import StringIO
import pandas as pd
import chardet
from decimal import Decimal
from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Company, FinancialData
from .serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CompanyPagination(PageNumberPagination):
    page_size = 10  # You can also override this in your settings for global control
    page_size_query_param = 'page_size'  # Allows clients to specify page size in the query string
    max_page_size = 100  # Limit the maximum page size



@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def upload_csv(request):
    # Ensure the request has a file
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded'}, status=400)

    csv_file = request.FILES['file']

    # Read the file content with proper encoding handling
    try:
        # Try decoding with 'utf-8', fallback to 'ISO-8859-1' if needed
        try:
            csv_data = csv_file.read().decode('utf-8', errors='replace')  # or 'ignore'
        except UnicodeDecodeError:
            # In case 'utf-8' fails, try 'ISO-8859-1'
            csv_data = csv_file.read().decode('ISO-8859-1')

        # Read the CSV file
        csv_reader = csv.DictReader(StringIO(csv_data))

        # Iterate through each row in the CSV
        for row in csv_reader:
            # Extract basic company data
            company_name = row['Company']
            sectors = row['Sectors']
            ticker = row['ticker']
            sub_sector = row.get('Sub-sector', '')
            year_of_incorporation_str = row.get('Year of incorporation', '').strip()

            # Handle EOP (End of Period) value and check if it is valid
            eop_str = row.get('EOP', '').strip()
            eop = None  # Default to None (null) if invalid or empty

            if eop_str:
                try:
                    # Try to parse the date, assuming it's in a format like "YYYY-MM-DD"
                    eop = datetime.strptime(eop_str, '%Y-%m-%d').date()
                except ValueError:
                    # If parsing fails, log the error and set eop to None
                    print(f"Invalid date format for EOP: {eop_str}")
                    eop = None  # Set invalid date as None, which will be NULL in the DB

            # Validate Year of Incorporation (just like the original code)
            year_of_incorporation = 0
            if year_of_incorporation_str.isdigit():
                year_of_incorporation = int(year_of_incorporation_str)

            remark = row.get('remark', '')

            # Create or update the company record
            company, created = Company.objects.get_or_create(
                name=company_name,
                year_of_incorporation=year_of_incorporation,
                defaults={'sector': sectors, 'sub_sector': sub_sector, 'remark': remark, 'ticker': ticker, 'eop': eop}
            )

            # Prepare financial data for the company (dynamic fields)
            financial_data = {
                'revenue': {},
                'pbt': {},
                'pat': {},
                'total_assets': {},
                'cash_equivalent': {},
                'equity': {},
                'fiscal_year_end': {}
            }

            # Process the year columns dynamically (handle the "revenue" columns)
            year_columns = []
            for field in csv_reader.fieldnames:
                if '"' in field:
                    year = field.split()[-1]
                    if year.isdigit() and year not in year_columns:
                        year_columns.append(year)

            for year in year_columns:
                for field in financial_data.keys():
                    field_name = f'"{field}" {year}'  # Handling columns like "revenue 2023"
                    field_value = row.get(field_name, '').replace(',', '').strip()  # Remove commas and spaces
                    print(f"Extracted value for {field_name}: '{field_value}'")  # Debugging print

                    try:
                        # If the value exists, convert it to a Decimal (to handle decimals and negative values)
                        if field_value:
                            # Convert to Decimal to handle large and decimal numbers
                            financial_data[field][year] = Decimal(field_value)
                        else:
                            financial_data[field][year] = None  # Set to None if no value
                    except Exception as e:
                        # If conversion fails, set value to None
                        financial_data[field][year] = None
                        print(f"Error converting '{field_value}' to Decimal for {field_name}: {str(e)}")

            # Convert Decimal to float for JSON serialization
            for field in financial_data:
                for year in financial_data[field]:
                    if isinstance(financial_data[field][year], Decimal):
                        financial_data[field][year] = float(financial_data[field][year])
            
            # Save financial data to the database
            FinancialData.objects.create(
                company=company,
                revenue=financial_data['revenue'],
                pbt=financial_data['pbt'],
                pat=financial_data['pat'],
                total_assets=financial_data['total_assets'],
                cash_equivalent=financial_data['cash_equivalent'],
                equity=financial_data['equity'],
                fiscal_year_end=financial_data['fiscal_year_end']
            )

        return JsonResponse({'message': 'File uploaded and data saved successfully'}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




@api_view(['GET'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=404)
    
@api_view(['GET'])
def company_list(request):
    companies = Company.objects.all()
    
    # Apply pagination
    paginator = CompanyPagination()
    result_page = paginator.paginate_queryset(companies, request)
    
    # Serialize the paginated data
    serializer = CompanySerializer(result_page, many=True)
    
    # Return the paginated response
    return paginator.get_paginated_response(serializer.data)  