from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Post(models.Model) :
  title = models.CharField(max_length=30)
  hook_text = models.CharField(max_length=100, blank=True)
  content = models.TextField()
  
  head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank = True)
  file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)
  
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

  # 포스트 제목이 뜨게 해주는 코드
  def __str__(self) :
    return f'[{self.pk}]{self.title} :: {self.author}'
    # self.pk -> 해당 포스트의 pk 값 / self.title -> 해당 포스트의 title 값

  def get_absolute_url(self) :
    return f'/blog/{self.pk}/'

  def get_file_name(self):
    return os.path.basename(self.file_upload.name)

  def get_file_ext(self) :
    return self.get_file_name().split('.')[-1]