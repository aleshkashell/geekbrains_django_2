from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='basket_total_cost')
def basket_total_cost(user):
    if user.is_anonymous:
        return 0
    else:
        return user.basket.all()[0].total_cost


@register.filter(name='total_quantity')
def total_quantity(user):
    if user.is_anonymous:
        return 0
    else:
        return user.basket.all()[0].total_quantity


@register.filter(name='media_folder_products')
def media_folder_products(image):
    return settings.MEDIA_URL + str(image)
