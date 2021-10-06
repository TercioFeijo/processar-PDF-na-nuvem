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


class DisplayProperties(object):
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
        'center_window': 'bool',
        'direction': 'Direction',
        'display_doc_title': 'bool',
        'hide_menu_bar': 'bool',
        'hide_tool_bar': 'bool',
        'hide_window_ui': 'bool',
        'non_full_screen_page_mode': 'PageMode',
        'page_layout': 'PageLayout',
        'page_mode': 'PageMode'
    }

    attribute_map = {
        'links': 'Links',
        'center_window': 'CenterWindow',
        'direction': 'Direction',
        'display_doc_title': 'DisplayDocTitle',
        'hide_menu_bar': 'HideMenuBar',
        'hide_tool_bar': 'HideToolBar',
        'hide_window_ui': 'HideWindowUI',
        'non_full_screen_page_mode': 'NonFullScreenPageMode',
        'page_layout': 'PageLayout',
        'page_mode': 'PageMode'
    }

    def __init__(self, links=None, center_window=None, direction=None, display_doc_title=None, hide_menu_bar=None, hide_tool_bar=None, hide_window_ui=None, non_full_screen_page_mode=None, page_layout=None, page_mode=None):
        """
        DisplayProperties - a model defined in Swagger
        """

        self._links = None
        self._center_window = None
        self._direction = None
        self._display_doc_title = None
        self._hide_menu_bar = None
        self._hide_tool_bar = None
        self._hide_window_ui = None
        self._non_full_screen_page_mode = None
        self._page_layout = None
        self._page_mode = None

        if links is not None:
          self.links = links
        if center_window is not None:
          self.center_window = center_window
        if direction is not None:
          self.direction = direction
        if display_doc_title is not None:
          self.display_doc_title = display_doc_title
        if hide_menu_bar is not None:
          self.hide_menu_bar = hide_menu_bar
        if hide_tool_bar is not None:
          self.hide_tool_bar = hide_tool_bar
        if hide_window_ui is not None:
          self.hide_window_ui = hide_window_ui
        if non_full_screen_page_mode is not None:
          self.non_full_screen_page_mode = non_full_screen_page_mode
        if page_layout is not None:
          self.page_layout = page_layout
        if page_mode is not None:
          self.page_mode = page_mode

    @property
    def links(self):
        """
        Gets the links of this DisplayProperties.
        Link to the document.

        :return: The links of this DisplayProperties.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this DisplayProperties.
        Link to the document.

        :param links: The links of this DisplayProperties.
        :type: list[Link]
        """

        self._links = links

    @property
    def center_window(self):
        """
        Gets the center_window of this DisplayProperties.
        Gets or sets flag specifying whether position of the document's window will be centerd on the screen.

        :return: The center_window of this DisplayProperties.
        :rtype: bool
        """
        return self._center_window

    @center_window.setter
    def center_window(self, center_window):
        """
        Sets the center_window of this DisplayProperties.
        Gets or sets flag specifying whether position of the document's window will be centerd on the screen.

        :param center_window: The center_window of this DisplayProperties.
        :type: bool
        """

        self._center_window = center_window

    @property
    def direction(self):
        """
        Gets the direction of this DisplayProperties.
        Gets or sets reading order of text: L2R (left to right) or R2L (right to left).

        :return: The direction of this DisplayProperties.
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this DisplayProperties.
        Gets or sets reading order of text: L2R (left to right) or R2L (right to left).

        :param direction: The direction of this DisplayProperties.
        :type: Direction
        """

        self._direction = direction

    @property
    def display_doc_title(self):
        """
        Gets the display_doc_title of this DisplayProperties.
        Gets or sets flag specifying whether document's window title bar should display document title.

        :return: The display_doc_title of this DisplayProperties.
        :rtype: bool
        """
        return self._display_doc_title

    @display_doc_title.setter
    def display_doc_title(self, display_doc_title):
        """
        Sets the display_doc_title of this DisplayProperties.
        Gets or sets flag specifying whether document's window title bar should display document title.

        :param display_doc_title: The display_doc_title of this DisplayProperties.
        :type: bool
        """

        self._display_doc_title = display_doc_title

    @property
    def hide_menu_bar(self):
        """
        Gets the hide_menu_bar of this DisplayProperties.
        Gets or sets flag specifying whether menu bar should be hidden when document is active.

        :return: The hide_menu_bar of this DisplayProperties.
        :rtype: bool
        """
        return self._hide_menu_bar

    @hide_menu_bar.setter
    def hide_menu_bar(self, hide_menu_bar):
        """
        Sets the hide_menu_bar of this DisplayProperties.
        Gets or sets flag specifying whether menu bar should be hidden when document is active.

        :param hide_menu_bar: The hide_menu_bar of this DisplayProperties.
        :type: bool
        """

        self._hide_menu_bar = hide_menu_bar

    @property
    def hide_tool_bar(self):
        """
        Gets the hide_tool_bar of this DisplayProperties.
        Gets or sets flag specifying whether toolbar should be hidden when document is active.

        :return: The hide_tool_bar of this DisplayProperties.
        :rtype: bool
        """
        return self._hide_tool_bar

    @hide_tool_bar.setter
    def hide_tool_bar(self, hide_tool_bar):
        """
        Sets the hide_tool_bar of this DisplayProperties.
        Gets or sets flag specifying whether toolbar should be hidden when document is active.

        :param hide_tool_bar: The hide_tool_bar of this DisplayProperties.
        :type: bool
        """

        self._hide_tool_bar = hide_tool_bar

    @property
    def hide_window_ui(self):
        """
        Gets the hide_window_ui of this DisplayProperties.
        Gets or sets flag specifying whether user interface elements should be hidden when document is active.

        :return: The hide_window_ui of this DisplayProperties.
        :rtype: bool
        """
        return self._hide_window_ui

    @hide_window_ui.setter
    def hide_window_ui(self, hide_window_ui):
        """
        Sets the hide_window_ui of this DisplayProperties.
        Gets or sets flag specifying whether user interface elements should be hidden when document is active.

        :param hide_window_ui: The hide_window_ui of this DisplayProperties.
        :type: bool
        """

        self._hide_window_ui = hide_window_ui

    @property
    def non_full_screen_page_mode(self):
        """
        Gets the non_full_screen_page_mode of this DisplayProperties.
        Gets or sets page mode, specifying how to display the document on exiting full-screen mode.

        :return: The non_full_screen_page_mode of this DisplayProperties.
        :rtype: PageMode
        """
        return self._non_full_screen_page_mode

    @non_full_screen_page_mode.setter
    def non_full_screen_page_mode(self, non_full_screen_page_mode):
        """
        Sets the non_full_screen_page_mode of this DisplayProperties.
        Gets or sets page mode, specifying how to display the document on exiting full-screen mode.

        :param non_full_screen_page_mode: The non_full_screen_page_mode of this DisplayProperties.
        :type: PageMode
        """

        self._non_full_screen_page_mode = non_full_screen_page_mode

    @property
    def page_layout(self):
        """
        Gets the page_layout of this DisplayProperties.
        Gets or sets page layout which shall be used when the document is opened.

        :return: The page_layout of this DisplayProperties.
        :rtype: PageLayout
        """
        return self._page_layout

    @page_layout.setter
    def page_layout(self, page_layout):
        """
        Sets the page_layout of this DisplayProperties.
        Gets or sets page layout which shall be used when the document is opened.

        :param page_layout: The page_layout of this DisplayProperties.
        :type: PageLayout
        """

        self._page_layout = page_layout

    @property
    def page_mode(self):
        """
        Gets the page_mode of this DisplayProperties.
        Gets or sets page mode, specifying how document should be displayed when opened.

        :return: The page_mode of this DisplayProperties.
        :rtype: PageMode
        """
        return self._page_mode

    @page_mode.setter
    def page_mode(self, page_mode):
        """
        Sets the page_mode of this DisplayProperties.
        Gets or sets page mode, specifying how document should be displayed when opened.

        :param page_mode: The page_mode of this DisplayProperties.
        :type: PageMode
        """

        self._page_mode = page_mode

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
        if not isinstance(other, DisplayProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
