# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic

from entropy.mixins import EnabledMixin, OrderingMixin

from .settings import CONTENT_MODELS, USE_FILEBROWSER

if USE_FILEBROWSER:
    from filebrowser.fields import FileBrowseField



class Image(EnabledMixin, OrderingMixin):

    title = models.CharField(blank=True, max_length=1024)
    alt = models.CharField(blank=True, max_length=1024)

    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        limit_choices_to={'model__in': CONTENT_MODELS},
    )
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    if USE_FILEBROWSER:
        file = FileBrowseField(
            'Image file',
            blank=True,
            directory='images/',
            max_length=1024,
            null=True)
    else:
        file = models.ImageField(
            blank=True,
            upload_to='images/',
            max_length=1024,
            null=True)

    _url = models.CharField('url', blank=True, max_length=1024)
        
    caption = models.TextField(blank=True, default='')

    is_icon = models.BooleanField(default=False)
    is_listing = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Attached Image'
        verbose_name_plural = 'Attachable Images to Content'

    def __unicode__(self):
        return self.url

    @property
    def url(self):
        try:
            return self.file.url
        except AttributeError:
            return self._url
