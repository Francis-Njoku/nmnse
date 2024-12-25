from rest_framework import serializers
from .models import Company, FinancialData

class FinancialDataSerializer(serializers.ModelSerializer):
    revenue = serializers.JSONField()
    pbt = serializers.JSONField()
    pat = serializers.JSONField()
    total_assets = serializers.JSONField()
    cash_equivalent = serializers.JSONField()
    equity = serializers.JSONField()
    fiscal_year_end = serializers.JSONField()

    class Meta:
        model = FinancialData
        fields = ['company', 'revenue', 'pbt', 'pat', 'total_assets', 'cash_equivalent', 'equity', 'fiscal_year_end']


class CompanySerializer(serializers.ModelSerializer):
    financial_data = FinancialDataSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'ticker', 'eop', 'sector', 'sub_sector', 'year_of_incorporation', 'remark', 'financial_data']


