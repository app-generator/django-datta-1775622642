# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    full_name = models.CharField(max_length=255, null=True, blank=True)
    dien_thoai = models.CharField(max_length=255, null=True, blank=True)
    dia_chi = models.CharField(max_length=255, null=True, blank=True)
    ngay_sinh = models.DateTimeField(blank=True, null=True, default=timezone.now)
    gioi_tinh = models.CharField(max_length=255, null=True, blank=True)
    so_bhxh = models.CharField(max_length=255, null=True, blank=True)
    so_bhyt = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Products(models.Model):

    #__Products_FIELDS__
    ma_hang = models.CharField(max_length=255, null=True, blank=True)
    ten_hang = models.CharField(max_length=255, null=True, blank=True)
    ngay_tao = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cap_nhat = models.DateTimeField(blank=True, null=True, default=timezone.now)
    quy_cach = models.ForeignKey(QuyCach, on_delete=models.CASCADE)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")


class Quycach(models.Model):

    #__Quycach_FIELDS__
    ma_quy_cach = models.CharField(max_length=255, null=True, blank=True)
    ten_quy_cach = models.CharField(max_length=255, null=True, blank=True)

    #__Quycach_FIELDS__END

    class Meta:
        verbose_name        = _("Quycach")
        verbose_name_plural = _("Quycach")


class Po_Thang(models.Model):

    #__Po_Thang_FIELDS__
    soat_phieu = models.BooleanField()
    ngay_bao = models.DateTimeField(blank=True, null=True, default=timezone.now)
    khach_hang = models.CharField(max_length=255, null=True, blank=True)
    mat_hang = models.ForeignKey(products, on_delete=models.CASCADE)
    quy_cach = models.ForeignKey(QuyCach, on_delete=models.CASCADE)
    so_luong = models.IntegerField(null=True, blank=True)
    ngay_xuat = models.DateTimeField(blank=True, null=True, default=timezone.now)
    vao_may = models.BooleanField()
    nhan_vien_kinh_doanh = models.CharField(max_length=255, null=True, blank=True)
    xuat_hoa_don = models.BooleanField()

    #__Po_Thang_FIELDS__END

    class Meta:
        verbose_name        = _("Po_Thang")
        verbose_name_plural = _("Po_Thang")



#__MODELS__END
