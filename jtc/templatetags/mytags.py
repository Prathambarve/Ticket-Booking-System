from django import template

register = template.Library()

	# # FILTER FOR PROVIDING MODULUS OPERATION
@register.filter
def modulo(num, val):
    return num % val

