import random
import string
from django.db import models
from datetime import date
from django.contrib.auth.models import User     # for UserProfile extension
# from django.core.urlresolvers import reverse
from django.dispatch import receiver            # for catching first Sign Ups
from allauth.account.signals import user_signed_up  # for catching first Sign Ups

class EntryManager(models.Manager):
    def expense(self):
        return self.filter(type='e')
    def income(self):
        return self.filter(type='i')

DEFAULT_FAMILY = 111111
DEFAULT_USER = 34       # default@default.com
DEFAULT_PIN = '0000'

class Family(models.Model):
    id = models.IntegerField('FamilyID', default=DEFAULT_FAMILY, primary_key=True)
    pin = models.CharField('PIN', max_length=4, default=DEFAULT_PIN)
    creator = models.CharField('Creator', blank=True, max_length=20)
    class Meta:
        verbose_name = 'Family'
        verbose_name_plural = 'Families'
    def __str__(self):
        return str(self.id)

class Category(models.Model):
    name = models.CharField('Name', max_length=20)
    icon = models.CharField('Icon', blank=True, max_length=20)
    icon_face = models.CharField('Icon Face', blank=True, max_length=20)
    CHOICES =(('e', 'Expense'),('i', 'Income'),)
    type = models.CharField('Type', default='e', max_length=1, choices=CHOICES)
    objects = EntryManager()    # reassigning a method for our improved Manager
                                # so we can use BlogEntry.objects.published() now!
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.IntegerField('Amount', blank=True)
    amount_dec = models.DecimalField('Amount_dec', max_digits=7, decimal_places=2, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField('Date', default=date.today)
    user_id = models.ForeignKey(User, default=DEFAULT_USER, on_delete=models.SET_DEFAULT)
    family_id = models.ForeignKey(Family, default=DEFAULT_FAMILY, on_delete=models.CASCADE)
    note = models.CharField('Note', blank=True, max_length=20)
    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ('-id',)
    def __str__(self):
        return str(self.id)

class UserProfile(models.Model):
    user_id = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    family_id = models.ForeignKey(Family, blank=True,
            on_delete=models.SET_DEFAULT,
            default=DEFAULT_FAMILY)
    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
    def __str__(self):
        return "{0}'s profile".format(self.user_id.username)

# create UserProfile record at very first request   
#User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


# populate UserProfile and create new Family when  user Signs Up first time
@receiver(user_signed_up)
def create_profile_for_new_user(sender, **kwargs):
    def start_new_family():
        def cook_f_id():
            return ''.join(random.choice(string.digits[1:]) for _ in range(6))
        f_id = cook_f_id()
        f_pin = ''.join(random.choice(string.digits[1:]) for _ in range(4))
        f_creator = str(kwargs.get('user').username) + " " + str(kwargs.get('user').email)
        while Family.objects.filter(id=f_id).exists()==True:
            f_id = cook_f_id()
        f = Family.objects.create(id=f_id, pin=f_pin, creator=f_creator)
        f.save()
        return f
    u = UserProfile.objects.get_or_create(user_id=kwargs.get('user'))[0]
    u.family_id = start_new_family()
    u.save()

#     def get_absolute_url(self):
#         return reverse('blog_details', kwargs={'year': self.published_at.year,
#                                  'month': self.published_at.strftime('%m'),
#                                  'day': self.published_at.strftime('%d'),
#                                  'slug': self.slug})
#
# improving default Manager method