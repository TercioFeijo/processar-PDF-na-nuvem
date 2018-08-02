# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2018 Aspose.PDF Cloud
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
    
"""


from pprint import pformat
from six import iteritems
import re


class AppendDocument(object):
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
        'document': 'str',
        'start_page': 'int',
        'end_page': 'int'
    }

    attribute_map = {
        'document': 'Document',
        'start_page': 'StartPage',
        'end_page': 'EndPage'
    }

    def __init__(self, document=None, start_page=None, end_page=None):
        """
        AppendDocument - a model defined in Swagger
        """

        self._document = None
        self._start_page = None
        self._end_page = None

        if document is not None:
          self.document = document
        self.start_page = start_page
        self.end_page = end_page

    @property
    def document(self):
        """
        Gets the document of this AppendDocument.
        Document to append (server path).

        :return: The document of this AppendDocument.
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """
        Sets the document of this AppendDocument.
        Document to append (server path).

        :param document: The document of this AppendDocument.
        :type: str
        """

        self._document = document

    @property
    def start_page(self):
        """
        Gets the start_page of this AppendDocument.
        Appending start page.

        :return: The start_page of this AppendDocument.
        :rtype: int
        """
        return self._start_page

    @start_page.setter
    def start_page(self, start_page):
        """
        Sets the start_page of this AppendDocument.
        Appending start page.

        :param start_page: The start_page of this AppendDocument.
        :type: int
        """
        if start_page is None:
            raise ValueError("Invalid value for `start_page`, must not be `None`")

        self._start_page = start_page

    @property
    def end_page(self):
        """
        Gets the end_page of this AppendDocument.
        Appending end page.

        :return: The end_page of this AppendDocument.
        :rtype: int
        """
        return self._end_page

    @end_page.setter
    def end_page(self, end_page):
        """
        Sets the end_page of this AppendDocument.
        Appending end page.

        :param end_page: The end_page of this AppendDocument.
        :type: int
        """
        if end_page is None:
            raise ValueError("Invalid value for `end_page`, must not be `None`")

        self._end_page = end_page

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
        if not isinstance(other, AppendDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
