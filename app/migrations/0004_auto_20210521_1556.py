# Generated by Django 2.2.4 on 2021-05-21 06:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_item_name_furigana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name_furigana',
            field=models.CharField(blank=True, default='', max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='全角フリガナで入力してください', regex='^[ァ-ヶ]+$')], verbose_name='フリガナ'),
        ),
    ]
