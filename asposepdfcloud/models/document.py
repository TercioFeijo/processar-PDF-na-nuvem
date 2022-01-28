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


class Document(object):
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
        'document_properties': 'DocumentProperties',
        'display_properties': 'DisplayProperties',
        'pages': 'Pages'
    }

    attribute_map = {
        'links': 'Links',
        'document_properties': 'DocumentProperties',
        'display_properties': 'DisplayProperties',
        'pages': 'Pages'
    }

    def __init__(self, links=None, document_properties=None, display_properties=None, pages=None):
        """
        Document - a model defined in Swagger
        """

        self._links = None
        self._document_properties = None
        self._display_properties = None
        self._pages = None

        if links is not None:
          self.links = links
        if document_properties is not None:
          self.document_properties = document_properties
        if display_properties is not None:
          self.display_properties = display_properties
        if pages is not None:
          self.pages = pages

    @property
    def links(self):
        """
        Gets the links of this Document.
        Link to the document.

        :return: The links of this Document.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Document.
        Link to the document.

        :param links: The links of this Document.
        :type: list[Link]
        """

        self._links = links

    @property
    def document_properties(self):
        """
        Gets the document_properties of this Document.
        Document properties.

        :return: The document_properties of this Document.
        :rtype: DocumentProperties
        """
        return self._document_properties

    @document_properties.setter
    def document_properties(self, document_properties):
        """
        Sets the document_properties of this Document.
        Document properties.

        :param document_properties: The document_properties of this Document.
        :type: DocumentProperties
        """

        self._document_properties = document_properties

    @property
    def display_properties(self):
        """
        Gets the display_properties of this Document.
        Document display properties.

        :return: The display_properties of this Document.
        :rtype: DisplayProperties
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """
        Sets the display_properties of this Document.
        Document display properties.

        :param display_properties: The display_properties of this Document.
        :type: DisplayProperties
        """

        self._display_properties = display_properties

    @property
    def pages(self):
        """
        Gets the pages of this Document.
        Document pages.

        :return: The pages of this Document.
        :rtype: Pages
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages of this Document.
        Document pages.

        :param pages: The pages of this Document.
        :type: Pages
        """

        self._pages = pages

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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
