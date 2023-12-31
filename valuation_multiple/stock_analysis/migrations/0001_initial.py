# Generated by Django 4.2.1 on 2023-08-02 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundamentalAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('industry', models.CharField(max_length=30)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('avg_price', models.FloatField(default=0)),
                ('avg_current_ratio', models.FloatField(default=0)),
                ('avg_quick_ratio', models.FloatField(default=0)),
                ('avg_cash_ratio', models.FloatField(default=0)),
                ('avg_debt_equity', models.FloatField(default=0)),
                ('avg_inventory_turnover', models.FloatField(default=0)),
                ('avg_days_inventory', models.FloatField(default=0)),
                ('avg_assets_turnover', models.FloatField(default=0)),
                ('avg_return_on_equity', models.FloatField(default=0)),
                ('avg_net_margin', models.FloatField(default=0)),
                ('avg_price_earnings', models.FloatField(default=0)),
                ('avg_price_cash_flow', models.FloatField(default=0)),
                ('avg_price_to_sales', models.FloatField(default=0)),
                ('avg_price_to_book', models.FloatField(default=0)),
                ('best_stock_id', models.IntegerField(default=0)),
                ('best_stock_price_earnings', models.FloatField(default=0)),
                ('best_stock_price_cash_flow', models.FloatField(default=0)),
                ('best_stock_price_to_sales', models.FloatField(default=0)),
                ('best_stock_price_to_book', models.FloatField(default=0)),
                ('historical', models.FloatField(default=0)),
                ('intrinsic_by_industry', models.FloatField(default=0)),
                ('final_value', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=30)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.FloatField(default=0)),
                ('price_bid', models.FloatField(default=0)),
                ('price_ask', models.FloatField(default=0)),
                ('current_ratio', models.FloatField(default=0)),
                ('quick_ratio', models.FloatField(default=0)),
                ('cash_ratio', models.FloatField(default=0)),
                ('debt_equity', models.FloatField(default=0)),
                ('inventory_turnover', models.FloatField(default=0)),
                ('days_inventory', models.FloatField(default=0)),
                ('assets_turnover', models.FloatField(default=0)),
                ('return_on_equity', models.FloatField(default=0)),
                ('net_margin', models.FloatField(default=0)),
                ('price_earnings', models.FloatField(default=0)),
                ('price_cash_flow', models.FloatField(default=0)),
                ('price_to_sales', models.FloatField(default=0)),
                ('price_to_book', models.FloatField(default=0)),
                ('price_earnings_five_years', models.FloatField(default=0)),
                ('price_to_sales_five_years', models.FloatField(default=0)),
                ('price_to_book_five_years', models.FloatField(default=0)),
                ('real_price_earnings', models.FloatField(default=0)),
                ('real_price_to_sales', models.FloatField(default=0)),
                ('real_price_to_book', models.FloatField(default=0)),
                ('fundamental_analyses', models.ManyToManyField(to='stock_analysis.fundamentalanalysis')),
            ],
        ),
    ]
