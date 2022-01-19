# Generated by Django 3.2 on 2021-08-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proxy", "0005_auto_20210506_1950"),
    ]

    operations = [
        migrations.AddField(
            model_name="relaynode",
            name="enable_ping",
            field=models.BooleanField(default=True, verbose_name="是否开启PING"),
        ),
        migrations.AddField(
            model_name="relaynode",
            name="enable_udp",
            field=models.BooleanField(default=True, verbose_name="是否开启UDP 转发"),
        ),
        migrations.AddField(
            model_name="relaynode",
            name="web_port",
            field=models.IntegerField(default=0, verbose_name="Web端口"),
        ),
        migrations.AddField(
            model_name="relaynode",
            name="web_token",
            field=models.CharField(
                default="", max_length=64, verbose_name="Web验证Token"
            ),
        ),
    ]