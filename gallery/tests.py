import email
from unicodedata import category
from django.test import TestCase

from gallery.views import image
from .models import Editor, Image, Location, Category

class EditorTestClass(TestCase):
# Set up method
    def setUp(self):
        self.juliet=Editor(first_name = 'Juliet', last_name = 'Oluoch', email = 'agutujuliet@gmail.com')

#Test instance

    def test_instance(self):
        self.assertTrue(isinstance(self.juliet,Editor))


#Test Save Method

    def test_save_method(self):
        self.juliet.save_editor()
        editors = Editor.objets.all()
        self.assertTrue(len(editors) > 0)


class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.juliet=Editor(first_name = 'Juliet', last_name = 'Oluoch', email = 'agutujuliet@gmail.com')
        self.juliet.save_editor()

        # Creating a new image and saving it
        self.new_image = image('testing')
        self.new_image.save()

        self.new_article= Image(title = 'Test Image',post = 'This is a random test Image',editor = self.jjuliet)
        self.new_article.save()

        self.new_image.images.add(self.new_image)

    def tearDown(self):
        Editor.objects.all().delete()
        Image.objects.all().delete()
        Category.objects.all().delete()  
        Location.objects.all().delete() 

    def test_get_image(self):
        image = Image.image()
        self.assertTrue(len(image)>0) 


    def test_get_image_by_category(self):
        test_category = 'travel'
        category = (test_category).category()
        image_by_category = Image.image(category)
        self.assertTrue(len(image_by_category) == 0)        
