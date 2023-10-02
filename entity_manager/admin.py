from django.contrib import admin
from .models import *
from django import forms

# Register your models here.
# admin.site.register(UniversalEntities)
admin.site.register(Business)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'business')

    def get_form(self, request, obj=None, **kwargs):
        # Exclude the 'business' field from the form
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['business'].widget = forms.HiddenInput()
        return form

    def save_model(self, request, obj, form, change):
        # Set the 'business' field based on the currently logged-in user
        if not obj.business_id and request.user.is_authenticated:
            obj.business = request.user.business
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Filter the queryset based on the logged-in user's associated business
        if request.user.is_authenticated:
            qs = qs.filter(business=request.user.business)

        return qs

admin.site.register(Type, TypeAdmin)
admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(Page)
admin.site.register(Button)
admin.site.register(AccessCode)
admin.site.register(AccessControl)
