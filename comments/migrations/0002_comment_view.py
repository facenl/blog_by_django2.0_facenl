# Generated by Django 4.0.3 on 2022-03-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='view',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
