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


class TextState(object):
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
        'font_size': 'float',
        'font': 'str',
        'foreground_color': 'Color',
        'background_color': 'Color',
        'font_style': 'FontStyles',
        'font_file': 'str'
    }

    attribute_map = {
        'font_size': 'FontSize',
        'font': 'Font',
        'foreground_color': 'ForegroundColor',
        'background_color': 'BackgroundColor',
        'font_style': 'FontStyle',
        'font_file': 'FontFile'
    }

    def __init__(self, font_size=None, font=None, foreground_color=None, background_color=None, font_style=None, font_file=None):
        """
        TextState - a model defined in Swagger
        """

        self._font_size = None
        self._font = None
        self._foreground_color = None
        self._background_color = None
        self._font_style = None
        self._font_file = None

        self.font_size = font_size
        if font is not None:
          self.font = font
        if foreground_color is not None:
          self.foreground_color = foreground_color
        if background_color is not None:
          self.background_color = background_color
        self.font_style = font_style
        if font_file is not None:
          self.font_file = font_file

    @property
    def font_size(self):
        """
        Gets the font_size of this TextState.
        Gets or sets font size of the text.

        :return: The font_size of this TextState.
        :rtype: float
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """
        Sets the font_size of this TextState.
        Gets or sets font size of the text.

        :param font_size: The font_size of this TextState.
        :type: float
        """
        if font_size is None:
            raise ValueError("Invalid value for `font_size`, must not be `None`")

        self._font_size = font_size

    @property
    def font(self):
        """
        Gets the font of this TextState.
        Gets or sets font name of the text.

        :return: The font of this TextState.
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """
        Sets the font of this TextState.
        Gets or sets font name of the text.

        :param font: The font of this TextState.
        :type: str
        """

        self._font = font

    @property
    def foreground_color(self):
        """
        Gets the foreground_color of this TextState.
        Gets or sets foreground color of the text.

        :return: The foreground_color of this TextState.
        :rtype: Color
        """
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, foreground_color):
        """
        Sets the foreground_color of this TextState.
        Gets or sets foreground color of the text.

        :param foreground_color: The foreground_color of this TextState.
        :type: Color
        """

        self._foreground_color = foreground_color

    @property
    def background_color(self):
        """
        Gets the background_color of this TextState.
        Sets background color of the text.

        :return: The background_color of this TextState.
        :rtype: Color
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this TextState.
        Sets background color of the text.

        :param background_color: The background_color of this TextState.
        :type: Color
        """

        self._background_color = background_color

    @property
    def font_style(self):
        """
        Gets the font_style of this TextState.
        Sets font style of the text.

        :return: The font_style of this TextState.
        :rtype: FontStyles
        """
        return self._font_style

    @font_style.setter
    def font_style(self, font_style):
        """
        Sets the font_style of this TextState.
        Sets font style of the text.

        :param font_style: The font_style of this TextState.
        :type: FontStyles
        """
        if font_style is None:
            raise ValueError("Invalid value for `font_style`, must not be `None`")

        self._font_style = font_style

    @property
    def font_file(self):
        """
        Gets the font_file of this TextState.
        Sets path of font file in storage.

        :return: The font_file of this TextState.
        :rtype: str
        """
        return self._font_file

    @font_file.setter
    def font_file(self, font_file):
        """
        Sets the font_file of this TextState.
        Sets path of font file in storage.

        :param font_file: The font_file of this TextState.
        :type: str
        """

        self._font_file = font_file

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
        if not isinstance(other, TextState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
