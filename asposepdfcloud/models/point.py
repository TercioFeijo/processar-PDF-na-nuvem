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


class Point(object):
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
        'x': 'float',
        'y': 'float'
    }

    attribute_map = {
        'x': 'X',
        'y': 'Y'
    }

    def __init__(self, x=None, y=None):
        """
        Point - a model defined in Swagger
        """

        self._x = None
        self._y = None

        self.x = x
        self.y = y

    @property
    def x(self):
        """
        Gets the x of this Point.
        X coordinate value.

        :return: The x of this Point.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x of this Point.
        X coordinate value.

        :param x: The x of this Point.
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")

        self._x = x

    @property
    def y(self):
        """
        Gets the y of this Point.
        Y coordinate value.

        :return: The y of this Point.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y of this Point.
        Y coordinate value.

        :param y: The y of this Point.
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")

        self._y = y

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
        if not isinstance(other, Point):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
