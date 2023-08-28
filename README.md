# NewProject
D2.9_News_Paper
PS C:\Users\1\PycharmProjects\NewProject> python -m venv venv
PS C:\Users\1\PycharmProjects\NewProject> venv\scripts\activate
(venv) PS C:\Users\1\PycharmProjects\NewProject> python -m pip install Django
Collecting Django
  Using cached Django-4.2.4-py3-none-any.whl (8.0 MB)
Collecting asgiref<4,>=3.6.0 (from Django)
  Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1 (from Django)
Collecting tzdata (from Django)
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-4.2.4 asgiref-3.7.2 sqlparse-0.4.4 tzdata-2023.3

[notice] A new release of pip is available: 23.1.2 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS C:\Users\1\PycharmProjects\NewProject> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\1\pycharmprojects\newproject\venv\lib\site-packages (23.1.2)
    Found existing installation: pip 23.1.2
    Uninstalling pip-23.1.2:
      Successfully uninstalled pip-23.1.2
Successfully installed pip-23.2.1
(venv) PS C:\Users\1\PycharmProjects\NewProject> django-admin startproject NewsPaper
(venv) PS C:\Users\1\PycharmProjects\NewProject> cd NewsPaper/
(venv) PS C:\Users\1\PycharmProjects\NewProject\NewsPaper> python manage.py startapp newapp
(venv) PS C:\Users\1\PycharmProjects\NewProject\NewsPaper> python manage.py makemigrations
  newapp\migrations\0001_initial.py
    - Create model Author
    - Create model Category
    - Create model Post
    - Create model PostCategory
    - Add field postCategory to post
    - Create model Comment
(venv) PS C:\Users\1\PycharmProjects\NewProject\NewsPaper> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, newapp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK   
  Applying auth.0008_alter_user_username_max_length... OK        
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying newapp.0001_initial... OK
  Applying sessions.0001_initial... OK
(venv) PS C:\Users\1\PycharmProjects\NewProject\NewsPaper> python manage.py shell
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from newapp.models import *
>>> u1 = User.objects.create_user(username='Анатолий')
>>> u1
<User: Анатолий>
>>> u2 = User.objects.create_user(username='Борис')
>>> u2
<User: Борис>
>>> Author.objects.create(authorUser=u1)
<Author: Author object (1)>
>>> Author.objects.create(authorUser=u2)
<Author: Author object (2)>
>>> Category.objects.create(name='IT')
<Category: Category object (1)>
>>> Category.objects.create(name='AI')
<Category: Category object (2)>
>>> Category.objects.create(name='NW')
<Category: Category object (3)>
>>> Category.objects.create(name='AR')
<Category: Category object (4)>
>>> author = Author.objects.get(id=1)
>>> author
<Author: Author object (1)>
>>> Post.objects.create(author=author, categoryType='NW', title='something', text='alotinfomationabou
t                                                                                                    
>>> Post.objects.create(author=author, categoryType='NW', title='something', text='alotinfomation')
<Post: Post object (1)>
>>> Post.objects.get(id=1)
<Post: Post object (1)>
>>> Post.objects.get(id=1).title
'something'
>>> Post.objects.create(author=author, categoryType='AR', title='ITdrama', text='sointerested')     
<Post: Post object (2)>
>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))
>>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
>>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
>>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anyletters')
<Comment: Comment object (1)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='anyletters')
<Comment: Comment object (2)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='anyletters')
<Comment: Comment object (3)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='anyletters')
<Comment: Comment object (4)>
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=2).dislike()
>>> Comment.objects.get(id=2).dislike()
>>> Comment.objects.get(id=2).rating   
-2
>>> Author.objects.get(id=1)
<Author: Author object (1)>
>>> a = Author.objects.get(id=1)
>>> a.update_rating()
>>> a.ratingAuthor
-1
>>> Post.objects.get(id=2).like()
>>> Author.objects.get(id=2).rating
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Author' object has no attribute 'rating'
>>> Author.objects.get(id=2).update_rating
>>> a.update_rating()
>>> a.ratingAuthor
2
>>> a = Author.objects.order_by('-ratingAuthor')[:1]
>>> a
<QuerySet [<Author: Author object (1)>]>
>>> c = Author.objects.get(id=2)          
>>> c.ratingAuthor 
0
>>> Comment.objects.get(id=2).like() 
>>> Comment.objects.get(id=2).like()
>>> c.ratingAuthor
0
>>> for i in a:
...     i.ratingAuthor
...     i.AuthorUser.username
... 
2

>>> for i in a:
...     i.ratingAuthor
...     i.authorUser.username
... 
2
'Анатолий'
>>> p = Post.objects.order_by('-rating')    
>>> for i in p[:1]:
...     i.dateCreation
...     i.author
...     i.rating
...     i.title
...     i.preview()
... 
datetime.datetime(2023, 8, 28, 12, 40, 4, 573414, tzinfo=datetime.timezone.utc)
<Author: Author object (1)>
1
'ITdrama'
'sointerested...'
>>> Post.objects.all().order_by('-rating')[0].comment_set.values('dateCreation', 'commentUser',
 'rating', 'text')
<QuerySet [{'dateCreation': datetime.datetime(2023, 8, 28, 13, 3, 52, 301412, tzinfo=datetime.t
imezone.utc), 'commentUser': 1, 'rating': 0, 'text': 'anyletters'}, {'dateCreation': datetime.d
atetime(2023, 8, 28, 13, 4, 37, 115464, tzinfo=datetime.timezone.utc), 'commentUser': 2, 'ratin
g': 0, 'text': 'anyletters'}]>
>>>
