# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util

from models.mts_capability_info_mts_access_info import MtsCapabilityInfoMtsAccessInfo  # noqa: E501
from models.mts_capability_info_time_stamp import MtsCapabilityInfoTimeStamp  # noqa: E501


class MtsCapabilityInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mts_access_info=None, mts_mode=None, time_stamp=None):  # noqa: E501
        """MtsCapabilityInfo - a model defined in OpenAPI

        :param mts_access_info: The mts_access_info of this MtsCapabilityInfo.  # noqa: E501
        :type mts_access_info: List[MtsCapabilityInfoMtsAccessInfo]
        :param mts_mode: The mts_mode of this MtsCapabilityInfo.  # noqa: E501
        :type mts_mode: List[int]
        :param time_stamp: The time_stamp of this MtsCapabilityInfo.  # noqa: E501
        :type time_stamp: MtsCapabilityInfoTimeStamp
        """
        self.openapi_types = {
            'mts_access_info': List[MtsCapabilityInfoMtsAccessInfo],
            'mts_mode': List[int],
            'time_stamp': MtsCapabilityInfoTimeStamp
        }

        self.attribute_map = {
            'mts_access_info': 'mtsAccessInfo',
            'mts_mode': 'mtsMode',
            'time_stamp': 'timeStamp'
        }

        self._mts_access_info = mts_access_info
        self._mts_mode = mts_mode
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'MtsCapabilityInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MtsCapabilityInfo of this MtsCapabilityInfo.  # noqa: E501
        :rtype: MtsCapabilityInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mts_access_info(self):
        """Gets the mts_access_info of this MtsCapabilityInfo.

        The information on access network connection as defined below  # noqa: E501

        :return: The mts_access_info of this MtsCapabilityInfo.
        :rtype: List[MtsCapabilityInfoMtsAccessInfo]
        """
        return self._mts_access_info

    @mts_access_info.setter
    def mts_access_info(self, mts_access_info):
        """Sets the mts_access_info of this MtsCapabilityInfo.

        The information on access network connection as defined below  # noqa: E501

        :param mts_access_info: The mts_access_info of this MtsCapabilityInfo.
        :type mts_access_info: List[MtsCapabilityInfoMtsAccessInfo]
        """
        if mts_access_info is None:
            raise ValueError("Invalid value for `mts_access_info`, must not be `None`")  # noqa: E501
        if mts_access_info is not None and len(mts_access_info) < 1:
            raise ValueError("Invalid value for `mts_access_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._mts_access_info = mts_access_info

    @property
    def mts_mode(self):
        """Gets the mts_mode of this MtsCapabilityInfo.

        Numeric value corresponding to a specific MTS operation supported by the TMS 0 = low cost, i.e. using the unmetered access network connection whenever it is available 1 = low latency, i.e. using the access network connection with lower latency 2 = high throughput, i.e. using the access network connection with higher throughput, or/and multiple access network connection simultaneously if supported 3 = redundancy, i.e. sending duplicated (redundancy) packets over multiple access network connections for highreliability and low-latency applications 4 = QoS, i.e. performing MTS based on the specific QoS requirements from the app  # noqa: E501

        :return: The mts_mode of this MtsCapabilityInfo.
        :rtype: List[int]
        """
        return self._mts_mode

    @mts_mode.setter
    def mts_mode(self, mts_mode):
        """Sets the mts_mode of this MtsCapabilityInfo.

        Numeric value corresponding to a specific MTS operation supported by the TMS 0 = low cost, i.e. using the unmetered access network connection whenever it is available 1 = low latency, i.e. using the access network connection with lower latency 2 = high throughput, i.e. using the access network connection with higher throughput, or/and multiple access network connection simultaneously if supported 3 = redundancy, i.e. sending duplicated (redundancy) packets over multiple access network connections for highreliability and low-latency applications 4 = QoS, i.e. performing MTS based on the specific QoS requirements from the app  # noqa: E501

        :param mts_mode: The mts_mode of this MtsCapabilityInfo.
        :type mts_mode: List[int]
        """
        if mts_mode is None:
            raise ValueError("Invalid value for `mts_mode`, must not be `None`")  # noqa: E501
        if mts_mode is not None and len(mts_mode) < 1:
            raise ValueError("Invalid value for `mts_mode`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._mts_mode = mts_mode

    @property
    def time_stamp(self):
        """Gets the time_stamp of this MtsCapabilityInfo.


        :return: The time_stamp of this MtsCapabilityInfo.
        :rtype: MtsCapabilityInfoTimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this MtsCapabilityInfo.


        :param time_stamp: The time_stamp of this MtsCapabilityInfo.
        :type time_stamp: MtsCapabilityInfoTimeStamp
        """

        self._time_stamp = time_stamp