# Generated by Django 2.0 on 2021-07-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('Material_Code', models.CharField(blank=True, max_length=255, null=True)),
                ('Material_Descriptions', models.CharField(blank=True, max_length=255, null=True)),
                ('Material_Location', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit_of_Measurement', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('Maximum_Level', models.IntegerField(blank=True, default=0, null=True)),
                ('Minimum_Level', models.IntegerField(blank=True, default=0, null=True)),
                ('Re_order_Level', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
