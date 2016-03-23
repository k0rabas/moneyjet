from django import forms
from .models import Transaction
from datetime import date
from monthdelta import monthdelta
from core.models import UserProfile


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount_dec', 'category_id', 'user_id', 'family_id', 'note', 'date']
        widgets = {
            'amount_dec': forms.NumberInput(attrs={'placeholder': 'Amount (required)',
                                                   'autofocus': 'true',
                                                   }),  # my custom placeholder and autofocus for the widget
            'note': forms.TextInput(attrs={'placeholder': 'Note (optional)',
                                           }),   # my custom placeholders for the widget
        }

    
class DateForm(forms.Form):
#         def __init__(self, *args, **kwargs):
#         super(SomeForm, self).__init__(*args, **kwargs)
#         self.fields['field'].initial = 'inital_value'
    YEAR_CHOICES = ('2015','2016')
#     mydate = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))

    SELECTOR_CHOICES = []
    today = date.today()
    for i in range(12):
        SELECTOR_CHOICES.append((str(today.year) + str(today.month).zfill(2),
                                str(today.strftime('%B')) + ' ' + str(today.year)))
        today = today - monthdelta(1)

    selector_mydate = forms.ChoiceField(
                    widget=forms.Select(attrs={'onchange': 'this.form.submit();'}),
                    choices=SELECTOR_CHOICES,
                    label='' )
    
class pureProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['family_id']
class ProfileForm(pureProfileForm):     
    # adding new field to the form
    new_pin = forms.CharField(label='',
        widget=forms.NumberInput(attrs={'placeholder': 'PIN (4-digits number)'}))
#     new_pin = forms.TextInput(attrs={'placeholder': "New Family's 4-digits PIN"})
    class Meta(pureProfileForm.Meta):
        fields = pureProfileForm.Meta.fields + ['new_pin']
        labels = {
                  'family_id': '',
        }
        initial= {
                  'family_id': 123,
        }
        error_messages = {
            'family_id': {
                'invalid_choice': "Entered Family does not exist",
            },
        }
        widgets = {
            'family_id': forms.NumberInput(
                attrs={'placeholder': 'Family (6-digits number)','autofocus': 'true'}),
#                                                 # my custom placeholder and autofocus
#             'new_pin': forms.Textarea(attrs={'placeholder': 'Note (optional)'}),
#                                                 # my custom placeholders for the widget
        }

    
    
    
    