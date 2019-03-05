import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField('Текст---вопроса',max_length=200)
    pub_date = models.DateTimeField('дата---публикации')
    # verbose_name_plural = '++++Вопросы'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Уже опубликовано?'

    # pub_date.verbose_name = 'Дата публикации'
    # question_text.verbose_name = 'Текст вопроса'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Текст ---- ответа',max_length=200)
    # choice_text.verbose_name = 'Текст ответа'

    votes = models.IntegerField('К-во ---голосов',default=0)
    # votes.verbose_name = 'К-во голосов'

    def __str__(self):
        return self.choice_text

