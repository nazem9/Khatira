from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like

class LikeTestCase(TestCase):
    def setUp(self):
        # Create a post
        self.user = User.objects.create_user(username='user1', password='password1')
        self.post = Post.objects.create(author =self.user ,title='Test Post', body='This is a test post')
        
        # Create users
        self.user1 = User.objects.create_user(username='user6', password='password1')
        self.user2 = User.objects.create_user(username='user09', password='password2')

        # User1 likes the post
        Like.objects.create(user=self.user1, post=self.post)
        # User2 also likes the post
        Like.objects.create(user=self.user2, post=self.post)
        
    def test_likes_count(self):
        # Get the post and count the likes
        post = Post.objects.get(title='Test Post')
        likes_count = post.like_set.count()
        
        # Check if the count is as expected
        self.assertEqual(likes_count, 2)