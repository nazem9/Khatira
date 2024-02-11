from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile  # Import your UserProfile model here

class UserProfileTest(TestCase):
    def test_user_model_has_profile(self):
        # Create a new user instance
        user = User.objects.create(
            email="nazem@gmail.com",
            username="nazem",
            password="qwerty"
        )

        # Check if the user has a related profile
        self.assertTrue(hasattr(user, 'profile'), "User should have a profile")

        # Retrieve the profile associated with the user
        profile = user.profile
        
        # Print profile details for debugging
        print("Profile details:")
        print("Birth Date:", profile.birth_date)
        print("Phone Number:", profile.phone_number)
        print("Nationality:", profile.nationality)
        print("City:", profile.city)
        print("Gender:", profile.gender)
        print("Accessibility:", profile.accessibility)
        
        # Additional assertions to diagnose the issue further
        self.assertIsNotNone(profile, "Profile should not be None")
        self.assertIsInstance(profile, UserProfile, "Profile should be an instance of UserProfile")
