import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_manager.settings")
django.setup()

from users.models import User

# user = User(
#     name = 'vlad1',
#     email = 'safaf@gmail.com',
#     role = 'user',
# )
# user.save()

user = User.objects.get(id=2)
user.role = 'user'
user.save()
