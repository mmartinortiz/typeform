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

    def get_form(self, form_key):
        """
        Returns a form object which can be queried to get
        responses to typeforms
        Parameters: formKey - Check the typeform API docs for info
        """
        # TODO implement exception for no network etc.
        api_url = "https://api.typeform.com/v0/form/{0}?key={1}".format(
            form_key, self.API_KEY)
        response = requests.get(api_url)
        status_code = response.status_code
        redirect_url = "https://api.typeform.com/login/"
        if status_code == 200 and response.url != redirect_url:
            return TypeForm(response.json())
        elif status_code == 404:
            raise ValueError("404 Not Found - Check Form Key")
        else:
            raise ValueError("404 Not Found - Check API_KEY")
