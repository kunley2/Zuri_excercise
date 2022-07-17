from django.db import models


class ActiveLinkManager(models.Manager):
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(active=True)