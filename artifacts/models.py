from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


#文物数据
class Artifact(models.Model):

    permissions = [

        ("view_artifact", "Can view artifact"),
        ("add_artifact", "Can add artifact"),
        ("change_artifact", "Can change artifact"),
        ("delete_artifact", "Can delete artifact"),

    ]

    year = models.CharField(max_length=4, default='0000', verbose_name="入藏年份")    # 年
    month = models.CharField(max_length=2, default='00', verbose_name="入藏月份")    # 月
    day = models.CharField(max_length=2, default='00', verbose_name="入藏日期")    # 日
    registration_number = models.CharField(max_length=50, default='---', verbose_name="总登记号")    # 总登记号
    classification_number = models.CharField(max_length=50, default='---', verbose_name="分类号")    # 分类号
    name = models.CharField(max_length=200, default='---', verbose_name="文物名称")    # 文物名称
    era = models.CharField(max_length=100, default='---', verbose_name="年代")    # 年代
    quantity = models.CharField(max_length=20, default='---', verbose_name="件数")    # 件数
    unit = models.CharField(max_length=20, default='---', verbose_name="单位")    # 单位
    size = models.CharField(max_length=50, default='---', verbose_name="尺寸")    # 尺寸
    weight = models.CharField(max_length=50, default='---', verbose_name="重量")    # 重量
    texture = models.CharField(max_length=100, default='---', verbose_name="质地")    # 质地
    condition = models.CharField(max_length=200, default='---', verbose_name="完残情况")    # 完残情况
    source = models.CharField(max_length=200, default='---', verbose_name="来源")    # 来源
    entrance_certificate_number = models.CharField(max_length=50, default='---', verbose_name="入馆凭证号")    # 入馆凭证号
    cancellation_certificate_number = models.CharField(max_length=50, default='---', verbose_name="注销凭证号")    # 注销凭证号
    level = models.CharField(max_length=50, default='---', verbose_name="级别")    # 级别
    remarks = models.TextField(default='---', verbose_name="备注")    # 备注
    person_in_charge = models.CharField(max_length=50, default='---', verbose_name="负责人")    # 负责人
    file_number = models.CharField(max_length=50, default='---', verbose_name="档案编号")    # 档案编号
    shape_description = models.TextField(default='---', verbose_name="形状内容描述")    # 形状内容描述
    current_storage_conditions = models.CharField(max_length=200, default='---', verbose_name="当前保存条件")    # 当前保存条件
    inscriptions = models.TextField(default='---', verbose_name="铭记题跋")    # 铭记提拔

    class Meta:
        verbose_name = _("文物")
        verbose_name_plural = _("文物列表")

    def __str__(self):
        return self.name

# 用户数据
class CustomUser(AbstractUser):
    real_name = models.CharField(max_length=100, verbose_name="真实姓名")        # 真实姓名
    id_card_number = models.CharField(max_length=18, unique=True, verbose_name="身份证号码")        # 身份证号码
    phone_number = models.CharField(max_length=15, verbose_name="手机号码")        # 手机号码

    class Meta:
        verbose_name = _("用户信息")
        verbose_name_plural = _("用户信息列表")

    def __str__(self):
        return self.username


# 日志模型
class LoginRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="用户名")  # 用户
    login_time = models.DateTimeField(default=timezone.now, verbose_name="登录时间")  # 登录时间
    logout_time = models.DateTimeField(null=True, blank=True, verbose_name="离开时间")  # 离开时间
    ip_address = models.GenericIPAddressField(verbose_name="用户端IP地址")  # IP地址
    session_duration = models.DurationField(null=True, blank=True, verbose_name="在线时长")  # 使用时长
    actions = models.TextField(null=True, blank=True, verbose_name="在线操作内容")  # 存储用户操作记录

    class Meta:
        verbose_name = _("用户日志")
        verbose_name_plural = _("用户日志列表")

    def __str__(self):
        return f'{self.user.username} - {self.login_time}'