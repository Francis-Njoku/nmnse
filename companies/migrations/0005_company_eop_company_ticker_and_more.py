# Generated by Django 5.0.4 on 2024-12-25 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_company_year_of_incorporation'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='eop',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='ticker',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='financialdata',
            name='cash_equivalent',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='financialdata',
            name='equity',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='financialdata',
            name='pat',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='financialdata',
            name='pbt',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='financialdata',
            name='revenue',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='financialdata',
            name='total_assets',
            field=models.JSONField(null=True),
        ),
    ]
