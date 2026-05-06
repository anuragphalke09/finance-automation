from rapidfuzz import fuzz
from datetime import timedelta
from .models import *

def reconcile_transactions():

    bank_entries = BankStatement.objects.all()
    ledger_entries = InternalLedger.objects.all()

    for bank in bank_entries:

        matched = False

        for ledger in ledger_entries:

            amount_match = bank.amount == ledger.amount

            date_difference = abs((bank.date - ledger.date).days)

            similarity = fuzz.ratio(
                bank.narration.lower(),
                ledger.description.lower()
            )

            if amount_match and date_difference <= 2 and similarity > 60:

                Reconciliation.objects.create(
                    bank_transaction=bank,
                    ledger_transaction=ledger,
                    status='Matched'
                )

                matched = True
                break

        if not matched:

            Reconciliation.objects.create(
                bank_transaction=bank,
                status='Unmatched'
            )