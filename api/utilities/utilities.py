"""Contains utility function to upload files and reverse a query string"""

import os
import random

from django.urls import reverse
from django.utils.http import urlencode
from django.utils import dateformat

import pytz
from dateutil.parser import parse


class Utilities:
    """Utilities class serves as namespace for utility functions"""

    def __init__(self):
        self.folder_name = None

    @staticmethod
    def reverse_querystring(view_name, kwargs=None, query_kwargs=None):
        """
        Custom reverse to add a query string after the url
        Example usage:
        url = my_reverse('my_test_url', kwargs={'pk': object.id}, query_kwargs={'next': reverse('home')})
        """

        url = reverse(view_name, kwargs=kwargs)

        if query_kwargs:
            return u'%s?%s' % (url, urlencode(query_kwargs))

        return url

    @classmethod
    def get_filename_ext(cls, file_path):
        """Split file path into name & extension"""

        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        return name, ext

    def upload_file_path(self, instance, file_name):
        """Create New File Name"""
        assert (self.folder_name is not None), \
            f"folder_name is {self.folder_name}." \
            f"Pass it into upload_folder_file_path('folder_name')"
        new_filename = random.randint(1, 3910209312)
        name, ext = self.get_filename_ext(file_name)
        final_filename = f"{new_filename}{ext}"
        return f'{self.folder_name}/{new_filename}/{final_filename}'

    def upload_folder_file_path(self, folder_name):
        """Get folder name & return function """
        self.folder_name = folder_name
        return self.upload_file_path

    @staticmethod
    def set_type(self, *args, **kwargs):
        """Implicitly set the type of the object"""

        if not self.__class__.__subclasses__():
            self._type = self.__class__.__name__.lower()
        else:
            subclass = [x for x in self.__class__.__subclasses__()
                        if x.__name__.lower() == self._type]
            if subclass:
                self.__class__ = subclass[0]
            else:
                self._type = self.__class__.__name__.lower()

    @staticmethod
    def covert_str_to_datetime(date_str):
        date = pytz.utc.localize(parse(date_str))
        if not dateformat.is_naive(date):
            print(date)
            return date
