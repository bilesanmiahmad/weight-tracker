from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from accounts.models import User

# Register your models here.


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class AccountAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'is_active', 'is_staff')
    readonly_fields = ('date_joined',)
    exclude = ('username',)
    add_form = AccountCreationForm
    fieldsets = (
        (None, {
            'fields': (
                'email', 'password', 'first_name',
                'last_name',
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, AccountAdmin)
