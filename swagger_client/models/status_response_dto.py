# coding: utf-8

"""
    e-MCF

    DGI Bénin - Tous droits réservés  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StatusResponseDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'bool',
        'version': 'str',
        'ifu': 'str',
        'nim': 'str',
        'token_valid': 'datetime',
        'server_date_time': 'datetime',
        'pending_requests_count': 'int',
        'pending_requests_list': 'list[PendingRequestDto]'
    }

    attribute_map = {
        'status': 'status',
        'version': 'version',
        'ifu': 'ifu',
        'nim': 'nim',
        'token_valid': 'tokenValid',
        'server_date_time': 'serverDateTime',
        'pending_requests_count': 'pendingRequestsCount',
        'pending_requests_list': 'pendingRequestsList'
    }

    def __init__(self, status=None, version=None, ifu=None, nim=None, token_valid=None, server_date_time=None, pending_requests_count=None, pending_requests_list=None):  # noqa: E501
        """StatusResponseDto - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._version = None
        self._ifu = None
        self._nim = None
        self._token_valid = None
        self._server_date_time = None
        self._pending_requests_count = None
        self._pending_requests_list = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if ifu is not None:
            self.ifu = ifu
        if nim is not None:
            self.nim = nim
        if token_valid is not None:
            self.token_valid = token_valid
        if server_date_time is not None:
            self.server_date_time = server_date_time
        if pending_requests_count is not None:
            self.pending_requests_count = pending_requests_count
        if pending_requests_list is not None:
            self.pending_requests_list = pending_requests_list

    @property
    def status(self):
        """Gets the status of this StatusResponseDto.  # noqa: E501


        :return: The status of this StatusResponseDto.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatusResponseDto.


        :param status: The status of this StatusResponseDto.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def version(self):
        """Gets the version of this StatusResponseDto.  # noqa: E501


        :return: The version of this StatusResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StatusResponseDto.


        :param version: The version of this StatusResponseDto.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def ifu(self):
        """Gets the ifu of this StatusResponseDto.  # noqa: E501


        :return: The ifu of this StatusResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._ifu

    @ifu.setter
    def ifu(self, ifu):
        """Sets the ifu of this StatusResponseDto.


        :param ifu: The ifu of this StatusResponseDto.  # noqa: E501
        :type: str
        """

        self._ifu = ifu

    @property
    def nim(self):
        """Gets the nim of this StatusResponseDto.  # noqa: E501


        :return: The nim of this StatusResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._nim

    @nim.setter
    def nim(self, nim):
        """Sets the nim of this StatusResponseDto.


        :param nim: The nim of this StatusResponseDto.  # noqa: E501
        :type: str
        """

        self._nim = nim

    @property
    def token_valid(self):
        """Gets the token_valid of this StatusResponseDto.  # noqa: E501


        :return: The token_valid of this StatusResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._token_valid

    @token_valid.setter
    def token_valid(self, token_valid):
        """Sets the token_valid of this StatusResponseDto.


        :param token_valid: The token_valid of this StatusResponseDto.  # noqa: E501
        :type: datetime
        """

        self._token_valid = token_valid

    @property
    def server_date_time(self):
        """Gets the server_date_time of this StatusResponseDto.  # noqa: E501


        :return: The server_date_time of this StatusResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._server_date_time

    @server_date_time.setter
    def server_date_time(self, server_date_time):
        """Sets the server_date_time of this StatusResponseDto.


        :param server_date_time: The server_date_time of this StatusResponseDto.  # noqa: E501
        :type: datetime
        """

        self._server_date_time = server_date_time

    @property
    def pending_requests_count(self):
        """Gets the pending_requests_count of this StatusResponseDto.  # noqa: E501


        :return: The pending_requests_count of this StatusResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._pending_requests_count

    @pending_requests_count.setter
    def pending_requests_count(self, pending_requests_count):
        """Sets the pending_requests_count of this StatusResponseDto.


        :param pending_requests_count: The pending_requests_count of this StatusResponseDto.  # noqa: E501
        :type: int
        """

        self._pending_requests_count = pending_requests_count

    @property
    def pending_requests_list(self):
        """Gets the pending_requests_list of this StatusResponseDto.  # noqa: E501


        :return: The pending_requests_list of this StatusResponseDto.  # noqa: E501
        :rtype: list[PendingRequestDto]
        """
        return self._pending_requests_list

    @pending_requests_list.setter
    def pending_requests_list(self, pending_requests_list):
        """Sets the pending_requests_list of this StatusResponseDto.


        :param pending_requests_list: The pending_requests_list of this StatusResponseDto.  # noqa: E501
        :type: list[PendingRequestDto]
        """

        self._pending_requests_list = pending_requests_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StatusResponseDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatusResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
