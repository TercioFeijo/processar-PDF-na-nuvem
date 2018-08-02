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


class TextReplace(object):
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
        'old_value': 'str',
        'new_value': 'str',
        'regex': 'bool',
        'text_state': 'TextState',
        'rect': 'Rectangle'
    }

    attribute_map = {
        'old_value': 'OldValue',
        'new_value': 'NewValue',
        'regex': 'Regex',
        'text_state': 'TextState',
        'rect': 'Rect'
    }

    def __init__(self, old_value=None, new_value=None, regex=None, text_state=None, rect=None):
        """
        TextReplace - a model defined in Swagger
        """

        self._old_value = None
        self._new_value = None
        self._regex = None
        self._text_state = None
        self._rect = None

        self.old_value = old_value
        self.new_value = new_value
        self.regex = regex
        if text_state is not None:
          self.text_state = text_state
        if rect is not None:
          self.rect = rect

    @property
    def old_value(self):
        """
        Gets the old_value of this TextReplace.
        Original text.

        :return: The old_value of this TextReplace.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """
        Sets the old_value of this TextReplace.
        Original text.

        :param old_value: The old_value of this TextReplace.
        :type: str
        """
        if old_value is None:
            raise ValueError("Invalid value for `old_value`, must not be `None`")

        self._old_value = old_value

    @property
    def new_value(self):
        """
        Gets the new_value of this TextReplace.
        New text.

        :return: The new_value of this TextReplace.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """
        Sets the new_value of this TextReplace.
        New text.

        :param new_value: The new_value of this TextReplace.
        :type: str
        """
        if new_value is None:
            raise ValueError("Invalid value for `new_value`, must not be `None`")

        self._new_value = new_value

    @property
    def regex(self):
        """
        Gets the regex of this TextReplace.
        Gets or sets a value indicating whether search text is regular expression.

        :return: The regex of this TextReplace.
        :rtype: bool
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """
        Sets the regex of this TextReplace.
        Gets or sets a value indicating whether search text is regular expression.

        :param regex: The regex of this TextReplace.
        :type: bool
        """
        if regex is None:
            raise ValueError("Invalid value for `regex`, must not be `None`")

        self._regex = regex

    @property
    def text_state(self):
        """
        Gets the text_state of this TextReplace.
        Text properties of a new text.

        :return: The text_state of this TextReplace.
        :rtype: TextState
        """
        return self._text_state

    @text_state.setter
    def text_state(self, text_state):
        """
        Sets the text_state of this TextReplace.
        Text properties of a new text.

        :param text_state: The text_state of this TextReplace.
        :type: TextState
        """

        self._text_state = text_state

    @property
    def rect(self):
        """
        Gets the rect of this TextReplace.
        Rectangle area where searched original text.

        :return: The rect of this TextReplace.
        :rtype: Rectangle
        """
        return self._rect

    @rect.setter
    def rect(self, rect):
        """
        Sets the rect of this TextReplace.
        Rectangle area where searched original text.

        :param rect: The rect of this TextReplace.
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
        if not isinstance(other, TextReplace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
