# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class MtsSessionInfoTimeStamp(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nano_seconds=None, seconds=None):  # noqa: E501
        """MtsSessionInfoTimeStamp - a model defined in OpenAPI

        :param nano_seconds: The nano_seconds of this MtsSessionInfoTimeStamp.  # noqa: E501
        :type nano_seconds: int
        :param seconds: The seconds of this MtsSessionInfoTimeStamp.  # noqa: E501
        :type seconds: int
        """
        self.openapi_types = {
            'nano_seconds': int,
            'seconds': int
        }

        self.attribute_map = {
            'nano_seconds': 'nanoSeconds',
            'seconds': 'seconds'
        }

        self._nano_seconds = nano_seconds
        self._seconds = seconds

    @classmethod
    def from_dict(cls, dikt) -> 'MtsSessionInfoTimeStamp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MtsSessionInfo_timeStamp of this MtsSessionInfoTimeStamp.  # noqa: E501
        :rtype: MtsSessionInfoTimeStamp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nano_seconds(self):
        """Gets the nano_seconds of this MtsSessionInfoTimeStamp.

        The nanoseconds part of the Time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :return: The nano_seconds of this MtsSessionInfoTimeStamp.
        :rtype: int
        """
        return self._nano_seconds

    @nano_seconds.setter
    def nano_seconds(self, nano_seconds):
        """Sets the nano_seconds of this MtsSessionInfoTimeStamp.

        The nanoseconds part of the Time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :param nano_seconds: The nano_seconds of this MtsSessionInfoTimeStamp.
        :type nano_seconds: int
        """
        if nano_seconds is None:
            raise ValueError("Invalid value for `nano_seconds`, must not be `None`")  # noqa: E501

        self._nano_seconds = nano_seconds

    @property
    def seconds(self):
        """Gets the seconds of this MtsSessionInfoTimeStamp.

        The seconds part of the Time. Time is defined as Unixtime since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :return: The seconds of this MtsSessionInfoTimeStamp.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this MtsSessionInfoTimeStamp.

        The seconds part of the Time. Time is defined as Unixtime since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :param seconds: The seconds of this MtsSessionInfoTimeStamp.
        :type seconds: int
        """
        if seconds is None:
            raise ValueError("Invalid value for `seconds`, must not be `None`")  # noqa: E501

        self._seconds = seconds
