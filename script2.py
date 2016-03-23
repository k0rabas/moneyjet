from core.models import Category,Transaction
from datetime import date
from monthdelta import monthdelta

def run():
    mydate = "201603"
    mylinedate = date(year=int(mydate[:4]),month=int(mydate[4:]),day=1)
    line_chart_values=[]
    for i in range(12):
        value_i = value_e = 0
        i_date = mylinedate - monthdelta(i)
        t = Transaction.objects.filter(date__year=i_date.year,
                                       date__month=i_date.month,
                                       family_id=748166,
                                       category_id__type='i')
        for entry in t:
            value_i += entry.amount/100
            print("value_i",value_i)
        t = Transaction.objects.filter(date__year=i_date.year,
                                       date__month=i_date.month,
                                       family_id=748166,
                                       category_id__type='e')
        for entry in t:
            value_e += entry.amount/100
            print("value_e",value_i)
        line_chart_values.append([i_date,value_e,value_i])
    print ("DONE")
    for i in range(len(line_chart_values)):
        print ("line_chart_values", line_chart_values[i])
        
        
        

