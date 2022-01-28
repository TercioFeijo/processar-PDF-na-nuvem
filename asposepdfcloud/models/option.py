# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


Copyright (c) 2022 Aspose.PDF Cloud
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


class Option(object):
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
        'value': 'str',
        'name': 'str',
        'selected': 'bool',
        'index': 'int'
    }

    attribute_map = {
        'value': 'Value',
        'name': 'Name',
        'selected': 'Selected',
        'index': 'Index'
    }

    def __init__(self, value=None, name=None, selected=None, index=None):
        """
        Option - a model defined in Swagger
        """

        self._value = None
        self._name = None
        self._selected = None
        self._index = None

        if value is not None:
          self.value = value
        if name is not None:
          self.name = name
        if selected is not None:
          self.selected = selected
        if index is not None:
          self.index = index

    @property
    def value(self):
        """
        Gets the value of this Option.
        Gets or sets option export value.

        :return: The value of this Option.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Option.
        Gets or sets option export value.

        :param value: The value of this Option.
        :type: str
        """

        self._value = value

    @property
    def name(self):
        """
        Gets the name of this Option.
        Gets or sets name of option.

        :return: The name of this Option.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Option.
        Gets or sets name of option.

        :param name: The name of this Option.
        :type: str
        """

        self._name = name

    @property
    def selected(self):
        """
        Gets the selected of this Option.
        Gets or sets selected status of option. Returns true if option is selected.

        :return: The selected of this Option.
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """
        Sets the selected of this Option.
        Gets or sets selected status of option. Returns true if option is selected.

        :param selected: The selected of this Option.
        :type: bool
        """

        self._selected = selected

    @property
    def index(self):
        """
        Gets the index of this Option.
        Gets index of the option. 

        :return: The index of this Option.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this Option.
        Gets index of the option. 

        :param index: The index of this Option.
        :type: int
        """

        self._index = index

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
        if not isinstance(other, Option):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
