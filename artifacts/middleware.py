from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin



class ActivityLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from .models import LoginRecord
        response = self.get_response(request)

        if request.user.is_authenticated:
            # 获取当前的登录记录
            login_record = LoginRecord.objects.filter(user=request.user, logout_time__isnull=True).first()
            if login_record:
                # 记录用户的请求
                action = f"访问页面: {request.path}，时间: {timezone.now()}"
                if login_record.actions:
                    login_record.actions += f"; {action}"
                else:
                    login_record.actions = action
                login_record.save()

        return response
