from django.contrib import admin
from stock_analysis.models.stock_model import Stock
from stock_analysis.models.fundamental_analysis_model import FundamentalAnalysis

admin.site.register(FundamentalAnalysis)
admin.site.register(Stock)
