from django.conf.urls import url
from core import views as core_views

urlpatterns = [
    url(r'^$', core_views.transactions_exp, name='transactions_exp'),
    url(r'^inc', core_views.transactions_inc, name='transactions_inc'),
    url(r'^add/(?P<category_id>[0-9]+)', core_views.add_trans_view, name='add_trans_url'),
    url(r'^dashboard', core_views.dashboard, name='dashboard_url'),
    url(r'^family', core_views.family, name='family_url'),
]