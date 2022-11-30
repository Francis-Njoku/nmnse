# Generated by Django 3.2.16 on 2022-11-26 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investment', '0019_investors_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investors',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='investors',
            name='closed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='closed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]