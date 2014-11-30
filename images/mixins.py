# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

from .models import Image


class ImageMixin(object):
    '''
    Provide a set of methods to conveniently mixin any Image Instances
    that have been related to the mixed model
    '''

    @cached_property
    def qset(self):
        return Image.objects.filter(
            object_id=self.pk,
            content_type=ContentType.objects.get_for_model(self)
        )

    @property
    def images(self):
        return self.qset

    @property
    def image(self):
        return self.images.first()

    @property
    def icons(self):
        return self.images.filter(is_icon=True)

    @property
    def icon(self):
        return self.icons.first()

    @property
    def listing_images(self):
        return self.images.filter(is_listing=True)

    @property
    def listing_image(self):
        return self.listing_images.first()

    @property
    def mobile_images(self):
        return self.images.filter(is_mobile=True)

    @property
    def mobile_image(self):
        return self.mobile_images.first() or self.images.first()
