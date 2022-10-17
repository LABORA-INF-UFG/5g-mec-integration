# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class ProblemDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, detail=None, instance=None, status=None, title=None, type=None):  # noqa: E501
        """ProblemDetails - a model defined in OpenAPI

        :param detail: The detail of this ProblemDetails.  # noqa: E501
        :type detail: str
        :param instance: The instance of this ProblemDetails.  # noqa: E501
        :type instance: str
        :param status: The status of this ProblemDetails.  # noqa: E501
        :type status: int
        :param title: The title of this ProblemDetails.  # noqa: E501
        :type title: str
        :param type: The type of this ProblemDetails.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'detail': str,
            'instance': str,
            'status': int,
            'title': str,
            'type': str
        }

        self.attribute_map = {
            'detail': 'detail',
            'instance': 'instance',
            'status': 'status',
            'title': 'title',
            'type': 'type'
        }

        self._detail = detail
        self._instance = instance
        self._status = status
        self._title = title
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'ProblemDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProblemDetails of this ProblemDetails.  # noqa: E501
        :rtype: ProblemDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail(self):
        """Gets the detail of this ProblemDetails.

        A human-readable explanation specific to this occurrence of the problem  # noqa: E501

        :return: The detail of this ProblemDetails.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProblemDetails.

        A human-readable explanation specific to this occurrence of the problem  # noqa: E501

        :param detail: The detail of this ProblemDetails.
        :type detail: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this ProblemDetails.

        A URI reference that identifies the specific occurrence of the problem  # noqa: E501

        :return: The instance of this ProblemDetails.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ProblemDetails.

        A URI reference that identifies the specific occurrence of the problem  # noqa: E501

        :param instance: The instance of this ProblemDetails.
        :type instance: str
        """

        self._instance = instance

    @property
    def status(self):
        """Gets the status of this ProblemDetails.

        The HTTP status code for this occurrence of the problem  # noqa: E501

        :return: The status of this ProblemDetails.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProblemDetails.

        The HTTP status code for this occurrence of the problem  # noqa: E501

        :param status: The status of this ProblemDetails.
        :type status: int
        """

        self._status = status

    @property
    def title(self):
        """Gets the title of this ProblemDetails.

        A short, human-readable summary of the problem type  # noqa: E501

        :return: The title of this ProblemDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemDetails.

        A short, human-readable summary of the problem type  # noqa: E501

        :param title: The title of this ProblemDetails.
        :type title: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this ProblemDetails.

        A URI reference according to IETF RFC 3986 that identifies the problem type  # noqa: E501

        :return: The type of this ProblemDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProblemDetails.

        A URI reference according to IETF RFC 3986 that identifies the problem type  # noqa: E501

        :param type: The type of this ProblemDetails.
        :type type: str
        """

        self._type = type
