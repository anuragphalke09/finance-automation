from django.urls import path
from .views import *

urlpatterns = [
    path('summary/', summary),
    path('reconciliation/', reconciliation_view),
    path('category-breakdown/', category_breakdown),
    path('daily-cashflow/', daily_cashflow),
]