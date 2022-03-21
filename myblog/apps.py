from django.apps import AppConfig


class MyblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myblog'
    verbose_name = '博客'  # 后台
