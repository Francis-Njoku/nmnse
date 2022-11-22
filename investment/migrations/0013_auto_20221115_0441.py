# Generated by Django 3.2.16 on 2022-11-15 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investment', '0012_auto_20221105_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=200),
        ),
        migrations.AlterField(
            model_name='investors',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=200),
        ),
        migrations.CreateModel(
            name='Mfa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mfa', models.CharField(max_length=255)),
                ('is_open', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mfa_key', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]