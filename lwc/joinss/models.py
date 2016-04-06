from django.db import models

# Create your models here.

class Join(models.Model):
    email = models.EmailField(max_length=256)
    friend = models.ForeignKey("self", related_name='referral', null= True, blank= True)
    ref_id = models.CharField(max_length=120, default='ABC', unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        unique_together = ("email", "ref_id",)

class JoinFriends(models.Model):
    email = models.OneToOneField(Join, related_name="Sharer")
    email = models.ForeignKey(Join)