from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models import Category,Transaction,Family, UserProfile
from django.contrib.auth import get_user_model
from core.forms import TransactionForm, DateForm, ProfileForm
from django import forms        # for HiddenInput widget use
from datetime import date
from monthdelta import monthdelta


def transactions_exp(request):
    c = Category.objects.expense()    # this is context
    return render(request, 'core/transactions_exp.html',
                  {'categories': c,
                   'navbar':'transact',   # 'navbar' is for active state triggering
                   })

def transactions_inc(request):
    c = Category.objects.income()    # this is context
    return render(request, 'core/transactions_inc.html',
                  {'categories': c,         # for navbar active state triggering
                   'navbar':'transact'})
                                    
    
def dashboard(request):
    if not request.user.is_authenticated():
        return render(request, 'core/login_needed.html', 
              {'navbar':'settings'})   # for navbar active state triggering
    this_month_date = str(date.today().year) + str(date.today().month).zfill(2)
    #debug_datetime_now = datetime.now().strftime('%Y.%m.%d %H:%M:%S')  #  Time like '2016.04.08 15:08:34'
    
    if 'mydate' in request.session:
        mydate = request.session['mydate']
    else:
        mydate = this_month_date

    form = DateForm(request.POST or None, auto_id=False, initial={'selector_mydate': mydate}, )
    if form.is_valid():
        mydate = request.session['mydate'] = form.cleaned_data['selector_mydate']
#         request.session['mydate'] = form.cleaned_data['mydate'].strftime('%Y%m')
#         mydate = form.cleaned_data['mydate'].strftime('%Y%m')
        return HttpResponseRedirect('/dashboard/')    

    t = Transaction.objects.filter(date__year=mydate[:4],
                                   date__month=mydate[4:],
                                   family_id=request.user.userprofile.family_id)
    cat_e = Category.objects.expense()
    cat_i = Category.objects.income()
    dict_e = {}                  # create dict of Exp categories and calculate
    for i in cat_e:              # total amounts per category
        dict_e[i.name] = 0
        for j in t:
            if j.category_id.name == i.name:
                dict_e[i.name] += int(j.amount/100)
    keys = list(dict_e.keys())        # clean dict form "0" elements
    for i in keys:
        if dict_e[i] <= 0:
            dict_e.pop(i)
    values = dict_e.values()    # calculate monthly total Exp
    expenses = 0
    for i in values:
        expenses += i
    list_e = list(dict_e.items())   # cook context: transform dict to list of tuples
    list_e = sorted(list_e, key=lambda mytuple: mytuple[1], reverse=True) # sort descending 

    dict_i = {}                  # create dict of Inc categories and calculate
    for i in cat_i:                 # total amounts per category for a month
        dict_i[i.name] = 0
        for j in t:
            if j.category_id.name == i.name:
                dict_i[i.name] += int(j.amount/100)
    keys = list(dict_i.keys())        # clean dict form "0" elements
    for i in keys:
        if dict_i[i] <= 0:
            dict_i.pop(i)
    values = dict_i.values()    # calculate monthly total Inc
    incomes = 0
    for i in values:
        incomes += i
    list_i = list(dict_i.items())   # cook context: transform dict to list of tuples
    list_i = sorted(list_i, key=lambda mytuple: mytuple[1], reverse=True) # sort descending 
    
    total = incomes - expenses
    if total < 0:
        total = '- ' + str(abs(total))
    elif total > 0:
        total = '+ ' + str(total)
    else:
        total = '0'

    mylinedate = date(year=int(this_month_date[:4]),month=int(this_month_date[4:]),day=1)
    line_chart_values=[]
    for i in range(12):
        value_i = value_e = 0
        i_date = mylinedate - monthdelta(i)
        t = Transaction.objects.filter(date__year=i_date.year,
                                       date__month=i_date.month,
                                       family_id=request.user.userprofile.family_id,
                                       category_id__type='i')
        for entry in t:
            value_i += int(entry.amount/100)
        t = Transaction.objects.filter(date__year=i_date.year,
                                       date__month=i_date.month,
                                       family_id=request.user.userprofile.family_id,
                                       category_id__type='e')
        for entry in t:
            value_e += int(entry.amount/100)
        line_chart_values.insert(0,[i_date,value_e,value_i])

    
    return render(request, 'core/dashboard.html', 
                  {'navbar':'dash',      # for navbar active state triggering
                   'expenses_values': list_e,
                   'expenses_total': expenses,
                   'incomes_values': list_i,
                   'incomes_total': incomes,
                   'total': total,
                   'pie_chart_values': list_e,
                   'line_chart_values': line_chart_values,
                   'userdata': request.user.userprofile.family_id,
                   'form': form,
                   'mydate': mydate,
                   })


def add_trans_view(request, category_id):
    if not request.user.is_authenticated():
        return render(request, 'core/login_needed.html', 
              {'navbar':'transact'})   # for navbar active state triggering

    category = Category.objects.get(id=category_id)
    form = TransactionForm(request.POST or None,
                           initial={'category_id':category,
                                    'user_id':request.user,
                                    'family_id':request.user.userprofile.family_id})
    form.fields['user_id'].widget = forms.HiddenInput()
    form.fields['family_id'].widget = forms.HiddenInput()
    form.fields['category_id'].widget = forms.HiddenInput()
    form.fields['date'].widget = forms.HiddenInput()
    if form.is_valid():
        instance = form.save(commit=False)
        # post-process the instance from the form data
#         if category.type == "i":
#             instance.amount_dec *= -1  # negate value for Incomes
        instance.amount = instance.amount_dec*100   # save amount in cents
        # end of post-process
        instance.save()
        return HttpResponseRedirect('/')
    return render(request, 'core/transaction_form.html',
                  {'form': form,
                   'navbar':'transact',
                   'category': category},)

def family(request):
    if not request.user.is_authenticated():
        return render(request, 'core/login_needed.html', 
              {'navbar':'transact'})   # for navbar active state triggering
    profile = UserProfile.objects.get(user_id=request.user.id)
    form = ProfileForm(request.POST or None, instance=profile)
    User = get_user_model()
    family_members = User.objects.filter(
                userprofile__family_id=request.user.userprofile.family_id).\
                exclude(id=request.user.id)
    if form.is_valid():
#         print(form.cleaned_data['new_pin'])
        instance = form.save(commit=False)
        new_family = Family.objects.get(id=instance.family_id.id) 
        if instance.family_id.id == request.user.userprofile.family_id.id:
            return render(request, 'core/same_family_pin.html', 
                   {'family_requested':new_family.id, 'navbar':'settings'})
        if new_family.pin == form.cleaned_data['new_pin']:
            family_members = User.objects.filter(userprofile__family_id=new_family.id).\
                                        exclude(id=request.user.id)
            instance.save()
        else:
            return render(request, 'core/incorrect_pin.html', 
                   {'family_requested':new_family.id, 'navbar':'settings'})
        return render(request, 'core/correct_pin.html', 
                  {'family_requested': new_family.id,
                   'family_members': family_members,
                   'navbar':'settings'})
    userr = User.objects.get(username=request.user)
    return render(request, 'core/family.html', 
                  {'form': form, 'family_members': family_members, 'navbar':'settings',
                   'userr':userr})


