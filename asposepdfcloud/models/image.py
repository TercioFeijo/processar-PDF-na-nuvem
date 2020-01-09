# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2020 Aspose.PDF Cloud
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


class Image(object):
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
        'width': 'int',
        'height': 'int',
        'id': 'str',
        'rectangle': 'Rectangle',
        'page_number': 'int'
    }

    attribute_map = {
        'links': 'Links',
        'width': 'Width',
        'height': 'Height',
        'id': 'Id',
        'rectangle': 'Rectangle',
        'page_number': 'PageNumber'
    }

    def __init__(self, links=None, width=None, height=None, id=None, rectangle=None, page_number=None):
        """
        Image - a model defined in Swagger
        """

        self._links = None
        self._width = None
        self._height = None
        self._id = None
        self._rectangle = None
        self._page_number = None

        if links is not None:
          self.links = links
        self.width = width
        self.height = height
        if id is not None:
          self.id = id
        if rectangle is not None:
          self.rectangle = rectangle
        self.page_number = page_number

    @property
    def links(self):
        """
        Gets the links of this Image.
        Link to the document.

        :return: The links of this Image.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Image.
        Link to the document.

        :param links: The links of this Image.
        :type: list[Link]
        """

        self._links = links

    @property
    def width(self):
        """
        Gets the width of this Image.
        Gets width of the image.

        :return: The width of this Image.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this Image.
        Gets width of the image.

        :param width: The width of this Image.
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this Image.
        Gets height of the image.

        :return: The height of this Image.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this Image.
        Gets height of the image.

        :param height: The height of this Image.
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")

        self._height = height

    @property
    def id(self):
        """
        Gets the id of this Image.
        Gets ID of the image.

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Image.
        Gets ID of the image.

        :param id: The id of this Image.
        :type: str
        """

        self._id = id

    @property
    def rectangle(self):
        """
        Gets the rectangle of this Image.
        Gets rectangle of the image.

        :return: The rectangle of this Image.
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle of this Image.
        Gets rectangle of the image.

        :param rectangle: The rectangle of this Image.
        :type: Rectangle
        """

        self._rectangle = rectangle

    @property
    def page_number(self):
        """
        Gets the page_number of this Image.
        Gets page number.

        :return: The page_number of this Image.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this Image.
        Gets page number.

        :param page_number: The page_number of this Image.
        :type: int
        """
        if page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")

        self._page_number = page_number

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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
