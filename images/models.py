# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic

from entropy.mixins import EnabledMixin, OrderingMixin

from .settings import CONTENT_MODELS


class Image(models.Model):
    '''
    Image URLs that reference an external source; such as FilePicker / S3
    [{
        "url":"https://www.filepicker.io/api/file/3d6OxllbQi2bfkLhGSrg",
        "filename":"m10.png",
        "mimetype":"image/png",
        "size":166680,
        "key":"y5dz1osWQaC89JT8dUJG_m10.png",
        "container":"m10-staging","isWriteable":true
    }]

    '''

    title = models.CharField(blank=True, max_length=1024)
    alt = models.CharField(blank=True, max_length=1024)
    url = models.CharField(max_length=1024)
    filename = models.CharField(max_length=1024)
    mimetype = models.CharField(max_length=64)
    caption = models.TextField(blank=True, default='')

    def image_instances(self):
        return [
            image_instance for image_instance in
            self.imageinstance_set.enabled().prefetch_related('content_object')
        ]


class ImageInstance(EnabledMixin, OrderingMixin):
    '''Content for Image'''

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
