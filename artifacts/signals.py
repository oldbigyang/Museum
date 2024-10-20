from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from .models import LoginRecord
import datetime

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    LoginRecord.objects.create(user=user, ip_address=ip)

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    record = LoginRecord.objects.filter(user=user, logout_time__isnull=True).last()
    if record:
        record.logout_time = timezone.now()
        record.session_duration = record.logout_time - record.login_time
        record.save()
