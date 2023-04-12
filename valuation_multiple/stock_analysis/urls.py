from django.urls import path
from stock_analysis.views.stocks_view import (
    stock_detail,
    add_stock,
    new_stock,
    create_stock,
)
from stock_analysis.views.fundamental_analysis_view import (
    IndexView,
    detail,
    new_fundamental_analysis,
    create_fundamental_analysis,
    delete_stock_from_fundamental_analysis,
)


app_name = "stock_analysis"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:fundamental_analysis_id>/", detail, name="detail"),
    path("new/", new_fundamental_analysis, name="new"),
    path("create/", create_fundamental_analysis, name="create"),
    path("stock/new/", new_stock, name="new_stock"),
    path("stock/create/", create_stock, name="create_stock"),
    path("stock/<int:stock_id>/", stock_detail, name="stock_detail"),
    path("<int:fundamental_analysis_id>", add_stock, name="add_stock"),
    path(
        "<int:fundamental_analysis_id>/<int:stock_id>",
        delete_stock_from_fundamental_analysis,
        name="delete_stock_from_fundamental_analysis",
    ),
]
