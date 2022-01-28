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


class TextRect(object):
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
        'text': 'str',
        'page': 'int',
        'rect': 'Rectangle',
        'horizontal_alignment': 'HorizontalAlignment',
        'vertical_alignment': 'VerticalAlignment',
        'position': 'Position',
        'baseline_position': 'Position',
        'text_state': 'TextState'
    }

    attribute_map = {
        'text': 'Text',
        'page': 'Page',
        'rect': 'Rect',
        'horizontal_alignment': 'HorizontalAlignment',
        'vertical_alignment': 'VerticalAlignment',
        'position': 'Position',
        'baseline_position': 'BaselinePosition',
        'text_state': 'TextState'
    }

    def __init__(self, text=None, page=None, rect=None, horizontal_alignment=None, vertical_alignment=None, position=None, baseline_position=None, text_state=None):
        """
        TextRect - a model defined in Swagger
        """

        self._text = None
        self._page = None
        self._rect = None
        self._horizontal_alignment = None
        self._vertical_alignment = None
        self._position = None
        self._baseline_position = None
        self._text_state = None

        if text is not None:
          self.text = text
        if page is not None:
          self.page = page
        if rect is not None:
          self.rect = rect
        if horizontal_alignment is not None:
          self.horizontal_alignment = horizontal_alignment
        if vertical_alignment is not None:
          self.vertical_alignment = vertical_alignment
        if position is not None:
          self.position = position
        if baseline_position is not None:
          self.baseline_position = baseline_position
        if text_state is not None:
          self.text_state = text_state

    @property
    def text(self):
        """
        Gets the text of this TextRect.
        Text of the occurrence.

        :return: The text of this TextRect.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this TextRect.
        Text of the occurrence.

        :param text: The text of this TextRect.
        :type: str
        """

        self._text = text

    @property
    def page(self):
        """
        Gets the page of this TextRect.
        Page on which the occurrence is found.

        :return: The page of this TextRect.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this TextRect.
        Page on which the occurrence is found.

        :param page: The page of this TextRect.
        :type: int
        """

        self._page = page

    @property
    def rect(self):
        """
        Gets the rect of this TextRect.
        Rectangle of the occurrence.

        :return: The rect of this TextRect.
        :rtype: Rectangle
        """
        return self._rect

    @rect.setter
    def rect(self, rect):
        """
        Sets the rect of this TextRect.
        Rectangle of the occurrence.

        :param rect: The rect of this TextRect.
        :type: Rectangle
        """

        self._rect = rect

    @property
    def horizontal_alignment(self):
        """
        Gets the horizontal_alignment of this TextRect.
        Gets or sets a horizontal alignment of text fragment. 

        :return: The horizontal_alignment of this TextRect.
        :rtype: HorizontalAlignment
        """
        return self._horizontal_alignment

    @horizontal_alignment.setter
    def horizontal_alignment(self, horizontal_alignment):
        """
        Sets the horizontal_alignment of this TextRect.
        Gets or sets a horizontal alignment of text fragment. 

        :param horizontal_alignment: The horizontal_alignment of this TextRect.
        :type: HorizontalAlignment
        """

        self._horizontal_alignment = horizontal_alignment

    @property
    def vertical_alignment(self):
        """
        Gets the vertical_alignment of this TextRect.
        Gets or sets a vertical alignment of text fragment. 

        :return: The vertical_alignment of this TextRect.
        :rtype: VerticalAlignment
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """
        Sets the vertical_alignment of this TextRect.
        Gets or sets a vertical alignment of text fragment. 

        :param vertical_alignment: The vertical_alignment of this TextRect.
        :type: VerticalAlignment
        """

        self._vertical_alignment = vertical_alignment

    @property
    def position(self):
        """
        Gets the position of this TextRect.
        Gets or sets text position for text, represented with TextRect object.

        :return: The position of this TextRect.
        :rtype: Position
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this TextRect.
        Gets or sets text position for text, represented with TextRect object.

        :param position: The position of this TextRect.
        :type: Position
        """

        self._position = position

    @property
    def baseline_position(self):
        """
        Gets the baseline_position of this TextRect.
        Gets text position for text, represented with TextRect object. The YIndent of the Position structure represents baseline coordinate of the text fragment.

        :return: The baseline_position of this TextRect.
        :rtype: Position
        """
        return self._baseline_position

    @baseline_position.setter
    def baseline_position(self, baseline_position):
        """
        Sets the baseline_position of this TextRect.
        Gets text position for text, represented with TextRect object. The YIndent of the Position structure represents baseline coordinate of the text fragment.

        :param baseline_position: The baseline_position of this TextRect.
        :type: Position
        """

        self._baseline_position = baseline_position

    @property
    def text_state(self):
        """
        Gets the text_state of this TextRect.
        Gets or sets text state for the text that TextRect object represents.

        :return: The text_state of this TextRect.
        :rtype: TextState
        """
        return self._text_state

    @text_state.setter
    def text_state(self, text_state):
        """
        Sets the text_state of this TextRect.
        Gets or sets text state for the text that TextRect object represents.

        :param text_state: The text_state of this TextRect.
        :type: TextState
        """

        self._text_state = text_state

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
        if not isinstance(other, TextRect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
