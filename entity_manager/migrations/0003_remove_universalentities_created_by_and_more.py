# Generated by Django 4.2.4 on 2023-09-14 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity_manager', '0002_type_universalentities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universalentities',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='universalentities',
            name='xbusiness',
        ),
        migrations.RemoveField(
            model_name='universalentities',
            name='xtype',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.DeleteModel(
            name='UniversalEntities',
        ),
    ]
