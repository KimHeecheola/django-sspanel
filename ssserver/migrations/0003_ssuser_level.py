# Generated by Django 2.0 on 2018-01-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssserver', '0002_remove_ssuser_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssuser',
            name='level',
            field=models.PositiveIntegerField(default=0, verbose_name='用户等级'),
        ),
    ]
