from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class problems(models.Model):
    objects = models.Manager()
    # name = models
    pid = models.AutoField(primary_key=True)
    pkey = models.CharField(max_length=100, unique=True)
    pname = models.CharField(max_length=255, blank=True, null=True)
    pstatement = models.TextField()
    pinput = models.TextField()
    poutput = models.TextField()
    psolution = models.TextField(null=True, blank=True)
    plevel = models.CharField(max_length=15)
    ptag = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.pname

    class Meta:
        db_table = 'problems'
        verbose_name_plural = 'problems'


class users_problem(models.Model):
    objects = models.Manager()
    uid = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    pid = models.ForeignKey(
        'problems',
        on_delete=models.CASCADE,
    )
    submitted_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.uid.username+ " solved " + self.pid.pname

    class Meta:
        db_table = 'user_problems'
        verbose_name_plural = 'user_problems'


class competitions(models.Model):
    objects = models.Manager()
    # name = models
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=255, blank=True, null=True)
    cdescription = models.TextField(blank=True, null=True)
    cstarttime = models.DateTimeField()
    cduration = models.FloatField()

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'competitions'
        verbose_name_plural = 'competitions'


class competition_problems(models.Model):
    objects = models.Manager()
    cid = models.ForeignKey(
        'competitions',
        on_delete=models.CASCADE,
    )
    pid = models.ForeignKey(
        'problems',
        on_delete=models.CASCADE,
    )
    added_on = models.DateTimeField(default=datetime.now, blank=True)
    cpscore = models.PositiveIntegerField(default=10)

    def __str__(self):
        #e = competitions.objects.get(cid=self.cid.get_cname(self))
        return str(self.cid.cname)

    class Meta:
        db_table = 'competition_problems'
        verbose_name_plural = 'competition_problems'


class user_competition_problems(models.Model):
    objects = models.Manager()
    uid = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    cid = models.ForeignKey(
        'competitions',
        on_delete=models.CASCADE,
    )
    pid = models.ForeignKey(
        'problems',
        on_delete=models.CASCADE,
    )
    submitted_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.uid.username+ " participated in "+ self.cid.cname+ " and solved " + self.pid.pname

    class Meta:
        db_table = 'user_competition_problems'
        verbose_name_plural = 'user_competition_problems'

class score_user(models.Model):
    objects = models.Manager()
    competitionid = models.ForeignKey(
        'competitions',
        on_delete=models.CASCADE,
    )
    userid = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    score = models.PositiveIntegerField(default=0, null=True, blank = True)

