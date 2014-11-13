# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

from .models import ImageInstance


class ImageMixin(object):
    '''
    Provide a set of methods to conveniently mixin any Image Instances
    that have been related to the mixed model
    '''

    @cached_property
    def qset(self):
        return ImageInstance.objects.filter(
            object_id=self.pk,
            content_type=ContentType.objects.get_for_model(self)
        )[1:]

    @property
    def images(self):
        '''Return all the images'''

        return self.qset

    @property
    def image(self):
        try:
            return self.images[0]
        except IndexError:
            return None

    @property
    def icons(self):
        return self.images.filter(is_listing=True)

    @property
    def icon(self):
        try:
            return self.icons[0]
        except IndexError:
            return None

    @property
    def listing_images(self):
        return self.images.filter(is_listing=True)

    @property
    def listing_image(self):
        try:
            return self.listing_images[0]
        except IndexError:
            return None
