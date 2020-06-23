from django import forms
from .models import Post

# 장고에 PostForm이 우리가 만들 forms.ModelForm이라는 것을 알려주는 것
class PostForm(forms.ModelForm):
    class Meta:
        # 이 폼을 만들이 위해 어떤 model이 쓰여야 하는지 장고에 알려주는 것
        model = Post
        # 이 폼에 포함될 필드
        fields = ('title', 'text')