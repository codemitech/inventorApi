from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_investor = models.BooleanField(default= False)
  is_inventor = models.BooleanField(default = False)
  image =  models.ImageField(upload_to=nameFile, blank=True, null=True)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email_address = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  country = models.CharField(max_length=200)
  state = models.CharField(max_length=250, null=True)
  company_name = models.CharField(max_length=200, null=True)
  company_email = models.CharField(max_length=200, null=True)
  company_address = models.CharField(max_length=200, null=True)
  head_office = models.CharField(max_length=200, null=True)
  hobbies = models.CharField(max_length=200, null=True)
  url = models.CharField(max_length=200, null=True)
  facebook_url = models.CharField(max_length=200, null=True)
  linkedin_url = models.CharField(max_length=200, null=True)

  def __str__(self) :
      return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
      if created:
            Token.objects.create(user=instance)


class inventionImage(models.Model):
    image = models.ImageField(upload_to="image", blank=True)





class inventions(models.Model):
    inventor = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    inventor_name = models.CharField(max_length=250, null=True)
    published_date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=250)
    invention_name = models.CharField(max_length=250, null=True)
    invention_caption =  models.CharField(max_length=250, null=True)
    inventor_image =  models.ImageField(upload_to=nameFile, blank=True, null=True)
    invention_image =  models.ImageField(upload_to=nameFile, blank=True, null=True)
    inventor_name = models.CharField(max_length=250, null=True)
    CHOICES = (
        ('E', 'Entertainment'),
        ('H', 'Handcraft'),
        ('M', 'Medical'),
        ('A', 'Artificial Intelligence'),
        ('C', 'Clothing'),
        ('F', 'Fintech'),
        ('N', 'Engineering'),
        ('G', 'Agriculture'),
        ('R', 'Aircraft'),
        ('D', 'Design'),
        ('S', 'Sport'),
        ('T', 'Technology'),
    )
    industry = models.CharField(max_length=1, choices= CHOICES)
    related_industry = models.CharField(max_length=250, null=True)
    sum_required_to_complete = models.CharField(max_length=250, null=True)
    current_budget = models.CharField(null=True, max_length=250)
    TAG_CHOICES = (
        ('M', 'Music'),
        ('P', 'Potray'),
        ('G', 'Games'),
        ('E', 'Events'),
        ('S', 'Sea'),
        ('O', 'Ocean'),
        ('B', 'Building'),
        ('T', 'Technology'),
        ('W', 'Water'),
        ('J', 'Jogging'),
        ('e', 'etc'),

    )
    tag = models.CharField(max_length=1, choices= TAG_CHOICES, blank=True, null=True)
    #gallery = models.ForeignKey(
        #inventionImage, on_delete=models.CASCADE, blank=True, null=True
    #)
    additional_details = models.TextField(blank=True, null=True)
    equity_per_invest = models.CharField(null=True, max_length=250)
    invention_url = models.CharField(max_length=250, null=True)
    invention_timeline = models.CharField(max_length=250, null=True)
    target_audience = models.CharField(max_length=250, null=True)
    business_model = models.CharField(max_length=250, null=True)
    revenue_generating_stractegy =  models.CharField(max_length=250, null=True)
    expansion_plans = models.CharField(max_length=250, null=True)
    required_amount = models.CharField(max_length=250, null=True)
    amount_needed_to_start = models.CharField(max_length=250, null=True)
    currency = models.CharField(max_length=250, null=True)
    number_of_investors = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    

    #invention_gallery = models.
    def __str__(self):
        if self.invention_name:
             return self.invention_name
        else:
            return self.tag
            
    def total_views(self):
        return self.views.count()
        
    def total_likes(self):
        return self.likes.count()
"""
class Likes(models.Model):
    invent = models.ForeignKey(inventions, on_delete=models.CASCADE, blank=True, null=True)

"""

class investment(models.Model):
    
     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
     Invents= models.OneToOneField(inventions, on_delete=models.CASCADE, blank =True, null=True,  default=inventions)
     amount = models.CharField(max_length=250)
     #is_investor = models.BooleanField(default= True)
     
     def __str__(self):
         if self.amount:
             return self.amount
         else:
             return self.Invents









