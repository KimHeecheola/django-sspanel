from django.db.models.signals import pre_delete, post_save
from apps.sspanel import models as m


def clear_get_configs_by_user_level_cache(sender, instance, *args, **kwargs):
    from apps.utils import cache

    if isinstance(instance, m.UserSSConfig):
        level = m.User.get_by_pk(instance.user_id).level
    else:
        level = instance.level
    key = m.UserSSConfig.get_configs_by_user_level.make_cache_key(m.UserSSConfig, level)
    cache.delete(key)


def register_connectors():

    post_save.connect(clear_get_configs_by_user_level_cache, sender=m.SSNode)
    pre_delete.connect(clear_get_configs_by_user_level_cache, sender=m.SSNode)

    post_save.connect(clear_get_configs_by_user_level_cache, sender=m.UserSSConfig)
    pre_delete.connect(clear_get_configs_by_user_level_cache, sender=m.UserSSConfig)
