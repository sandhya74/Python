# Generated by Django 2.0 on 2021-08-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210802_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='Material_Code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='materials',
            name='Material_Descriptions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='materials',
            name='Material_Location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
