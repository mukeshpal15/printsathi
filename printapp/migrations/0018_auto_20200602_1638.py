# Generated by Django 2.1.1 on 2020-06-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0017_auto_20200602_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdata',
            name='Detail_File',
            field=models.FileField(upload_to='orderdetailfile/'),
        ),
        migrations.AlterModelTable(
            name='userdata',
            table='UserData',
        ),
    ]
