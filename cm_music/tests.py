from django.test import TestCase
from django.core.exceptions import ValidationError

# Create your tests here.
from . models import ContactMessage, Videos

class ContactMessageTestCase(TestCase):

    def test_contact_message_created(self):
        ContactMessage.objects.create(name="Craig", email="craig.adam.morley@gmail.com", message="Testing a contact message.")
        self.assertEqual(len(ContactMessage.objects.all()), 1)

    
    def test_contact_message_message(self):
        ContactMessage.objects.create(name="Craig", email="craig.adam.morley@gmail.com", message="Testing a different message.")
        self.assertEqual(ContactMessage.objects.get(id=1).message, "Testing a different message.")


    def test_empty_name(self):
        empty_name = ContactMessage.objects.create(name="", email="craig.adam.morley@gmail.com", message="Testing a third message.")
        self.assertFalse(empty_name.is_valid_message())

    def test_empty_email(self):
        empty_email = ContactMessage.objects.create(name="Bob", email="", message="Testing a third message.")
        self.assertFalse(empty_email.is_valid_message())

    def test_empty_message(self):
        empty_message = ContactMessage.objects.create(name="Bob", email="", message="Testing a third message.")
        self.assertFalse(empty_message.is_valid_message())


    def test_multiple_messages(self):
        ContactMessage.objects.create(name="Craig", email="craig.adam.morley@gmail.com", message="Message 1.")
        ContactMessage.objects.create(name="Craig", email="craig.adam.morley@gmail.com", message="Message 2.")
        ContactMessage.objects.create(name="helen", email="helen@email.com", message="Message 3.")
        self.assertEqual(len(ContactMessage.objects.all()), 3)


class VideosTestCase(TestCase):

    def test_video_added(self):
        Videos.objects.create(title="Lovely video", file_path="/videos/thisisthe video.mp4")
        self.assertEqual(len(Videos.objects.all()), 1)

    def test_no_file_path(self):
        video = Videos.objects.create(title="Nice vid", file_path="")
        with self.assertRaises(ValidationError):
            video.full_clean()