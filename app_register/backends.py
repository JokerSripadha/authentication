from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class StudentIDAuthBackend(BaseBackend):
    def authenticate(self, request, student_id=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Fetch user by student_id
            user = UserModel.objects.get(student_id=student_id)
            return user  # Return the user if found
        except UserModel.DoesNotExist:
            return None  # Return None if the user does not exist

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)  # Fetch user by primary key (user_id)
        except UserModel.DoesNotExist:
            return None  # Return None if user does not exist
