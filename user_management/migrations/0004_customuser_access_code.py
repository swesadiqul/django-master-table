# Generated by Django 4.2.4 on 2023-09-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_alter_customuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='access_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]