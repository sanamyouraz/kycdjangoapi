from django.db import models

PROVINCE_CHOICE = ((
 ('Pradesh No.1','Pradesh No.1'),
 ('Pradesh No.2','Pradesh No.2'),
 ('Pradesh No.3','Pradesh No.3'),
 ('Pradesh No.4', 'Pradesh No.4'),
 ('Pradesh No.5', 'Pradesh No.5'),
))

class Profile(models.Model):
  name= models.CharField(max_length=100)
  email = models.EmailField()
  dob = models.DateField(auto_now=False, auto_now_add=False)
  province = models.CharField(choices=PROVINCE_CHOICE, max_length=50)
  gender= models.CharField(max_length=100)
  location= models.CharField(max_length=100)
  pimage = models.ImageField(upload_to='pimages', blank=True)
  rdoc = models.FileField(upload_to='rdocs', blank=True)

