# Generated by Django 4.2.4 on 2023-09-14 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity_manager', '0005_delete_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
