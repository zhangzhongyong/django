# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funddata', '0002_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_AB_ratio',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_A_increased_share',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_A_share',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_T1_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_T2_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_current_interest_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_current_price',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_discount_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_discount_yield',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_fixed_yield',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_growth_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_index_growth_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_interest_rule',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_name',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_net_value',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_next_intereste_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_next_rate_date',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_overrall_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_reference_index',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_remaining_period',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_to_discount_required_rate',
        ),
        migrations.RemoveField(
            model_name='showdata',
            name='fund_turnover',
        ),
    ]
