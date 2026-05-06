import pandas as pd
from .models import *

def upload_bank_csv(file_path):

    df = pd.read_csv(file_path)

    for _, row in df.iterrows():

        BankStatement.objects.create(
            date=row['date'],
            narration=row['narration'],
            amount=row['amount'],
            transaction_type=row['type']
        )


def upload_ledger_csv(file_path):

    df = pd.read_csv(file_path)

    for _, row in df.iterrows():

        InternalLedger.objects.create(
            date=row['date'],
            description=row['description'],
            amount=row['amount'],
            category=row['category']
        )