# -*- coding: utf-8 -*-

import requests

from .form import TypeForm


class TypeFormAPI:
    """
    Class representing one connection to typeform
    Parameters: API_KEY - retrieved from your typeform account settings
    """

    def __init__(self, api_key):
        self.API_KEY = api_key

    def get_form(self, form_key, options_dict={}, api_version=0):
        """
        Returns a form object which can be queried to get
        responses to typeforms
        Parameters:
          formKey - Check the typeform API docs for info
          options_dict - Dictionary with TypeForm's API options. Check https://www.typeform.com/help/data-api/ for details
          api_version - API version to be used. So far we have seen version 0 and 1
        """
        # TODO implement exception for no network etc.
        # @TODO: Incorporate tests for the options
        options = '&'.join(['{}={}'.format(k, v) for k, v in options_dict.items()])
        api_url = "https://api.typeform.com/v{version}/form/{form_key}?key={api_key}&{options}".format(
            form_key=form_key, api_key=self.API_KEY, version=api_version, options=options)
        response = requests.get(api_url)
        status_code = response.status_code
        redirect_url = "https://api.typeform.com/login/"
        if status_code == 200 and response.url != redirect_url:
            return TypeForm(response.json())
        elif status_code == 400:
            raise ValueError('400 - Invalid date in query')
        elif status_code == 403:
            raise ValueError('403 - Expired token/Invalid token/token does not have access permissions/invalid token')
        elif status_code == 404:
            raise ValueError("404 - Type in URL/Invalid typeform ID")
        elif status_code == 429:
            raise ValueError("429 - Request limit reached")
        else:
            raise ValueError("Unknown returned status code - Check API_KEY")
