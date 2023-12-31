import os

from django.db import models
from .fundamental_analysis_model import FundamentalAnalysis
from stock_analysis.classes.stock_valuation import StockValuation
from django.utils import timezone
from django.core.handlers.wsgi import WSGIRequest
from urllib.request import urlopen
import json
import certifi
import yfinance as yf
from statistics import mean
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')


class Stock(models.Model):
    fundamental_analyses = models.ManyToManyField(FundamentalAnalysis)

    # Stock basic info
    ticker = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    last_update = models.DateTimeField(default=timezone.now)

    # Price
    price = models.FloatField(default=0)
    price_bid = models.FloatField(default=0)
    price_ask = models.FloatField(default=0)

    # Ratios
    current_ratio = models.FloatField(default=0)
    quick_ratio = models.FloatField(default=0)
    cash_ratio = models.FloatField(default=0)
    debt_equity = models.FloatField(default=0)
    inventory_turnover = models.FloatField(default=0)
    days_inventory = models.FloatField(default=0)
    assets_turnover = models.FloatField(default=0)
    return_on_equity = models.FloatField(default=0)
    net_margin = models.FloatField(default=0)
    price_earnings = models.FloatField(default=0)
    price_cash_flow = models.FloatField(default=0)
    price_to_sales = models.FloatField(default=0)
    price_to_book = models.FloatField(default=0)

    # Five year ratios
    price_earnings_five_years = models.FloatField(default=0)
    price_to_sales_five_years = models.FloatField(default=0)
    price_to_book_five_years = models.FloatField(default=0)

    # TODO: Verify that this variables are correctly named
    # Real ratios values
    real_price_earnings = models.FloatField(default=0)
    real_price_to_sales = models.FloatField(default=0)
    real_price_to_book = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"{self.ticker}: {self.name}"

    def update_stock_ratios(self) -> bool:
        if not self.__yf_update_stock_ratios():
            return False

        if not self.__financialmodelingprep_update_stock_ratios():
            return False

        self.save()
        return True

    def valuate_stock(self, fundamental_analysis) -> StockValuation:
        historical = (self.real_price_to_sales + self.real_price_to_book) / 2

        per_current_value = (
                self.price * fundamental_analysis.avg_price_earnings / self.price_earnings
        )
        pcf_current_value = (
                self.price * fundamental_analysis.avg_price_cash_flow / self.price_cash_flow
        )
        ps_current_value = (
                self.price * fundamental_analysis.avg_price_to_sales / self.price_to_sales
        )
        pbv_current_value = (
                self.price * fundamental_analysis.avg_price_to_book / self.price_to_book
        )

        intrinsic_by_industry = mean(
            [per_current_value, pcf_current_value, ps_current_value, pbv_current_value]
        )

        final_value = (historical + intrinsic_by_industry) / 2

        stock_valuation = StockValuation(
            final_value=final_value,
            current_percentage=final_value / self.price,
            intrinsic_by_industry=intrinsic_by_industry,
            historical=historical,
            per_current_value=per_current_value,
            pcf_current_value=pcf_current_value,
            ps_current_value=ps_current_value,
            pbv_current_value=pbv_current_value,
        )

        print("======================", stock_valuation)

        return stock_valuation

    def calculate_real_values(self) -> None:
        self.real_price_earnings = (
                self.price * self.price_earnings_five_years / self.price_earnings
        )

        self.real_price_to_sales = (
                self.price * self.price_to_sales_five_years / self.price_to_sales
        )

        self.real_price_to_book = (
                self.price * self.price_to_book_five_years / self.price_to_book
        )

    def __set_five_year_ratios(self, ratios) -> None:
        if len(ratios) >= 5:
            ratios = ratios[:5]

        price_earnings_five_years = []
        price_to_sales_five_years = []
        price_to_book_five_years = []

        for stock in ratios:
            price_earnings_five_years.append(stock["priceEarningsRatio"])
            price_to_sales_five_years.append(stock["priceToSalesRatio"])
            price_to_book_five_years.append(stock["priceToBookRatio"])

        self.price_earnings_five_years = mean(price_earnings_five_years)
        self.price_to_sales_five_years = mean(price_to_sales_five_years)
        self.price_to_book_five_years = mean(price_to_book_five_years)

    def __financialmodelingprep_update_stock_ratios(self) -> bool:
        url = f"https://financialmodelingprep.com/api/v3/ratios/{self.ticker}?apikey={API_KEY}"
        response = urlopen(url, cafile=certifi.where())
        data = response.read().decode("utf-8")
        ratios = json.loads(data)

        if not ratios:
            return False

        latest_year = ratios[0]
        latest_year = {ratio: value or 0 for (ratio, value) in latest_year.items()}

        self.cash_ratio = latest_year["cashRatio"]
        self.inventory_turnover = latest_year["inventoryTurnover"]
        self.assets_turnover = latest_year["assetTurnover"]

        self.net_margin = latest_year["netProfitMargin"]
        self.days_inventory = latest_year["daysOfInventoryOutstanding"]

        self.price_earnings = latest_year["priceEarningsRatio"]
        self.price_cash_flow = latest_year["priceCashFlowRatio"]
        self.price_to_sales = latest_year["priceToSalesRatio"]

        self.__set_five_year_ratios(ratios)
        self.calculate_real_values()

        return True

    def __yf_update_stock_ratios(self) -> bool:
        try:
            ratios = yf.Ticker(self.ticker).info
        except:
            return False

        if not ratios:
            return False

        self.name = ratios["shortName"]
        self.price_ask = ratios["ask"]
        self.price_bid = ratios["bid"]
        self.price = (self.price_bid + self.price_ask) / 2

        self.current_ratio = ratios["currentRatio"]
        self.quick_ratio = ratios["quickRatio"]

        self.debt_equity = ratios["debtToEquity"]
        self.return_on_equity = ratios["returnOnEquity"]
        self.price_to_book = ratios["priceToBook"]

        return True

    def generate_stock(request: WSGIRequest):
        stock = Stock()
        stock.name = request.POST["name"]
        stock.ticker = request.POST["ticker"]
        stock.price = float(request.POST["price"])

        stock.current_ratio = float(request.POST["current_ratio"])
        stock.quick_ratio = float(request.POST["quick_ratio"])
        stock.cash_ratio = float(request.POST["cash_ratio"])
        stock.debt_equity = float(request.POST["debt_equity"])
        stock.inventory_turnover = float(request.POST["inventory_turnover"])
        stock.days_inventory = float(request.POST["days_inventory"])
        stock.assets_turnover = float(request.POST["assets_turnover"])
        stock.return_on_equity = float(request.POST["return_on_equity"])
        stock.net_margin = float(request.POST["net_margin"])
        stock.price_cash_flow = float(request.POST["price_cash_flow"])
        stock.price_earnings = float(request.POST["price_earnings"])
        stock.price_earnings_five_years = float(
            request.POST["price_earnings_five_years"]
        )
        stock.price_to_sales = float(request.POST["price_to_sales"])
        stock.price_to_sales_five_years = float(
            request.POST["price_to_sales_five_years"]
        )
        stock.price_to_book = float(request.POST["price_to_book"])
        stock.price_to_book_five_years = float(request.POST["price_to_book_five_years"])

        return stock
