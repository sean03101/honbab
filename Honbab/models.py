from django.conf import settings
from django.db import models

# Create your models here.


class Honbab(models.Model):
    
    restraunt = models.CharField(max_length=200)
    
    level = models.CharField(max_length=10) #혼밥레벨
    menu = models.TextField()  # 주메뉴  
    img = models.TextField()   # 식당 이미지
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like',
                                           through_fields=('post', 'user'),
                                           )
                                           
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
                                           
    @property                                          
    def like_count(self):
        return self.like_user_set.count()
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(Honbab,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
                                           

