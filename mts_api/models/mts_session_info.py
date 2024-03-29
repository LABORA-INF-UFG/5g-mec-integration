# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
from models.mts_session_info_flow_filter import MtsSessionInfoFlowFilter
from models.mts_session_info_qos_d import MtsSessionInfoQosD
from models.mts_session_info_time_stamp import MtsSessionInfoTimeStamp
import util

from models.mts_session_info_flow_filter import MtsSessionInfoFlowFilter  # noqa: E501
from models.mts_session_info_qos_d import MtsSessionInfoQosD  # noqa: E501
from models.mts_session_info_time_stamp import MtsSessionInfoTimeStamp  # noqa: E501


class MtsSessionInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_ins_id=None, flow_filter=None, mts_mode=None, qos_d=None, request_type=None, time_stamp=None, traffic_direction=None):  # noqa: E501
        """MtsSessionInfo - a model defined in OpenAPI

        :param app_ins_id: The app_ins_id of this MtsSessionInfo.  # noqa: E501
        :type app_ins_id: str
        :param flow_filter: The flow_filter of this MtsSessionInfo.  # noqa: E501
        :type flow_filter: List[MtsSessionInfoFlowFilter]
        :param mts_mode: The mts_mode of this MtsSessionInfo.  # noqa: E501
        :type mts_mode: int
        :param qos_d: The qos_d of this MtsSessionInfo.  # noqa: E501
        :type qos_d: MtsSessionInfoQosD
        :param request_type: The request_type of this MtsSessionInfo.  # noqa: E501
        :type request_type: int
        :param time_stamp: The time_stamp of this MtsSessionInfo.  # noqa: E501
        :type time_stamp: MtsSessionInfoTimeStamp
        :param traffic_direction: The traffic_direction of this MtsSessionInfo.  # noqa: E501
        :type traffic_direction: str
        """
        self.openapi_types = {
            'app_ins_id': str,
            'flow_filter': List[MtsSessionInfoFlowFilter],
            'mts_mode': int,
            'qos_d': MtsSessionInfoQosD,
            'request_type': int,
            'time_stamp': MtsSessionInfoTimeStamp,
            'traffic_direction': str
        }

        self.attribute_map = {
            'app_ins_id': 'appInsId',
            'flow_filter': 'flowFilter',
            'mts_mode': 'mtsMode',
            'qos_d': 'qosD',
            'request_type': 'requestType',
            'time_stamp': 'timeStamp',
            'traffic_direction': 'trafficDirection'
        }

        self._app_ins_id = app_ins_id
        self._flow_filter = flow_filter
        self._mts_mode = mts_mode
        self._qos_d = qos_d
        self._request_type = request_type
        self._time_stamp = time_stamp
        self._traffic_direction = traffic_direction

        @classmethod
        def from_dict(cls, dikt) -> 'MtsSessionInfo':
            """Returns the dict as a model

            :param dikt: A dict.
            :type: dict
            :return: The MtsSessionInfo of this MtsSessionInfo.  # noqa: E501
            :rtype: MtsSessionInfo
            """
            return util.deserialize_model(dikt, cls)

        @property
        def app_ins_id(self):
            """Gets the app_ins_id of this MtsSessionInfo.

            Application instance identifier  # noqa: E501

            :return: The app_ins_id of this MtsSessionInfo.
            :rtype: str
            """
            # Atribuição do ID presente no mapa de atributos da sessão à uma variável local(?). 
            self._app_ins_id = self.attribute_map.app_ins_id

            return self._app_ins_id

        @app_ins_id.setter
        def app_ins_id(self, app_ins_id):
            """Sets the app_ins_id of this MtsSessionInfo.

            Application instance identifier  # noqa: E501   

            :param app_ins_id: The app_ins_id of this MtsSessionInfo.
            :type app_ins_id: str
            """
            if app_ins_id is None:
                raise ValueError("Invalid value for `app_ins_id`, must not be `None`")  # noqa: E501

            self._app_ins_id = app_ins_id

        @property
        def flow_filter(self):
            """Gets the flow_filter of this MtsSessionInfo.

            Traffic flow filtering criteria, applicable only if when requestType is set as FLOW_SPECIFIC_MTS_SESSION. Any filtering criteria shall define a single session only. In case multiple sessions match flowFilter the request shall be rejected. If the flowFilter field is included, at least one of its subfields shall be included. Any flowFilter subfield that is not included shall be ignored in traffic flow filtering  # noqa: E501

            :return: The flow_filter of this MtsSessionInfo.
            :rtype: List[MtsSessionInfoFlowFilter]
            """
            return self._flow_filter

        @flow_filter.setter
        def flow_filter(self, flow_filter):
            """Sets the flow_filter of this MtsSessionInfo.

            Traffic flow filtering criteria, applicable only if when requestType is set as FLOW_SPECIFIC_MTS_SESSION. Any filtering criteria shall define a single session only. In case multiple sessions match flowFilter the request shall be rejected. If the flowFilter field is included, at least one of its subfields shall be included. Any flowFilter subfield that is not included shall be ignored in traffic flow filtering  # noqa: E501

            :param flow_filter: The flow_filter of this MtsSessionInfo.
            :type flow_filter: List[MtsSessionInfoFlowFilter]
            """
            if flow_filter is None:
                raise ValueError("Invalid value for `flow_filter`, must not be `None`")  # noqa: E501
            if flow_filter is not None and len(flow_filter) < 1:
                raise ValueError("Invalid value for `flow_filter`, number of items must be greater than or equal to `1`")  # noqa: E501

            self._flow_filter = flow_filter

        @property
        def mts_mode(self):
            """Gets the mts_mode of this MtsSessionInfo.

            Numeric value (0 - 255) corresponding to a specific MTS mode of the MTS session: 0 = low cost, i.e. using the unmetered access network connection whenever it is available 1 = low latency, i.e. using the access network connection with lower latency 2 = high throughput, i.e. using the access network connection with higher throughput, or multiple access network connection simultaneously 3 = redundancy, i.e. sending duplicated (redundancy) packets over multiple access network connections for high-reliability and low-latency applications 4 = QoS, i.e. performing MTS based on the QoS requirement (qosD)  # noqa: E501

            :return: The mts_mode of this MtsSessionInfo.
            :rtype: int
            """
            return self._mts_mode

        @mts_mode.setter
        def mts_mode(self, mts_mode):
            """Sets the mts_mode of this MtsSessionInfo.

            Numeric value (0 - 255) corresponding to a specific MTS mode of the MTS session: 0 = low cost, i.e. using the unmetered access network connection whenever it is available 1 = low latency, i.e. using the access network connection with lower latency 2 = high throughput, i.e. using the access network connection with higher throughput, or multiple access network connection simultaneously 3 = redundancy, i.e. sending duplicated (redundancy) packets over multiple access network connections for high-reliability and low-latency applications 4 = QoS, i.e. performing MTS based on the QoS requirement (qosD)  # noqa: E501

            :param mts_mode: The mts_mode of this MtsSessionInfo.
            :type mts_mode: int
            """
            if mts_mode is None:
                raise ValueError("Invalid value for `mts_mode`, must not be `None`")  # noqa: E501

            self._mts_mode = mts_mode

        @property
        def qos_d(self):
            """Gets the qos_d of this MtsSessionInfo.


            :return: The qos_d of this MtsSessionInfo.
            :rtype: MtsSessionInfoQosD
            """
            return self._qos_d

        @qos_d.setter
        def qos_d(self, qos_d):
            """Sets the qos_d of this MtsSessionInfo.


            :param qos_d: The qos_d of this MtsSessionInfo.
            :type qos_d: MtsSessionInfoQosD
            """
            if qos_d is None:
                raise ValueError("Invalid value for `qos_d`, must not be `None`")  # noqa: E501

            self._qos_d = qos_d

        @property
        def request_type(self):
            """Gets the request_type of this MtsSessionInfo.

            Numeric value (0 - 255) corresponding to specific type of consumer as following: 0 = APPLICATION_SPECIFIC_MTS_SESSION 1 = FLOW_SPECIFIC_MTS_SESSION  # noqa: E501

            :return: The request_type of this MtsSessionInfo.
            :rtype: int
            """
            return self._request_type

        @request_type.setter
        def request_type(self, request_type):
            """Sets the request_type of this MtsSessionInfo.

            Numeric value (0 - 255) corresponding to specific type of consumer as following: 0 = APPLICATION_SPECIFIC_MTS_SESSION 1 = FLOW_SPECIFIC_MTS_SESSION  # noqa: E501

            :param request_type: The request_type of this MtsSessionInfo.
            :type request_type: int
            """
            allowed_values = [0, 1]  # noqa: E501
            if request_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `request_type` ({0}), must be one of {1}"
                    .format(request_type, allowed_values)
                )

            self._request_type = request_type

        @property
        def time_stamp(self):
            """Gets the time_stamp of this MtsSessionInfo.


            :return: The time_stamp of this MtsSessionInfo.
            :rtype: MtsSessionInfoTimeStamp
            """
            return self._time_stamp

        @time_stamp.setter
        def time_stamp(self, time_stamp):
            """Sets the time_stamp of this MtsSessionInfo.


            :param time_stamp: The time_stamp of this MtsSessionInfo.
            :type time_stamp: MtsSessionInfoTimeStamp
            """

            self._time_stamp = time_stamp

        @property
        def traffic_direction(self):
            """Gets the traffic_direction of this MtsSessionInfo.

            The direction of the requested MTS session: 00 = Downlink (towards the UE) 01 = Uplink (towards the application/session) 10 = Symmetrical (see note)   # noqa: E501

            :return: The traffic_direction of this MtsSessionInfo.
            :rtype: str
            """
            return self._traffic_direction

        @traffic_direction.setter
        def traffic_direction(self, traffic_direction):
            """Sets the traffic_direction of this MtsSessionInfo.

            The direction of the requested MTS session: 00 = Downlink (towards the UE) 01 = Uplink (towards the application/session) 10 = Symmetrical (see note)   # noqa: E501

            :param traffic_direction: The traffic_direction of this MtsSessionInfo.
            :type traffic_direction: str
            """
            if traffic_direction is None:
                raise ValueError("Invalid value for `traffic_direction`, must not be `None`")  # noqa: E501

            self._traffic_direction = traffic_direction
