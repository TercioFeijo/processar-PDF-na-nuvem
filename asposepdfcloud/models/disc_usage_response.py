# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2019 Aspose.PDF Cloud
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.



    OpenAPI spec version: 2.0
    
"""


from pprint import pformat
from six import iteritems
import re


class DiscUsageResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'code': 'int',
        'status': 'str',
        'disc_usage': 'DiscUsage'
    }

    attribute_map = {
        'code': 'Code',
        'status': 'Status',
        'disc_usage': 'DiscUsage'
    }

    def __init__(self, code=None, status=None, disc_usage=None):
        """
        DiscUsageResponse - a model defined in Swagger
        """

        self._code = None
        self._status = None
        self._disc_usage = None

        self.code = code
        if status is not None:
          self.status = status
        if disc_usage is not None:
          self.disc_usage = disc_usage

    @property
    def code(self):
        """
        Gets the code of this DiscUsageResponse.
        Response status code.

        :return: The code of this DiscUsageResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this DiscUsageResponse.
        Response status code.

        :param code: The code of this DiscUsageResponse.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def status(self):
        """
        Gets the status of this DiscUsageResponse.
        Response status.

        :return: The status of this DiscUsageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DiscUsageResponse.
        Response status.

        :param status: The status of this DiscUsageResponse.
        :type: str
        """

        self._status = status

    @property
    def disc_usage(self):
        """
        Gets the disc_usage of this DiscUsageResponse.

        :return: The disc_usage of this DiscUsageResponse.
        :rtype: DiscUsage
        """
        return self._disc_usage

    @disc_usage.setter
    def disc_usage(self, disc_usage):
        """
        Sets the disc_usage of this DiscUsageResponse.

        :param disc_usage: The disc_usage of this DiscUsageResponse.
        :type: DiscUsage
        """

        self._disc_usage = disc_usage

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DiscUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
