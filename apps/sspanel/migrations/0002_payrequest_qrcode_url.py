# Generated by Django 2.0.5 on 2018-07-07 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="payrequest",
            name="qrcode_url",
            field=models.CharField(max_length=64, null=True, verbose_name="支付连接"),
        )
    ]
