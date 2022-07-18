from django.contrib.auth.models import UserManager
# from django.contrib


class CustomManager(UserManager):
   def create_user(self, username: str, email, password, **extra_fields):
       email = self.normalize_email(email = email)
       user = self.model(email = email)
       user.set_password()
       user.save()

       return user