from django.test import TestCase
from .models import Book

class get_absolute_url(TestCase):

  def test_get_absolute_url(self):
          book = Book.objects.get(id=1)
          #get_absolute_url() should take you to the detail page of book #1
          #and load the URL /books/list/1
          self.assertEqual(book.get_absolute_url(), '/books/list/1')

  def test_get_absolute_url(self):
          book = Book.objects.get(id=2)
          #get_absolute_url() should take you to the detail page of book #2
          #and load the URL /books/list/2
          self.assertEqual(book.get_absolute_url(), '/books/list/2')

  def test_get_absolute_url(self):
          book = Book.objects.get(id=3)
          #get_absolute_url() should take you to the detail page of book #3
          #and load the URL /books/list/3
          self.assertEqual(book.get_absolute_url(), '/books/list/3')

  def test_get_absolute_url(self):
          book = Book.objects.get(id=4)
          #get_absolute_url() should take you to the detail page of book #4
          #and load the URL /books/list/4
          self.assertEqual(book.get_absolute_url(), '/books/list/4')

  def test_get_absolute_url(self):
          book = Book.objects.get(id=5)
          #get_absolute_url() should take you to the detail page of book #5
          #and load the URL /books/list/5
          self.assertEqual(book.get_absolute_url(), '/books/list/5')