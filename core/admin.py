from django.contrib import admin
from .models import Transaction, Category, Family, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'icon', 'icon_face')
    list_display_links = ('name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'amount_dec', 'category_id', 'user_id', 'family_id', 'date', 'note')
    
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'pin', 'creator')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'family_id')
    list_display_links = ('user_id',)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfiles'

# extend UserAdmin class, add UserProfile inlines, add new columns
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

    def get_family_id(self, u):
        return u.userprofile.family_id
    get_family_id.short_description = 'family'

    def __init__(self, *args, **kwargs):
        super(BaseUserAdmin,self).__init__(*args, **kwargs)
        columns = list(BaseUserAdmin.list_display)
        BaseUserAdmin.list_display = ['id', ] + \
            columns[:-1] + ['get_family_id'] + \
            columns[-1:]
    
    list_display_links = ('username', 'email')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)




admin.site.register(Family, FamilyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(UserProfile, UserProfileAdmin)