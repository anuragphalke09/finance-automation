from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.db.models import Sum

@api_view(['GET'])
def summary(request):

    total_credits = BankStatement.objects.filter(
        transaction_type='credit'
    ).aggregate(Sum('amount'))

    total_debits = BankStatement.objects.filter(
        transaction_type='debit'
    ).aggregate(Sum('amount'))

    unmatched = Reconciliation.objects.filter(
        status='Unmatched'
    ).count()

    return Response({
        "total_credits": total_credits,
        "total_debits": total_debits,
        "unmatched": unmatched
    })

@api_view(['GET'])
def reconciliation_view(request):

    data = Reconciliation.objects.values()

    return Response(data)

@api_view(['GET'])
def category_breakdown(request):

    data = InternalLedger.objects.values(
        'category'
    ).annotate(total=Sum('amount'))

    return Response(data)

@api_view(['GET'])
def daily_cashflow(request):

    data = BankStatement.objects.values(
        'date'
    ).annotate(total=Sum('amount'))

    return Response(data)