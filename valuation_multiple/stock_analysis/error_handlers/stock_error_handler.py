from typing import List
from stock_analysis.models.fundamental_analysis_model import FundamentalAnalysis
from stock_analysis.models.stock_model import Stock


def not_found_tickers(stocks: List[str]) -> List[str]:
    errors = []

    for stock in stocks:
        if type(stock) != Stock:
            errors.append(f"The ticker {stock} could not be found")

    return errors


def get_stock_errors(
        fundamental_analysis: FundamentalAnalysis, stocks: List[str]
) -> List[str]:
    errors = not_found_tickers(stocks)

    for stock in stocks:
        if stock in fundamental_analysis.stock_set.all():
            errors.append(f"{stock} is already in fundamental analysis")

    return errors


def get_single_stock_errors(stock: Stock) -> List[str]:
    errors = []

    existing_stock = Stock.objects.filter(ticker=stock.ticker)

    if existing_stock:
        errors.append(f"There is already a stock with the ticker {stock.ticker}")

    if not stock.name:
        errors.append("Stock has no name")

    if not stock.ticker:
        errors.append("Stock has no ticker")

    if not stock.price:
        errors.append("Stock has no price")

    if not stock.price_earnings:
        errors.append("Price Earnings must have a value")

    if not stock.price_to_sales:
        errors.append("Price to Sales must have a value")

    if not stock.price_to_book:
        errors.append("Price to Book must have a value")

    return errors
