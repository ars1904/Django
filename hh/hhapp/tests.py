from django.test import TestCase
from .models import Articles, Category
from usersapp.models import BlogUser
from faker import Faker
from mixer.backend.django import mixer
# Create your tests here.
class PostTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(name='test_category')
        user = BlogUser.objects.create_user(username='test_user', email='test@test.com', password='leo1234567')
        self.post = Articles.objects.create(name='test_post', user=user)
        self.post_str=Articles.objects.create(name='test_post_str', user=user)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        post=Articles.objects.get(name='test_post')

        self.assertFalse(post.some_method() == 'somi method')

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str')

class PostTestCaseFake(TestCase):

    def setUp(self):
        faker=Faker()
        category = Category.objects.create(name=faker.name())
        user = BlogUser.objects.create_user(username='test_user', email='test@test.com', password='leo1234567')
        self.post = Articles.objects.create(name=faker.name(), user=user)
        self.post_str=Articles.objects.create(name='test_post_str', user=user)
        print(self.post.name)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        self.assertFalse(self.post.some_method() == 'some method')

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str')

class PostTestCaseMixer(TestCase):

    def setUp(self):
        # self.post = mixer.blend(Articles)
        # user = BlogUser.objects.create_user(username='leo', email='test@test.com', password='leo1234567')
        # self.post_str=Articles.objects.create(name='test_post_str', user=user)
        self.post = mixer.blend(Articles)
        self.post_str = mixer.blend(Articles, name='test_post_str')

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        self.assertFalse(self.post.some_method() == 'some method')

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str')