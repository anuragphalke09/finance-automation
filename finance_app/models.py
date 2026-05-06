from django.db import models

class BankStatement(models.Model):
    date = models.DateField()
    narration = models.CharField(max_length=255)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=10)

class InternalLedger(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    category = models.CharField(max_length=100)

class Reconciliation(models.Model):
    bank_transaction = models.ForeignKey(BankStatement, on_delete=models.CASCADE, null=True)
    ledger_transaction = models.ForeignKey(InternalLedger, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20)

class NormalizedLedger(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    source = models.CharField(max_length=20)
    reconciliation_status = models.CharField(max_length=20)