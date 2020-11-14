# Generated by Django 3.1.1 on 2020-11-14 02:07

from decimal import Decimal

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProxyNode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sequence",
                    models.IntegerField(
                        db_index=True, default=1, help_text="处于序列中的第几位"
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="名字")),
                (
                    "server",
                    models.CharField(
                        help_text="支持逗号分隔传多个地址", max_length=256, verbose_name="服务器地址"
                    ),
                ),
                (
                    "enable",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="是否开启"
                    ),
                ),
                (
                    "node_type",
                    models.CharField(
                        choices=[
                            ("ss", "ss"),
                            ("vless", "vless"),
                            ("trojan", "trojan"),
                        ],
                        default="ss",
                        max_length=32,
                        verbose_name="节点类型",
                    ),
                ),
                (
                    "info",
                    models.CharField(blank=True, max_length=1024, verbose_name="节点说明"),
                ),
                ("level", models.PositiveIntegerField(default=0)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("US", "美国"),
                            ("CN", "中国"),
                            ("GB", "英国"),
                            ("SG", "新加坡"),
                            ("TW", "台湾"),
                            ("HK", "香港"),
                            ("JP", "日本"),
                            ("FR", "法国"),
                            ("DE", "德国"),
                            ("KR", "韩国"),
                            ("JE", "泽西岛"),
                            ("NZ", "新西兰"),
                            ("MX", "墨西哥"),
                            ("CA", "加拿大"),
                            ("BR", "巴西"),
                            ("CU", "古巴"),
                            ("CZ", "捷克"),
                            ("EG", "埃及"),
                            ("FI", "芬兰"),
                            ("GR", "希腊"),
                            ("GU", "关岛"),
                            ("IS", "冰岛"),
                            ("MO", "澳门"),
                            ("NL", "荷兰"),
                            ("NO", "挪威"),
                            ("PL", "波兰"),
                            ("IT", "意大利"),
                            ("IE", "爱尔兰"),
                            ("AR", "阿根廷"),
                            ("PT", "葡萄牙"),
                            ("AU", "澳大利亚"),
                            ("RU", "俄罗斯联邦"),
                            ("CF", "中非共和国"),
                        ],
                        default="CN",
                        max_length=5,
                        verbose_name="国家",
                    ),
                ),
                (
                    "used_traffic",
                    models.BigIntegerField(default=0, verbose_name="已用流量"),
                ),
                (
                    "total_traffic",
                    models.BigIntegerField(default=1073741824, verbose_name="总流量"),
                ),
                (
                    "enlarge_scale",
                    models.DecimalField(
                        decimal_places=1,
                        default=Decimal("1.0"),
                        max_digits=10,
                        verbose_name="倍率",
                    ),
                ),
                (
                    "ehco_listen_host",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="隧道监听地址"
                    ),
                ),
                (
                    "ehco_listen_port",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="隧道监听端口"
                    ),
                ),
                (
                    "ehco_listen_type",
                    models.CharField(
                        choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                        default="raw",
                        max_length=64,
                        verbose_name="隧道监听类型",
                    ),
                ),
                (
                    "ehco_transport_type",
                    models.CharField(
                        choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                        default="raw",
                        max_length=64,
                        verbose_name="隧道传输类型",
                    ),
                ),
            ],
            options={"verbose_name_plural": "代理节点", "ordering": ("sequence",),},
        ),
        migrations.CreateModel(
            name="RelayNode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="名字")),
                (
                    "server",
                    models.CharField(
                        help_text="支持逗号分隔传多个地址", max_length=256, verbose_name="服务器地址"
                    ),
                ),
                (
                    "enable",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="是否开启"
                    ),
                ),
                (
                    "isp",
                    models.CharField(
                        choices=[
                            ("移动", "移动"),
                            ("联通", "联通"),
                            ("电信", "电信"),
                            ("BGP", "BGP"),
                        ],
                        default="BGP",
                        max_length=64,
                        verbose_name="ISP线路",
                    ),
                ),
            ],
            options={"verbose_name_plural": "中转节点",},
        ),
        migrations.CreateModel(
            name="SSConfig",
            fields=[
                (
                    "proxy_node",
                    models.OneToOneField(
                        help_text="代理节点",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="ss_config",
                        serialize=False,
                        to="proxy.proxynode",
                        verbose_name="代理节点",
                    ),
                ),
                (
                    "method",
                    models.CharField(
                        choices=[
                            ("chacha20-ietf-poly1305", "chacha20-ietf-poly1305"),
                            ("aes-128-gcm", "aes-128-gcm"),
                            ("aes-256-gcm", "aes-256-gcm"),
                        ],
                        default="aes-256-cfb",
                        max_length=32,
                        verbose_name="加密类型",
                    ),
                ),
                (
                    "multi_user_port",
                    models.IntegerField(
                        blank=True,
                        help_text="单端口多用户端口",
                        null=True,
                        verbose_name="多用户端口",
                    ),
                ),
            ],
            options={"verbose_name_plural": "SS配置",},
        ),
        migrations.CreateModel(
            name="RelayRule",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("relay_port", models.CharField(max_length=64, verbose_name="中转端口")),
                (
                    "listen_type",
                    models.CharField(
                        choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                        default="raw",
                        max_length=64,
                        verbose_name="监听类型",
                    ),
                ),
                (
                    "transport_type",
                    models.CharField(
                        choices=[("raw", "raw"), ("wss", "wss"), ("mwss", "mwss")],
                        default="raw",
                        max_length=64,
                        verbose_name="传输类型",
                    ),
                ),
                (
                    "proxy_node",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="relay_rules",
                        to="proxy.proxynode",
                        verbose_name="代理节点",
                    ),
                ),
                (
                    "relay_node",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="relay_rules",
                        to="proxy.relaynode",
                        verbose_name="中转节点",
                    ),
                ),
            ],
            options={"verbose_name_plural": "中转规则",},
        ),
        migrations.CreateModel(
            name="UserTrafficLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        help_text="创建时间",
                        verbose_name="创建时间",
                    ),
                ),
                (
                    "upload_traffic",
                    models.BigIntegerField(default=0, verbose_name="上传流量"),
                ),
                (
                    "download_traffic",
                    models.BigIntegerField(default=0, verbose_name="下载流量"),
                ),
                (
                    "proxy_node",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="proxy.proxynode",
                        verbose_name="代理节点",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "用户流量记录",
                "ordering": ["-created_at"],
                "index_together": {("user", "proxy_node", "created_at")},
            },
        ),
        migrations.CreateModel(
            name="UserOnLineIpLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        help_text="创建时间",
                        verbose_name="创建时间",
                    ),
                ),
                ("ip", models.CharField(max_length=128, verbose_name="IP地址")),
                (
                    "proxy_node",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="proxy.proxynode",
                        verbose_name="代理节点",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "用户在线IP记录",
                "ordering": ["-created_at"],
                "index_together": {("user", "proxy_node", "created_at")},
            },
        ),
        migrations.CreateModel(
            name="NodeOnlineLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        help_text="创建时间",
                        verbose_name="创建时间",
                    ),
                ),
                (
                    "online_user_count",
                    models.IntegerField(default=0, verbose_name="用户数"),
                ),
                (
                    "tcp_connections_count",
                    models.IntegerField(default=0, verbose_name="tcp链接数"),
                ),
                (
                    "proxy_node",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="proxy.proxynode",
                        verbose_name="代理节点",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "节点在线记录",
                "ordering": ["-created_at"],
                "index_together": {("proxy_node", "created_at")},
            },
        ),
    ]
