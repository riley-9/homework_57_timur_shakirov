from django.db import models


class Task(models.Model):
    summary = models.CharField(verbose_name='Title', null=False, blank=False, max_length=90)
    description = models.TextField(verbose_name='Description', null=True, blank=True, max_length=250)
    state = models.ManyToManyField(
        to='webapp.State',
        related_name='states',
        verbose_name='Статус',
        blank=False,
    )
    type = models.ManyToManyField(
        to='webapp.Type',
        related_name='types',
        verbose_name='Тип',
        blank=False,
    )
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'Заголовок: {self.summary}, Статус: {self.state.first()}, Тип: {self.type.first()}, Дата Обновления: {self.updated_date}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
