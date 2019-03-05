from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
# class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1
    # verbose_name = 'hjhhhjhjjhhjjh'
    verbose_name_plural = 'Ответы'

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # (None,               {'fields': ['question_text']}),
        ('Текст= вопроса', {'fields': ['question_text']}),
        ('Дата= публикации', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


