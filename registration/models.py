from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User Model without StudentManager
class StudentModel(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['first_name', 'last_name'] 

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        """ Hash password before saving it """
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """ Check password with stored hashed password """
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
    
    # def get_by_natural_key(self, email):
    #     return self.get(email=email)

