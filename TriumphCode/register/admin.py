from django.contrib import admin
from .models import problems, users_problem,competitions,competition_problems,user_competition_problems,score_user
# Register your models here.
admin.site.register(problems)
admin.site.register(users_problem)
admin.site.register(competitions)
admin.site.register(competition_problems)
admin.site.register(user_competition_problems)
admin.site.register(score_user)
