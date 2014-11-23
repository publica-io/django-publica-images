# -*- coding: utf-8 -*-
import copy

from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

from .models import ImageInstance, Image


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
        )

    @property
    def image_instances(self):
        return self.qset

    @property
    def images(self):
        '''
        Traverse the ImageInstancee 
        '''
        return Image.objects.filter(
            id__in=[instance.id for instance in self.image_instances]
        )


    @property
    def image(self):
        return self.images.first()


    @property
    def icons(self):
        return self.images.filter(
            id__in=self.image_instances.filter(is_icon=True)
        )

    @property
    def icon(self):
        return self.icons.first()

    @property
    def listing_images(self):
        return self.images.filter(
            id__in=self.image_instances.filter(is_listing=True)
        )

    @property
    def listing_image(self):
        return self.listing_images.first()
