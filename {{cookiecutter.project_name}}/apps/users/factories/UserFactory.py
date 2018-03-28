from django.contrib.auth.models import User
from django.utils import timezone
from factory import django, Faker, LazyAttribute, LazyFunction, Sequence, PostGenerationMethodCall


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Sequence(lambda n: 'user{}@family.com'.format(n))
    username = LazyAttribute(lambda obj: obj.email)
    password = PostGenerationMethodCall('set_password', 'myweakpassword')
    date_joined = LazyFunction(timezone.now)
