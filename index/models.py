from django.db import models
from django.contrib.auth.models import User
from .validators import (
    validate_customer_phone_number,
    validate_customer_city, validate_customer_zip_code)


class UnitedUserProfile(models.Model):
    """
    Extends User model with
    contact details and address information.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=17, validators=[
            validate_customer_phone_number], blank=False)
    city = models.CharField(
        max_length=50, validators=[
            validate_customer_city], blank=True)
    zip_code = models.CharField(
        max_length=10, validators=[
            validate_customer_zip_code], blank=True)

    def __str__(self):
        """
    Returns the username associated
    with the user profile.
        """
        return self.user.username


class ContactMessage(models.Model):
    """
    Model to store contact messages submitted by users.
    Includes fields for name, email,
    and the message content, along with a
    timestamp marking when the message was submitted.
    """
    name = models.CharField(max_length=40)
    phone_number = models.CharField(
        max_length=17, validators=[
            validate_customer_phone_number], blank=False)
    email = models.EmailField()
    message = models.TextField(max_length=350)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the message,
        showing the sender's name and email.
        """
        return f"Message from {self.name} - {self.email}"