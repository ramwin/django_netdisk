# Generated by Django 3.0 on 2020-01-12 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_netdisk', '0004_auto_20191231_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_netdisk.File')),
            ],
            options={
                'verbose_name': 'Excel文件',
                'verbose_name_plural': 'Excel文件',
            },
            bases=('django_netdisk.file',),
        ),
    ]
