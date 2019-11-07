from django.db import models
from django.conf import settings
from django.utils import timezone
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Video(BaseModel):
    class Meta:
        db_table = 'video'

    video = models.FileField(upload_to='video/')
    name = models.CharField(blank=False, null=False, max_length = 100, verbose_name='Name')
    theme = models.TextField(blank=False, null=False, max_length = 4000, verbose_name='Theme')


    def __str__(self):
        return self.name

    @property
    def thumbs_up(self):
        print(self.video)
        return Like.objects.filter(like=0,video_id = self.id).count()

    @property
    def thumbs_down(self):
        return Like.objects.filter(like=1,video_id = self.id).count()


class Like(BaseModel):
    class Meta:
        db_table = 'like'
        ordering = ['-like']

    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name= 'Video')
    like = models.IntegerField(verbose_name= 'Likes')

    @property
    def thumbs_down(self):
        return Like.objects.filter().count()

