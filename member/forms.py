from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['username', 'password']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['password1', 'password2']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                # 'class': 'form-control'
            })

    class Meta:
        model = User

        # fields = '__all__'
        fields = (
            'user_categ',
            'username',
            'password1',
            'password2',
            'full_name',
            # 'last_name',
            # 'first_name',
            'email',
            'img_profile',
            'birth_date',
            'gender',
            'phone_number',
            'job_selects1',
            'job_selects2',
            'job_selects3',
            'profile',
        )
        widgets = {
            'user_categ': forms.Select(
                attrs={
                    # 'class': 'form-control',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                }
            ),
            # 'first_name': forms.TextInput(
            #     attrs={
            #         # 'class': 'form-control',
            #     }
            # ),
            # 'last_name': forms.TextInput(
            #     attrs={
            #         # 'class': 'form-control',
            #     }
            # ),
            'username': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    # 'class': 'form-control',
                }
            ),
            'gender': forms.Select(
                attrs={
                    # 'class': 'form-control',
                }
            ),
            'birth_date': forms.SelectDateWidget(
                attrs = {
                 },years = range(1920, 2018),),

            'profile': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                }
            ),


        }
        labels = {
            'username': '아이디',
            'email': '이메일',
            'job_selects1':'직종선택1',
            'job_selects2':'직종선택2',
            'job_selects3':'직종선택3',
        }
