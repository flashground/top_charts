# Generated by Django 3.1.5 on 2021-01-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0006_auto_20210111_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='station',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
