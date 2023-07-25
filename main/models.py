from django.db import models


class Course(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Ph(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Выбранный курс')
    number = models.CharField('Номер', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новый запрос'
        verbose_name_plural = 'Запросы'

