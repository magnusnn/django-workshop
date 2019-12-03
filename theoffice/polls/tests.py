import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):
    def test1(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test2(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old = Question(pub_date=time)
        self.assertIs(old.was_published_recently(), False)

    def test3(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        old = Question(pub_date=time)
        self.assertIs(old.was_published_recently(), True)

class QuestionViewTests(TestCase):
    def test1(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ingen spørsmål tilgjengelig.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test2(self):
        create_question(question_text="Utløpt spørsmål.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Utløpt spørsmål.>'])

    def test3(self):
        create_question(question_text="Spørsmålet kommer snart.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Ingen spørsmål tilgjengelig.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test4(self):
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

class QuestionDetailViewTests(TestCase):
    def test1(self):
        future_question = create_question(question_text="Future question", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test2(self):
        past_question = create_question(question_text="Past question", days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)