from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


default_app_config = 'wagtailvideos.apps.WagtailVideosApp'


def get_video_model_string():
    """
    Get the dotted ``app.Model`` name for the video model as a string.
    Useful for developers making Wagtail plugins that need to refer to the
    video model, such as in foreign keys, but the model itself is not required.
    """
    return getattr(settings, 'WAGTAILVIDEOS_VIDEO_MODEL', 'wagtailvideos.Video')


def get_video_model():
    """
    Get the video model from the ``WAGTAILVIDEOSVIDEO_MODEL`` setting.
    Useful for developers making Wagtail plugins that need the video model.
    Defaults to the standard :class:`~wagtailvideo.models.Video` model
    if no custom model is defined.
    """
    from django.apps import apps
    model_string = get_video_model_string()
    try:
        return apps.get_model(model_string)
    except ValueError:
        raise ImproperlyConfigured("WAGTAILVIDEOS_VIDEO_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "WAGTAILVIDEOS_VIDEO_MODEL refers to model '%s' that has not been installed" % model_string
        )
