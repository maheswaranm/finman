# To add CSS filters on the input fields instead of adding at each place
# http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/

from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})
