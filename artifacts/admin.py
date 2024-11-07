from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Artifact, CustomUser, LoginRecord

class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('id', 'registration_number', 'classification_number', 'combined_year', 'combined_name', 'person_in_charge')
    list_filter = ('person_in_charge',)
    search_fields = ('name', 'registration_number', 'classification_number')
    list_per_page = 30  # 每页显示 20 个文物
    ordering = ['registration_number']  # 默认按年份和月份排序

    def combined_name(self, obj):
        return f"{obj.era} - {obj.name}"  # 合并字段
    combined_name.short_description = '名称'  # 设置显示名称

    def combined_year(self, obj):
        return f"{obj.year} - {obj.month} - {obj.day}"
    combined_year.short_description = '年代'

admin.site.register(Artifact, ArtifactAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('real_name', 'id_card_number', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('real_name', 'id_card_number', 'phone_number')}),
    )
    list_display = ('username', 'real_name', 'id_card_number', 'phone_number')

admin.site.register(CustomUser, CustomUserAdmin)

class LoginRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time', 'logout_time', 'ip_address', 'session_duration')
    list_filter = ('user', 'login_time')
    search_fields = ('user__username', 'ip_address')

admin.site.register(LoginRecord, LoginRecordAdmin)