from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['pk']
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class TegType(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['pk']
        verbose_name = 'тип'
        verbose_name_plural = 'типы тегов'
    

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    tag_type = models.ForeignKey(to=TegType, on_delete=models.CASCADE, verbose_name='тип')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['pk']
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


def update_filename(instance, filename):
        return 'previews/' + str(instance.pk) + instance.video_url
    
class Video(models.Model): 
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    video_url = models.SlugField(verbose_name='ссылка на видео')
    data_add = models.DateTimeField(auto_now_add=True, verbose_name='дата содания')
    image = models.ImageField(upload_to=update_filename, default='default.jpg')
    
    genres = models.ManyToManyField(to=Genre, blank=True, verbose_name='жанры')
    tags = models.ManyToManyField(to=Tag, blank=True, verbose_name='теги')
    
    likes = models.PositiveIntegerField(default=0, verbose_name='лайки')
    dis_likes = models.PositiveIntegerField(default=0, verbose_name='дислайки')
    views = models.PositiveIntegerField(default=0, verbose_name='просмотры')
    users_liked = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='liked_video', blank=True)
    users_disliked = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='disliked_video', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-data_add']
        verbose_name = 'видео'
        verbose_name_plural = 'видио'
    
    
class Comment(models.Model):
    text = models.TextField(blank=True, verbose_name='текст коментария')
    video = models.ForeignKey(to=Video, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0, verbose_name='лайки')
    dis_likes = models.PositiveIntegerField(default=0, verbose_name='дислайки')
    users_liked = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='liked_comments', blank=True)
    users_disliked = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='disliked_comments', blank=True)
    
    class Meta:
        ordering = ['-pk']
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'
