from django.db import models

# Create your models here.
class Code_categ(models.Model):
    cc_name = models.CharField('카테고리 이름',max_length=10, null=False)

    class Meta:
        verbose_name = '코드 카테고리'
        verbose_name_plural = '코드 카테고리 모음'

    def __str__(self):
        return self.cc_name

# 코드 통합(상태, 면접 신청, 직종분류, 면접상태, 고용형태)
class Code(models.Model):
    category = models.ForeignKey(Code_categ, null = False, blank = False, on_delete = models.CASCADE)
    c_num = models.IntegerField(primary_key=True)
    c_name = models.CharField('코드 이름',max_length=10, null=False)

    class Meta:
        verbose_name = '코드'
        verbose_name_plural = '코드 모음'

    def __str__(self):
        return self.c_name
