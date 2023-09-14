from django import template

#from newapp.models import Post

register = template.Library()

bad_words = [
    'Microsoft',
    'Visual'
]


text = 'Microsoft Visual Studio Code'
x = text.split()


@register.filter()
def censor(text):
    t1 = text.split()
    for t in t1:
        if t in x:
            text = text.replace(t, t[0] + (len(t)-1)*'*')
            return text
    else:
        return f'{text}'
