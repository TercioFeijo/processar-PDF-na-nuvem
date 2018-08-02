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


class LinkAnnotation(object):
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
        'action_type': 'LinkActionType',
        'action': 'str',
        'highlighting': 'LinkHighlightingMode',
        'color': 'Color'
    }

    attribute_map = {
        'links': 'Links',
        'action_type': 'ActionType',
        'action': 'Action',
        'highlighting': 'Highlighting',
        'color': 'Color'
    }

    def __init__(self, links=None, action_type=None, action=None, highlighting=None, color=None):
        """
        LinkAnnotation - a model defined in Swagger
        """

        self._links = None
        self._action_type = None
        self._action = None
        self._highlighting = None
        self._color = None

        if links is not None:
          self.links = links
        if action_type is not None:
          self.action_type = action_type
        if action is not None:
          self.action = action
        if highlighting is not None:
          self.highlighting = highlighting
        if color is not None:
          self.color = color

    @property
    def links(self):
        """
        Gets the links of this LinkAnnotation.
        Link to the document.

        :return: The links of this LinkAnnotation.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this LinkAnnotation.
        Link to the document.

        :param links: The links of this LinkAnnotation.
        :type: list[Link]
        """

        self._links = links

    @property
    def action_type(self):
        """
        Gets the action_type of this LinkAnnotation.

        :return: The action_type of this LinkAnnotation.
        :rtype: LinkActionType
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this LinkAnnotation.

        :param action_type: The action_type of this LinkAnnotation.
        :type: LinkActionType
        """

        self._action_type = action_type

    @property
    def action(self):
        """
        Gets the action of this LinkAnnotation.

        :return: The action of this LinkAnnotation.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this LinkAnnotation.

        :param action: The action of this LinkAnnotation.
        :type: str
        """

        self._action = action

    @property
    def highlighting(self):
        """
        Gets the highlighting of this LinkAnnotation.

        :return: The highlighting of this LinkAnnotation.
        :rtype: LinkHighlightingMode
        """
        return self._highlighting

    @highlighting.setter
    def highlighting(self, highlighting):
        """
        Sets the highlighting of this LinkAnnotation.

        :param highlighting: The highlighting of this LinkAnnotation.
        :type: LinkHighlightingMode
        """

        self._highlighting = highlighting

    @property
    def color(self):
        """
        Gets the color of this LinkAnnotation.

        :return: The color of this LinkAnnotation.
        :rtype: Color
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this LinkAnnotation.

        :param color: The color of this LinkAnnotation.
        :type: Color
        """

        self._color = color

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
        if not isinstance(other, LinkAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
