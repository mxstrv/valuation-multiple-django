from typing import List
from stock_analysis.error_handlers.stock_error_handler import not_found_tickers
from stock_analysis.models.fundamental_analysis_model import FundamentalAnalysis


def get_fundamental_analysis_errors(
        fundamental_analysis: FundamentalAnalysis, stocks: List[str]
) -> List[str]:
    errors = []
    if not fundamental_analysis.name:
        errors.append("Fundamental Analysis must have a name")

    return errors + not_found_tickers(stocks)
