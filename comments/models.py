from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    name = models.CharField('名字',max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址',blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('myblog.Post', verbose_name='文章', on_delete=models.CASCADE)

    # 将 editable 参数设为 False 将不允许通过 django admin 后台编辑此字段的内容。因为阅读量应该根据被访问次数统计，而不应该人为修改。

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name



    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
