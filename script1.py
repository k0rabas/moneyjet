from core.models import Transaction
# from decimal import Decimal
from datetime import date,timedelta

# from django.shortcuts import get_object_or_404
# obj = get_object_or_404(MyModel, id=1)

def run():
    transactions = Transaction.objects.all()
    for t in transactions:
        if t.date == date.today():
            t.date = date.today() - timedelta(days=20)
        t.amount_dec=t.amount/100
        t.save()
    print('Done')
ver = '1.0'