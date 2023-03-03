from django.db import models


class Entry(models.Model):
    STATUS_CHOICE = [
        ('active', ' Активно'),
        ('blocked', 'Заблокированно')
    ]

    author = models.CharField(max_length=120, blank=False, null=False, verbose_name='Author')
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    text = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, null=False, blank=False,
                              default=STATUS_CHOICE[0][0], verbose_name='Status')
