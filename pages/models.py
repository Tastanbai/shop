
from django.db import models

class Certificate(models.Model):
    image = models.ImageField(upload_to='certificates/', verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'Сертификат {self.id}'


class PortfolioItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    youtube_url = models.URLField(verbose_name='Ссылка на YouTube')

    def __str__(self):
        return self.title

    def get_embed_url(self):
        """Преобразует обычную ссылку в embed-ссылку"""
        if "watch?v=" in self.youtube_url:
            return self.youtube_url.replace("watch?v=", "embed/")
        elif "youtu.be/" in self.youtube_url:
            video_id = self.youtube_url.split('/')[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.youtube_url
