# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic

from entropy.mixins import EnabledMixin, OrderingMixin

from .settings import CONTENT_MODELS, USE_FILEBROWSER

if USE_FILEBROWSER:
    from filebrowser.fields import FileBrowseField



class Image(models.Model):

    title = models.CharField(blank=True, max_length=1024)
    alt = models.CharField(blank=True, max_length=1024)

    if USE_FILEBROWSER:
        file = FileBrowseField(
            'Image file',
            blank=False,
            directory='images/',
            max_length=1024,
            null=True)
    else:
        file = models.ImageField(
            upload_to='images/',
            max_length=1024)
        
    caption = models.TextField(blank=True, default='')

    def image_instances(self):
        return [
            image_instance for image_instance in
            self.imageinstance_set.enabled().prefetch_related('content_object')
        ]


class ImageInstance(EnabledMixin, OrderingMixin):
    '''
    Image Instance links the Image to the object; whereas the ImageMixin
    provides convenient pass through properties to access the image file
    properties
    '''
    # enabled
    # order

    image = models.ForeignKey('Image')
    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        limit_choices_to={'model__in': CONTENT_MODELS},
    )
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    is_icon = models.BooleanField(default=False)
    is_listing = models.BooleanField(default=False)
    _caption = models.TextField('caption', blank=True, default='')

    @property
    def caption(self):
        if self._caption:
            return self._caption
        return self.image.caption
