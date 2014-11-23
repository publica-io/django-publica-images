# -*- coding: utf-8 -*-
from django.conf import settings


# @@@ TODO: recurse through available content apps and dynamically set this
CONTENT_MODELS = getattr(
    settings, 'IMAGES_CONTENT_MODELS', ['post', 'page', 'widget']
)

# Should we use Django Filebrowser's FileBrowseField?

USE_FILEBROWSER = getattr(
	settings, 'IMAGES_USE_FILEBROWSER', False
)
