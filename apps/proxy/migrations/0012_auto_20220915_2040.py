# Generated by Django 3.2.15 on 2022-09-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proxy", "0011_auto_20220828_1040"),
    ]

    operations = [
        migrations.AddField(
            model_name="proxynode",
            name="ehco_log_level",
            field=models.CharField(
                choices=[
                    ("debug", "debug"),
                    ("info", "info"),
                    ("warn", "warn"),
                    ("error", "error"),
                ],
                default="info",
                max_length=64,
                verbose_name="隧道日志等级",
            ),
        ),
        migrations.AddField(
            model_name="proxynode",
            name="xray_grpc_port",
            field=models.IntegerField(default=23456, verbose_name="xray grpc port"),
        ),
        migrations.AlterField(
            model_name="proxynode",
            name="ehco_listen_type",
            field=models.CharField(
                choices=[
                    ("raw", "raw"),
                    ("wss", "wss"),
                    ("mwss", "mwss"),
                    ("mtcp", "mtcp"),
                ],
                default="raw",
                max_length=64,
                verbose_name="隧道监听类型",
            ),
        ),
        migrations.AlterField(
            model_name="proxynode",
            name="ehco_transport_type",
            field=models.CharField(
                choices=[
                    ("raw", "raw"),
                    ("wss", "wss"),
                    ("mwss", "mwss"),
                    ("mtcp", "mtcp"),
                ],
                default="raw",
                max_length=64,
                verbose_name="隧道传输类型",
            ),
        ),
        migrations.AlterField(
            model_name="relayrule",
            name="listen_type",
            field=models.CharField(
                choices=[
                    ("raw", "raw"),
                    ("wss", "wss"),
                    ("mwss", "mwss"),
                    ("mtcp", "mtcp"),
                ],
                default="raw",
                max_length=64,
                verbose_name="监听类型",
            ),
        ),
        migrations.AlterField(
            model_name="relayrule",
            name="transport_type",
            field=models.CharField(
                choices=[
                    ("raw", "raw"),
                    ("wss", "wss"),
                    ("mwss", "mwss"),
                    ("mtcp", "mtcp"),
                ],
                default="raw",
                max_length=64,
                verbose_name="传输类型",
            ),
        ),
    ]
