# Generated by Django 4.0.3 on 2022-03-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
