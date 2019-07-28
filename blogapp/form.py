from django import forms
from .models import Blog


class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog    #어떤 모델을 기반으로 form을 만들것인지 정의
        fields = ['title', 'body']#어떤 항목을 입력받을 것인지 정의 