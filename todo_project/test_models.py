from django.test import TestCase
from todo_app.models import ToDoItem, ToDoList

@pytest.mark.django_db
class TestModels(TestCase):
    def test_todo_model(self):
        ToDoList.objects()