
from django.contrib import admin
from .models import Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option')
    search_fields = ('text',)

admin.site.register(Question, QuestionAdmin)
