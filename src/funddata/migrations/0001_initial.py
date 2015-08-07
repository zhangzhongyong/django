# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShowData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fund_id', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_name', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_current_price', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_growth_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_turnover', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_net_value', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_discount_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_interest_rule', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_current_interest_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_next_intereste_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_fixed_yield', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_remaining_period', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_reference_index', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_index_growth_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_to_discount_required_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_discount_yield', models.CharField(max_length=120, null=True, blank=True)),
                ('first_name', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_overrall_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_T1_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_T2_rate', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_A_share', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_A_increased_share', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_AB_ratio', models.CharField(max_length=120, null=True, blank=True)),
                ('fund_next_rate_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
