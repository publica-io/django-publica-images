# -*- coding: utf-8 -*-
from django.test import TestCase

from .models import Image, ImageInstance


class WidgetsTestCase(TestCase):
    def setUp(self):
        pass

    def test_image_creation(self):
        image = Image.objects.create(
            title='A nice commoncode publica picture',
            alt='Publica Images',
            url='http://lorempixel.com/640/480/cats',
            filename='cats.jpg',
            mimetype='image/jpeg',
            caption='A neat image caption'
        )

        self.assertEqual(image.title, 'A nice commoncode publica picture')
        self.assertEqual(image.alt, 'Publica Images')
        self.assertEqual(image.url, 'http://lorempixel.com/640/480/cats')
        self.assertEqual(image.filename, 'cats.jpg')
        self.assertEqual(image.mimetype, 'image/jpeg')
        self.assertEqual(image.caption, 'A neat image caption')

    def test_image_instance_caption(self):
        image = Image.objects.create(
            title='A nice commoncode publica picture',
            alt='Publica Images',
            url='http://lorempixel.com/640/480/cats',
            filename='cats.jpg',
            mimetype='image/jpeg',
            caption='A neat image caption'
        )
        instance = ImageInstance.objects.create(image=image)

        self.assertEqual(instance.caption, 'A neat image caption')

        instance._caption = 'Foobar'
        instance.save()

        self.assertEqual(instance.caption, 'Foobar')
