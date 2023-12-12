# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=unknown-option-value
# pylint: disable=no-member

from django.test import TestCase
from todo_app.models import ToDoList

class TestModels(TestCase):
    def test_todo_model(self):
        ToDoList.objects()
