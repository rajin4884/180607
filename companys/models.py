from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from member.models import User
from django.core.urlresolvers import reverse
# from tagging.fields import TagField
# from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings
from django.db.models import F, Sum, Avg, Count, Case, When

# Create your models here.

@python_2_unicode_compatible
class Companys(models.Model):
    BIG = '대기업'
    MIDDLE = '중소기업'
    SMALL = '소기업'
    CHOICES_SCALE = (
        (BIG, '대기업'),
        (MIDDLE, '중소기업'),
        (SMALL, '소기업'),
    )

    company_name = models.CharField('회사 이름', max_length=50, help_text="회사명을 입력해주세요.")
    occ = models.CharField('업무', max_length=50, help_text="회사의 주요 업무를 입력해주세요.")
    location = models.CharField('주소', max_length=50, help_text="회사 주소를 입력해주세요.")
    scale = models.CharField('회사 규모', max_length=50, choices=CHOICES_SCALE)
    payment = models.IntegerField('평균 연봉', default=0, help_text="평균 연봉을 입력해주세요.")

    # 부가적인 요소들
    # tag = TagField()
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.', null = True)
    # create_date = models.DateTimeField('Create Date', auto_now_add=True)
    # modify_date = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL)


    # class Meta:
    #     verbose_name = 'post'
    #     verbose_name_plural = 'posts'
    #     db_table  = 'blog_posts'
    #     ordering  = ('-modify_date',)

    def __str__(self):
        return self.company_name

    # def get_company_info(self):


    #
    def get_absolute_url(self):
        return reverse('companys:companys_detail', args=(self.slug,))
    #
    # def get_previous_post(self):
    #     return self.get_previous_by_modify_date()
    #
    # def get_next_post(self):
    #     return self.get_next_by_modify_date()
    # #
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.company_name, allow_unicode=True)
        super(Companys, self).save(*args, **kwargs)

"""

"""
@python_2_unicode_compatible
class Pay(models.Model):
    company_name = models.ForeignKey(Companys)
    mem_num = models.ForeignKey(settings.AUTH_USER_MODEL)
    g_pay = models.IntegerField(default=3000)
    # my_sum = models.IntegerField(default=0)

    def __str__(self):
        return '{} -{} : {:2d}' \
            .format(self.company_name, self.mem_num,self.g_pay)

    # def gpay_total(self):  # 합계 점수
    #     pay_annotate = Pay.objects.annotate(cname = F('company_name__company_name'), mnum = F('mem_num__username'), gpay = F('g_pay'),).values('cname', 'mnum', 'gpay')
    #     paysum = Sum('gpay')
    #     my_sum = pay_annotate.aggregate(paysum = Sum('gpay'))
    #     return self.my_sum[paysum]





'''
앨범 / 포토(기업 사진 추가 부분)
'''
from photo.fields import ThumbnailImageField

@python_2_unicode_compatible
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    # description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.OneToOneField(Companys, on_delete=models.CASCADE,
        primary_key=True)

    class Meta:
        ordering = ['album_name']

    def __str__(self):
        return self.album_name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

@python_2_unicode_compatible
class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    # description = models.TextField('Photo Description', blank=True)
    # year = models.CharField(max_length=50)
    # money = models.CharField(max_length=50)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))
