# Generated by Django 4.2.4 on 2023-09-14 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity_manager', '0007_delete_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity_manager.business')),
            ],
        ),
    ]
