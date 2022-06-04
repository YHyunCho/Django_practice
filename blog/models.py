from django.db import models

# Create your models here.
class Post(models.Model) :
  title = models.CharField(max_length=30)
  content = models.TextField()
  
  head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank = True)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)


  # 포스트 제목이 뜨게 해주는 코드
  def __str__(self) :
    return f'[{self.pk}]{self.title}'
    # self.pk -> 해당 포스트의 pk 값 / self.title -> 해당 포스트의 title 값

  def get_absolute_url(self) :
    return f'/blog/{self.pk}/'