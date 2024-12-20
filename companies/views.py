import csv
from io import StringIO
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Company, FinancialData
from .serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])  # Only admins can upload and update
def upload_csv(request):
    # Ensure the request has a file
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded'}, status=400)

    csv_file = request.FILES['file']
    
    # Read the CSV file content
    try:
        csv_data = csv_file.read().decode('utf-8')
        csv_reader = csv.DictReader(StringIO(csv_data))

        # Extract years dynamically from the headers
        year_columns = []
        for field in csv_reader.fieldnames:
            # Extract the year part (e.g., "revenue 2023", "pbt 2023")
            if '"' in field:
                year = field.split()[-1]  # Get the year from "revenue 2023"
                if year.isdigit() and year not in year_columns:
                    year_columns.append(year)

        # Iterate through each row in the CSV
        for row in csv_reader:
            # Extract basic company data
            company_name = row['Company']
            sectors = row['Sectors']
            sub_sector = row.get('Sub-sector', '')
            year_of_incorporation_str = row.get('Year of incorporation', '').strip()

            # Validate 'Year of incorporation' to ensure it's an integer
            if year_of_incorporation_str.isdigit():
                year_of_incorporation = int(year_of_incorporation_str)
            else:
                year_of_incorporation = 0  # Set to a default year or handle this case as needed

            remark = row.get('remark', '')

            # Create or update the company
            company, created = Company.objects.get_or_create(
                name=company_name,
                year_of_incorporation=year_of_incorporation,
                defaults={'sector': sectors, 'sub_sector': sub_sector, 'remark': remark}
            )

            # Prepare a dynamic dictionary for the financial data
            financial_data = {
                'revenue': {},
                'pbt': {},
                'pat': {},
                'total_assets': {},
                'cash_equivalent': {},
                'equity': {},
                'fiscal_year_end': {}
            }

            # Loop through each year and build financial data
            for year in year_columns:
                # Validate financial data fields
                for field in ['revenue', 'pbt', 'pat', 'total_assets', 'cash_equivalent', 'equity', 'fiscal_year_end']:
                    field_value = row.get(f'"{field}" {year}', '').strip()  # Ensure it's not empty
                    if field_value.isdigit():
                        financial_data[field][year] = int(field_value)
                    else:
                        financial_data[field][year] = None  # Or default value like 0, depending on requirements

            # Save financial data related to the company
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
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)    