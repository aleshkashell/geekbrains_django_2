from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse
import json

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from django.core.files.base import ContentFile

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    print('responce:')
    print(json.dumps(response, indent=4))
    if backend.name == 'vk-oauth2':
        api_url = urlunparse(('https',
                            'api.vk.com',
                            '/method/users.get',
                            None,
                            urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo')),
                                                    access_token=response['access_token'],
                                                    v='5.92')),
                            None
                            ))

        resp = requests.get(api_url)
        if resp.status_code != 200:
            return
        data = resp.json()['response'][0]
        print(json.dumps(data, indent=4))
        if data['photo'] and user.avatar == '':
            image_content = ContentFile(requests.get(data['photo']).content)
            user.avatar.save(str(data['id']), image_content)
        if data['sex']:
            user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

        if data['about']:
            user.shopuserprofile.aboutMe = data['about']

        if data['bdate']:
            bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
            age = timezone.now().date().year - bdate.year
            if age < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.vk.VKOAuth2')
            else:
                user.age = age
        user.save()
    elif backend.name == 'google-oauth2':
        if user.avatar == '':
            image_content = ContentFile(requests.get(response['picture']).content)
            user.avatar.save(str(response['email']), image_content)
        user.save()
