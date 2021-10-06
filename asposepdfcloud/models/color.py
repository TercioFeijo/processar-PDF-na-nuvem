# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


Copyright (c) 2021 Aspose.PDF Cloud
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



    OpenAPI spec version: 3.0
    
"""


from pprint import pformat
from six import iteritems
import re


class Color(object):
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
        'a': 'int',
        'r': 'int',
        'g': 'int',
        'b': 'int'
    }

    attribute_map = {
        'a': 'A',
        'r': 'R',
        'g': 'G',
        'b': 'B'
    }

    def __init__(self, a=None, r=None, g=None, b=None):
        """
        Color - a model defined in Swagger
        """

        self._a = None
        self._r = None
        self._g = None
        self._b = None

        self.a = a
        self.r = r
        self.g = g
        self.b = b

    @property
    def a(self):
        """
        Gets the a of this Color.
        Alpha component.

        :return: The a of this Color.
        :rtype: int
        """
        return self._a

    @a.setter
    def a(self, a):
        """
        Sets the a of this Color.
        Alpha component.

        :param a: The a of this Color.
        :type: int
        """
        if a is None:
            raise ValueError("Invalid value for `a`, must not be `None`")

        self._a = a

    @property
    def r(self):
        """
        Gets the r of this Color.
        Red component.

        :return: The r of this Color.
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r):
        """
        Sets the r of this Color.
        Red component.

        :param r: The r of this Color.
        :type: int
        """
        if r is None:
            raise ValueError("Invalid value for `r`, must not be `None`")

        self._r = r

    @property
    def g(self):
        """
        Gets the g of this Color.
        Green component.

        :return: The g of this Color.
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g):
        """
        Sets the g of this Color.
        Green component.

        :param g: The g of this Color.
        :type: int
        """
        if g is None:
            raise ValueError("Invalid value for `g`, must not be `None`")

        self._g = g

    @property
    def b(self):
        """
        Gets the b of this Color.
        Blue component.

        :return: The b of this Color.
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """
        Sets the b of this Color.
        Blue component.

        :param b: The b of this Color.
        :type: int
        """
        if b is None:
            raise ValueError("Invalid value for `b`, must not be `None`")

        self._b = b

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
        if not isinstance(other, Color):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
