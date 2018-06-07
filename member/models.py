from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(gender=self.model.GENDER_OTHER, *args, **kwargs)



class User(AbstractUser):
    MENTO = '멘토'
    MENTI = '멘티'
    COMPANY = '기업'
    CHOICES_CATEG = (
        (MENTO, '멘토'),
        (MENTI, '멘티'),
        (COMPANY, '기업'),
    )

    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_OTHER = 'o'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
        (GENDER_OTHER, '기타'),
    )
    user_categ = models.CharField('회원구분', max_length=5, choices=CHOICES_CATEG, null=True)
    full_name = models.CharField('이름', max_length=10, null=True)
    img_profile = models.ImageField('프로필 사진', upload_to='user', blank=True)
    gender = models.CharField('성별', max_length=1, choices=CHOICES_GENDER)
    birth_date = models.CharField('생년월일', max_length=12, null=True, blank=True)
    profile = models.TextField('자기소개', null=True, help_text="간략하게 자기소개를 해주세요!")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="번호가 맞지 않습니다. 다시확인해주세요!")
    phone_number = models.CharField('핸드폰번호', validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    job_selects1 = models.ForeignKey('codecategory.Code', max_length=3, null=True, blank = True,)
    job_selects2 = models.ForeignKey('codecategory.Code', max_length=3, null=True, blank = True,related_name = 'job_selects2')
    job_selects3 = models.ForeignKey('codecategory.Code', max_length=3, null=True, blank = True,related_name = 'job_selects3')
    objects = UserManager()


    # def __str__(self):
    #     return self.username

    # def __str__(self):
    #     return self.user_categ

    def __str__(self):
        return '{} {}'.format(self.username, self.user_categ)

    def get_user_categ(self):
    # The user is identified by their email address
        return self.user_categ()
