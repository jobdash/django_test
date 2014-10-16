"""
Django Unit Test and DocTest framework
"""

from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from todo.models import Todo
import todo.views

# tests here.


def setup(self):
    self.user = User(id=1, username="tjnelson")
    self.user.set_password("bazinga")
    self.user.save()
    self.todo = Todo(
        title='Test Todo',
        status="C",
        description='This is a test todo',
        importance='A',
        owner=self.user)
    self.todo.save()


def test_short_model_name(self):
    self.assertEqual(self.todo.short_description(), 'This is a test todo')

    self.todo.description = "Test\nMultiple\nLines"
    self.assertEqual(self.todo.short_description(), 'Test')

    self.todo.description = ("A"*50) + ("B"*50)
    self.assertEqual(self.todo.short_description(), ("A"*50) + ("B"*30))


def test_index(self):
    client = Client()
    client.login(username=self.user.username, password='bazinga')

    response = client.get('/todos/')
    # print response.content
    self.assertTrue('Welcome, Travis' in response.content)
    self.assertTrue(self.todo.title in response.content)


def test_login(self):
    """ Login should redirect to the index page """
    client = Client()
    response = client.post(reverse(todo.views.todo_login), {'username': self.user.username, 'password': "bazinga"})

    self.assertEqual(response.status_code, 302)
    self.assertTrue(response['location'].endswith(reverse(todo.views.todo_index)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()