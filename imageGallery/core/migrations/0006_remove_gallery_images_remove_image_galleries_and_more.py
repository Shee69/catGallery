# Generated by Django 4.2.2 on 2023-07-05 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_image_galleries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='images',
        ),
        migrations.RemoveField(
            model_name='image',
            name='galleries',
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.image'),
        ),
    ]
