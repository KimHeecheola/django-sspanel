# Generated by Django 3.1.1 on 2020-11-12 00:13

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField(db_index=True, default=1, help_text='处于序列中的第几位')),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('node_type', models.CharField(choices=[('ss', 'ss'), ('vless', 'vless'), ('trojan', 'trojan')], default='ss', max_length=32, verbose_name='节点类型')),
                ('server', models.CharField(help_text='支持逗号分隔传多个地址', max_length=256, verbose_name='服务器地址')),
                ('info', models.CharField(blank=True, max_length=1024, verbose_name='节点说明')),
                ('level', models.PositiveIntegerField(default=0)),
                ('country', models.CharField(choices=[('US', '美国'), ('CN', '中国'), ('GB', '英国'), ('SG', '新加坡'), ('TW', '台湾'), ('HK', '香港'), ('JP', '日本'), ('FR', '法国'), ('DE', '德国'), ('KR', '韩国'), ('JE', '泽西岛'), ('NZ', '新西兰'), ('MX', '墨西哥'), ('CA', '加拿大'), ('BR', '巴西'), ('CU', '古巴'), ('CZ', '捷克'), ('EG', '埃及'), ('FI', '芬兰'), ('GR', '希腊'), ('GU', '关岛'), ('IS', '冰岛'), ('MO', '澳门'), ('NL', '荷兰'), ('NO', '挪威'), ('PL', '波兰'), ('IT', '意大利'), ('IE', '爱尔兰'), ('AR', '阿根廷'), ('PT', '葡萄牙'), ('AU', '澳大利亚'), ('RU', '俄罗斯联邦'), ('CF', '中非共和国')], default='CN', max_length=5, verbose_name='国家')),
                ('used_traffic', models.BigIntegerField(default=0, verbose_name='已用流量')),
                ('total_traffic', models.BigIntegerField(default=1073741824, verbose_name='总流量')),
                ('enable', models.BooleanField(db_index=True, default=True, verbose_name='是否开启')),
                ('enlarge_scale', models.DecimalField(decimal_places=2, default=Decimal('1.0'), max_digits=10, verbose_name='倍率')),
            ],
            options={
                'verbose_name_plural': '代理节点',
                'ordering': ('sequence',),
            },
        ),
        migrations.CreateModel(
            name='SSConfig',
            fields=[
                ('node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ss_config', serialize=False, to='proxy.proxynode')),
                ('method', models.CharField(choices=[('chacha20-ietf-poly1305', 'chacha20-ietf-poly1305'), ('aes-128-gcm', 'aes-128-gcm'), ('aes-256-gcm', 'aes-256-gcm')], default='aes-256-cfb', max_length=32, verbose_name='加密类型')),
                ('multi_user_port', models.IntegerField(blank=True, help_text='单端口多用户端口', null=True, verbose_name='多用户端口')),
            ],
            options={
                'verbose_name_plural': 'SS节点配置',
            },
        ),
    ]
