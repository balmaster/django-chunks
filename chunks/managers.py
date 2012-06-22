# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models


class ImageManager(models.Manager):

    def url(self, key):
        try:
            obj = self.get(key=key)
        except self.model.DoesNotExist:
            return settings.STATIC_URL + 'chunks/stub.png'
        else:
            return obj.image.url
