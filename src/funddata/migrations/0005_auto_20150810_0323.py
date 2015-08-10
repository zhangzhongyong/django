# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funddata', '0004_auto_20150810_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showdata',
            name='first_name',
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_AB_ratio',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_A_increased_share',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_A_share',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_T1_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_T2_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_current_interest_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_current_price',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_discount_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_discount_yield',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_fixed_yield',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_growth_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_index_growth_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_interest_rule',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_net_value',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_next_intereste_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_overrall_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_reference_index',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_remaining_period',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_to_discount_required_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='fund_turnover',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
