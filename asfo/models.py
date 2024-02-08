from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


from django.db import models




class ItemType(models.Model):
    it_pk = models.AutoField(primary_key=True)
    it_title = models.CharField(max_length=10, null=True)
    it_type = models.CharField(max_length=10, null=True)
    tier = models.CharField(max_length=10, null=True)
    tier_1 = models.CharField(max_length=10, null=True)
    tier_2 = models.CharField(max_length=10, null=True)
    tier_3 = models.CharField(max_length=10, null=True)
    tier_4 = models.CharField(max_length=10, null=True)
    tier_5 = models.CharField(max_length=10, null=True)
    tier_6 = models.CharField(max_length=10, null=True)
    tier_7 = models.CharField(max_length=10, null=True)
    tier_8 = models.CharField(max_length=10, null=True)
    tier_9 = models.CharField(max_length=10, null=True)
    tier_10 = models.CharField(max_length=10, null=True)
    level = models.IntegerField(default=0)
    is_use = models.IntegerField(default=0)

    def __str__(self):
        return self.it_title

    class Meta:
        db_table = 'item_type'


class WeaponData(models.Model):
    it_pk = models.ForeignKey(ItemType, on_delete=models.CASCADE, db_column='it_pk')  # 외래 키 필드 이름을 "it_pk"로 지정
    wd_pk = models.AutoField(primary_key=True)
    # it_pk = models.IntegerField(default=0)
    tier = models.IntegerField(null=True)
    wd_type = models.CharField(max_length=20, null=True)
    min_dam = models.IntegerField(default=0)
    max_dam = models.IntegerField(default=0)
    dam_increase = models.IntegerField(default=0)
    buff_up = models.IntegerField(default=0)
    time_extension = models.IntegerField(default=0)
    consumption_reduction = models.IntegerField(default=0)
    hit = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    mp = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
    str = models.IntegerField(default=0)
    dex = models.IntegerField(default=0)
    con = models.IntegerField(default=0)
    wis = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    critical = models.IntegerField(default=0)
    att_speed = models.IntegerField(default=0)
    job = models.CharField(max_length=20, null=True)
    is_use = models.IntegerField(default=1)
    special_effects = models.JSONField(null=True)

    class Meta:
        db_table = 'weapon_data'

    def __str__(self):
        return self.wd_type, self.job
