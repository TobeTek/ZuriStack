from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

class CustomUserManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@email.com', password='foo')
        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='superuser@email.com', password='foo')
        
        self.assertEqual(admin_user.email, 'superuser@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class CustomUserModelTests(TestCase):
    
    def test_user_slug_is_unique(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@email.com', password='foo')
        user2 = User.objects.create_user(email='user2@email.com', password='foo')
        self.assertNotEqual(user.slug, user2.slug)

        with self.assertRaises(IntegrityError):
            User.objects.create_user(email='user@email.com', slug='user-slug' ,password='foo')
            User.objects.create_user(email='user2@email.com', slug='user-slug' ,password='foo')

    def test___str__(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@email.com', password='foo')
        self.assertEqual(str(user), user.email)
    
    def test_user_slug_is_generated_if_blank(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@email.com', password='foo')
        self.assertNotEqual(user.slug, '')

    def test_user_slug_is_not_overwritten(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@email.com', password='foo', slug='weird-slug')
        self.assertEqual(user.slug, 'weird-slug')