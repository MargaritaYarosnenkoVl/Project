from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=255, verbose_name='Название урока')
    video = models.URLField(max_length=250, verbose_name='URL видео')
    duration_video = models.IntegerField(verbose_name='Длительность видео в секундах')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    access = models.BooleanField(default=False, verbose_name='Доступ к уроку')
    watched_video = models.IntegerField(verbose_name='Просмотренное видео в секундах')
    status = models.CharField(max_length=14,
                              choices=[('Просмотрено', 'Просмотрено'), ('Не просмотрено', 'Не просмотрено')],
                              default='Не просмотрено', verbose_name='Статус просмотра')
    view_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def set_status(self):
        threshold = 0.8 * self.duration_video
        if self.watched_video >= threshold:
            self.status = 'Просмотрено'
        self.save()




