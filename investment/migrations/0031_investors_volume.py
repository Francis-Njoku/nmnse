# Generated by Django 3.2.16 on 2023-01-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0030_auto_20230116_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='investors',
            name='volume',
            field=models.IntegerField(default=1),
        ),
    ]