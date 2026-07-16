from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Chaia_Variety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return self.name
    

#ONE TO MANY
class Chai_Review(models.Model):
    chai = models.ForeignKey(Chaia_Variety, on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField("")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
    
# MANY TO MANY RELATION

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(Chaia_Variety,related_name='stores')

    def __str__(self):
        return self.name
    
# ONE TO ONE

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(Chaia_Variety,on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_data = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateField()

    def __str__(self):
        return f"Certificate for {self.chai.name}"
