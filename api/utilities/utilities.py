"""Contains utility function to upload files and reverse a query string"""

import os
import random

from django.urls import reverse
from django.utils.http import urlencode


class Utilities:
    """Utilities class serves as namespace for utility functions"""

    @classmethod
    def reverse_querystring(cls, view_name, kwargs=None, query_kwargs=None):
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

    @classmethod
    def upload_file_path(cls, instance, file_name):
        """Create New File Name"""
        new_filename = random.randint(1, 3910209312)
        name, ext = cls.get_filename_ext(file_name)
        final_filename = f"{new_filename}{ext}"
        return f'{folder_name}/{new_filename}/{final_filename}'

    @classmethod
    def upload_folder_file_path(cls, folder_name):
        """Get folder name & return function """

        # def upload_file_path(instance, file_name):
        #     """Create New File Name"""
        #     new_filename = random.randint(1, 3910209312)
        #     name, ext = cls.get_filename_ext(file_name)
        #     final_filename = f"{new_filename}{ext}"
        #     return f'{folder_name}/{new_filename}/{final_filename}'

        return cls.upload_file_path

    @classmethod
    def set_type(cls, self, *args, **kwargs):
        """Implicitly set the type of the object"""

        if not self.__class__.__subclasses__():
            self._type = self.__class__.__name__.lower()
        else:
            subclass = [x for x in self.__class__.__subclasses__() if x.__name__.lower() == self._type]
            if subclass:
                self.__class__ = subclass[0]
            else:
                self._type = self.__class__.__name__.lower()
