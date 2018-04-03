# coding: utf-8

"""
    Aspose.Pdf for Cloud API Reference


   Copyright (c) 2018 Aspose.Pdf for Cloud
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



    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Field(object):
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
        'links': 'list[Link]',
        'name': 'str',
        'type': 'FieldType',
        'values': 'list[str]',
        'selected_items': 'list[int]',
        'rect': 'Rectangle'
    }

    attribute_map = {
        'links': 'Links',
        'name': 'Name',
        'type': 'Type',
        'values': 'Values',
        'selected_items': 'SelectedItems',
        'rect': 'Rect'
    }

    def __init__(self, links=None, name=None, type=None, values=None, selected_items=None, rect=None):
        """
        Field - a model defined in Swagger
        """

        self._links = None
        self._name = None
        self._type = None
        self._values = None
        self._selected_items = None
        self._rect = None

        if links is not None:
          self.links = links
        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if values is not None:
          self.values = values
        if selected_items is not None:
          self.selected_items = selected_items
        if rect is not None:
          self.rect = rect

    @property
    def links(self):
        """
        Gets the links of this Field.
        Link to the document.

        :return: The links of this Field.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Field.
        Link to the document.

        :param links: The links of this Field.
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """
        Gets the name of this Field.
        Field name.

        :return: The name of this Field.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Field.
        Field name.

        :param name: The name of this Field.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Field.
        Field type.

        :return: The type of this Field.
        :rtype: FieldType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Field.
        Field type.

        :param type: The type of this Field.
        :type: FieldType
        """

        self._type = type

    @property
    def values(self):
        """
        Gets the values of this Field.
        Field values.

        :return: The values of this Field.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this Field.
        Field values.

        :param values: The values of this Field.
        :type: list[str]
        """

        self._values = values

    @property
    def selected_items(self):
        """
        Gets the selected_items of this Field.
        Selected items.

        :return: The selected_items of this Field.
        :rtype: list[int]
        """
        return self._selected_items

    @selected_items.setter
    def selected_items(self, selected_items):
        """
        Sets the selected_items of this Field.
        Selected items.

        :param selected_items: The selected_items of this Field.
        :type: list[int]
        """

        self._selected_items = selected_items

    @property
    def rect(self):
        """
        Gets the rect of this Field.
        Field rectangle.

        :return: The rect of this Field.
        :rtype: Rectangle
        """
        return self._rect

    @rect.setter
    def rect(self, rect):
        """
        Sets the rect of this Field.
        Field rectangle.

        :param rect: The rect of this Field.
        :type: Rectangle
        """

        self._rect = rect

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
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other