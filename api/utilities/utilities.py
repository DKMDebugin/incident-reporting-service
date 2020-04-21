"""Contains utility function to upload files and reverse a query string"""

import os

from django.urls import reverse
from django.utils.http import urlencode


def reverse_querystring(viewname, kwargs=None, query_kwargs=None):
    """
    Custom reverse to add a query string after the url
    Example usage:
    url = my_reverse('my_test_url', kwargs={'pk': object.id}, query_kwargs={'next': reverse('home')})
    """
    url = reverse(viewname, kwargs=kwargs)

    if query_kwargs:
        return u'%s?%s' % (url, urlencode(query_kwargs))

    return url


def get_filename_ext(filepath):
    """Split file path into name & extension"""
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_file_path(instance, filename):
    """Create New File Name"""
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = f"{new_filename}{ext}"
    return f'blog/{new_filename}/{final_filename}'
