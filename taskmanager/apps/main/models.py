from django.db import models

class Task(models.Model):
    title = models.CharField('Название задачи', max_length=100)
    task = models.TextField('Описание задачи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
