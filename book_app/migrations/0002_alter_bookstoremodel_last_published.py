# Generated by Django 4.2.3 on 2023-08-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstoremodel',
            name='last_published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
