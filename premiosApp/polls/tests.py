from datetime import datetime
from http import client
from django.urls.base import reverse

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

class QuestionModelTest(TestCase):
    
    # def test_was_published_recently_with_future_question(self):
    #     """was_published_recently returns false for question whose pub_date is in the future"""
    #     time = timezone.now() + datetime.timedelta(days=30)
    #     future_question= Question(Question_text="¿Quién es el mejor course Director de Platzi?", pub_date=time)
    #     self.assertIs(future_question.was_published_recently(), False)
    pass


def create_question(question_text, days):
    """
    Creates a question with the given "question_text", and publiched the given
    number of days offset to now( negative for questions published in the past,
    possitive for questions that yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text, pub_date=time)


class QuestionIndexviewTests(TestCase):
    def test_no_question(self):
        """if no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren´t displayed on the index page.
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])


    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed in the index page
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])