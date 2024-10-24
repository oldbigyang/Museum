from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.db import models


#文物数据
class Artifact(models.Model):

    permissions = [

        ("view_artifact", "Can view artifact"),
        ("add_artifact", "Can add artifact"),
        ("change_artifact", "Can change artifact"),
        ("delete_artifact", "Can delete artifact"),

    ]

    year = models.CharField(max_length=4, default='0000')    # 年
    month = models.CharField(max_length=2, default='00')    # 月
    day = models.CharField(max_length=2, default='00')    # 日
    registration_number = models.CharField(max_length=50, default='---')    # 总登记号
    classification_number = models.CharField(max_length=50, default='---')    # 分类号
    name = models.CharField(max_length=200, default='---')    # 文物名称
    era = models.CharField(max_length=100, default='---')    # 年代
    quantity = models.CharField(max_length=20, default='---')    # 件数
    unit = models.CharField(max_length=20, default='---')    # 单位
    size = models.CharField(max_length=50, default='---')    # 尺寸
    weight = models.CharField(max_length=50, default='---')    # 重量
    texture = models.CharField(max_length=100, default='---')    # 质地
    condition = models.CharField(max_length=200, default='---')    # 完残情况
    source = models.CharField(max_length=200, default='---')    # 来源
    entrance_certificate_number = models.CharField(max_length=50, default='---')    # 入馆凭证号
    cancellation_certificate_number = models.CharField(max_length=50, default='---')    # 注销凭证号
    level = models.CharField(max_length=50, default='---')    # 级别
    remarks = models.TextField(default='---')    # 备注
    person_in_charge = models.CharField(max_length=50, default='---')    # 负责人
    file_number = models.CharField(max_length=50, default='---')    # 档案编号
    shape_description = models.TextField(default='---')    # 形状内容描述
    current_storage_conditions = models.CharField(max_length=200, default='---')    # 当前保存条件
    inscriptions = models.TextField(default='---')    # 铭记提拔

    def __str__(self):
        return self.name

# 用户数据
class CustomUser(AbstractUser):
    real_name = models.CharField(max_length=100)        # 真实姓名
    id_card_number = models.CharField(max_length=18, unique=True)        # 身份证号码
    phone_number = models.CharField(max_length=15)        # 手机号码

    def __str__(self):
        return self.username


# 日志模型
class LoginRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)        # 用户名
    login_time = models.DateTimeField(default=timezone.now)        # 登录时间
    logout_time = models.DateTimeField(null=True, blank=True)        # 离开时间
    ip_address = models.GenericIPAddressField()        # IP地址
    session_duration = models.DurationField(null=True, blank=True)        #使用时长

    def __str__(self):
        return f'{self.user.username} - {self.login_time}'
