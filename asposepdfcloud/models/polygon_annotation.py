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


class PolygonAnnotation(object):
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
        'color': 'Color',
        'contents': 'str',
        'modified': 'str',
        'id': 'str',
        'flags': 'list[AnnotationFlags]',
        'name': 'str',
        'rect': 'Rectangle',
        'page_index': 'int',
        'z_index': 'int',
        'horizontal_alignment': 'HorizontalAlignment',
        'vertical_alignment': 'VerticalAlignment',
        'creation_date': 'str',
        'subject': 'str',
        'title': 'str',
        'rich_text': 'str',
        'interior_color': 'Color',
        'starting_style': 'LineEnding',
        'ending_style': 'LineEnding',
        'intent': 'PolyIntent',
        'vertices': 'list[Point]'
    }

    attribute_map = {
        'links': 'Links',
        'color': 'Color',
        'contents': 'Contents',
        'modified': 'Modified',
        'id': 'Id',
        'flags': 'Flags',
        'name': 'Name',
        'rect': 'Rect',
        'page_index': 'PageIndex',
        'z_index': 'ZIndex',
        'horizontal_alignment': 'HorizontalAlignment',
        'vertical_alignment': 'VerticalAlignment',
        'creation_date': 'CreationDate',
        'subject': 'Subject',
        'title': 'Title',
        'rich_text': 'RichText',
        'interior_color': 'InteriorColor',
        'starting_style': 'StartingStyle',
        'ending_style': 'EndingStyle',
        'intent': 'Intent',
        'vertices': 'Vertices'
    }

    def __init__(self, links=None, color=None, contents=None, modified=None, id=None, flags=None, name=None, rect=None, page_index=None, z_index=None, horizontal_alignment=None, vertical_alignment=None, creation_date=None, subject=None, title=None, rich_text=None, interior_color=None, starting_style=None, ending_style=None, intent=None, vertices=None):
        """
        PolygonAnnotation - a model defined in Swagger
        """

        self._links = None
        self._color = None
        self._contents = None
        self._modified = None
        self._id = None
        self._flags = None
        self._name = None
        self._rect = None
        self._page_index = None
        self._z_index = None
        self._horizontal_alignment = None
        self._vertical_alignment = None
        self._creation_date = None
        self._subject = None
        self._title = None
        self._rich_text = None
        self._interior_color = None
        self._starting_style = None
        self._ending_style = None
        self._intent = None
        self._vertices = None

        if links is not None:
          self.links = links
        if color is not None:
          self.color = color
        if contents is not None:
          self.contents = contents
        if modified is not None:
          self.modified = modified
        if id is not None:
          self.id = id
        if flags is not None:
          self.flags = flags
        if name is not None:
          self.name = name
        self.rect = rect
        if page_index is not None:
          self.page_index = page_index
        if z_index is not None:
          self.z_index = z_index
        if horizontal_alignment is not None:
          self.horizontal_alignment = horizontal_alignment
        if vertical_alignment is not None:
          self.vertical_alignment = vertical_alignment
        if creation_date is not None:
          self.creation_date = creation_date
        if subject is not None:
          self.subject = subject
        if title is not None:
          self.title = title
        if rich_text is not None:
          self.rich_text = rich_text
        if interior_color is not None:
          self.interior_color = interior_color
        if starting_style is not None:
          self.starting_style = starting_style
        if ending_style is not None:
          self.ending_style = ending_style
        if intent is not None:
          self.intent = intent
        self.vertices = vertices

    @property
    def links(self):
        """
        Gets the links of this PolygonAnnotation.
        Link to the document.

        :return: The links of this PolygonAnnotation.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PolygonAnnotation.
        Link to the document.

        :param links: The links of this PolygonAnnotation.
        :type: list[Link]
        """

        self._links = links

    @property
    def color(self):
        """
        Gets the color of this PolygonAnnotation.
        Color of the annotation.

        :return: The color of this PolygonAnnotation.
        :rtype: Color
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this PolygonAnnotation.
        Color of the annotation.

        :param color: The color of this PolygonAnnotation.
        :type: Color
        """

        self._color = color

    @property
    def contents(self):
        """
        Gets the contents of this PolygonAnnotation.
        Get the annotation content.

        :return: The contents of this PolygonAnnotation.
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """
        Sets the contents of this PolygonAnnotation.
        Get the annotation content.

        :param contents: The contents of this PolygonAnnotation.
        :type: str
        """

        self._contents = contents

    @property
    def modified(self):
        """
        Gets the modified of this PolygonAnnotation.
        The date and time when the annotation was last modified.

        :return: The modified of this PolygonAnnotation.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this PolygonAnnotation.
        The date and time when the annotation was last modified.

        :param modified: The modified of this PolygonAnnotation.
        :type: str
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this PolygonAnnotation.
        Gets ID of the annotation.

        :return: The id of this PolygonAnnotation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PolygonAnnotation.
        Gets ID of the annotation.

        :param id: The id of this PolygonAnnotation.
        :type: str
        """

        self._id = id

    @property
    def flags(self):
        """
        Gets the flags of this PolygonAnnotation.
        Gets Flags of the annotation.

        :return: The flags of this PolygonAnnotation.
        :rtype: list[AnnotationFlags]
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """
        Sets the flags of this PolygonAnnotation.
        Gets Flags of the annotation.

        :param flags: The flags of this PolygonAnnotation.
        :type: list[AnnotationFlags]
        """

        self._flags = flags

    @property
    def name(self):
        """
        Gets the name of this PolygonAnnotation.
        Gets Name of the annotation.

        :return: The name of this PolygonAnnotation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolygonAnnotation.
        Gets Name of the annotation.

        :param name: The name of this PolygonAnnotation.
        :type: str
        """

        self._name = name

    @property
    def rect(self):
        """
        Gets the rect of this PolygonAnnotation.
        Gets Rect of the annotation.

        :return: The rect of this PolygonAnnotation.
        :rtype: Rectangle
        """
        return self._rect

    @rect.setter
    def rect(self, rect):
        """
        Sets the rect of this PolygonAnnotation.
        Gets Rect of the annotation.

        :param rect: The rect of this PolygonAnnotation.
        :type: Rectangle
        """
        if rect is None:
            raise ValueError("Invalid value for `rect`, must not be `None`")

        self._rect = rect

    @property
    def page_index(self):
        """
        Gets the page_index of this PolygonAnnotation.
        Gets PageIndex of the annotation.

        :return: The page_index of this PolygonAnnotation.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this PolygonAnnotation.
        Gets PageIndex of the annotation.

        :param page_index: The page_index of this PolygonAnnotation.
        :type: int
        """

        self._page_index = page_index

    @property
    def z_index(self):
        """
        Gets the z_index of this PolygonAnnotation.
        Gets ZIndex of the annotation.

        :return: The z_index of this PolygonAnnotation.
        :rtype: int
        """
        return self._z_index

    @z_index.setter
    def z_index(self, z_index):
        """
        Sets the z_index of this PolygonAnnotation.
        Gets ZIndex of the annotation.

        :param z_index: The z_index of this PolygonAnnotation.
        :type: int
        """

        self._z_index = z_index

    @property
    def horizontal_alignment(self):
        """
        Gets the horizontal_alignment of this PolygonAnnotation.
        Gets HorizontalAlignment of the annotation.

        :return: The horizontal_alignment of this PolygonAnnotation.
        :rtype: HorizontalAlignment
        """
        return self._horizontal_alignment

    @horizontal_alignment.setter
    def horizontal_alignment(self, horizontal_alignment):
        """
        Sets the horizontal_alignment of this PolygonAnnotation.
        Gets HorizontalAlignment of the annotation.

        :param horizontal_alignment: The horizontal_alignment of this PolygonAnnotation.
        :type: HorizontalAlignment
        """

        self._horizontal_alignment = horizontal_alignment

    @property
    def vertical_alignment(self):
        """
        Gets the vertical_alignment of this PolygonAnnotation.
        Gets VerticalAlignment of the annotation.

        :return: The vertical_alignment of this PolygonAnnotation.
        :rtype: VerticalAlignment
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """
        Sets the vertical_alignment of this PolygonAnnotation.
        Gets VerticalAlignment of the annotation.

        :param vertical_alignment: The vertical_alignment of this PolygonAnnotation.
        :type: VerticalAlignment
        """

        self._vertical_alignment = vertical_alignment

    @property
    def creation_date(self):
        """
        Gets the creation_date of this PolygonAnnotation.
        The date and time when the annotation was created.

        :return: The creation_date of this PolygonAnnotation.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this PolygonAnnotation.
        The date and time when the annotation was created.

        :param creation_date: The creation_date of this PolygonAnnotation.
        :type: str
        """

        self._creation_date = creation_date

    @property
    def subject(self):
        """
        Gets the subject of this PolygonAnnotation.
        Get the annotation subject.

        :return: The subject of this PolygonAnnotation.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this PolygonAnnotation.
        Get the annotation subject.

        :param subject: The subject of this PolygonAnnotation.
        :type: str
        """

        self._subject = subject

    @property
    def title(self):
        """
        Gets the title of this PolygonAnnotation.
        Get the annotation title.

        :return: The title of this PolygonAnnotation.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this PolygonAnnotation.
        Get the annotation title.

        :param title: The title of this PolygonAnnotation.
        :type: str
        """

        self._title = title

    @property
    def rich_text(self):
        """
        Gets the rich_text of this PolygonAnnotation.
        Get the annotation RichText.

        :return: The rich_text of this PolygonAnnotation.
        :rtype: str
        """
        return self._rich_text

    @rich_text.setter
    def rich_text(self, rich_text):
        """
        Sets the rich_text of this PolygonAnnotation.
        Get the annotation RichText.

        :param rich_text: The rich_text of this PolygonAnnotation.
        :type: str
        """

        self._rich_text = rich_text

    @property
    def interior_color(self):
        """
        Gets the interior_color of this PolygonAnnotation.
        Gets or sets the interior color with which to fill the annotation’s line endings.

        :return: The interior_color of this PolygonAnnotation.
        :rtype: Color
        """
        return self._interior_color

    @interior_color.setter
    def interior_color(self, interior_color):
        """
        Sets the interior_color of this PolygonAnnotation.
        Gets or sets the interior color with which to fill the annotation’s line endings.

        :param interior_color: The interior_color of this PolygonAnnotation.
        :type: Color
        """

        self._interior_color = interior_color

    @property
    def starting_style(self):
        """
        Gets the starting_style of this PolygonAnnotation.
        Gets or sets the style of first line ending.

        :return: The starting_style of this PolygonAnnotation.
        :rtype: LineEnding
        """
        return self._starting_style

    @starting_style.setter
    def starting_style(self, starting_style):
        """
        Sets the starting_style of this PolygonAnnotation.
        Gets or sets the style of first line ending.

        :param starting_style: The starting_style of this PolygonAnnotation.
        :type: LineEnding
        """

        self._starting_style = starting_style

    @property
    def ending_style(self):
        """
        Gets the ending_style of this PolygonAnnotation.
        Gets or sets the style of second line ending.

        :return: The ending_style of this PolygonAnnotation.
        :rtype: LineEnding
        """
        return self._ending_style

    @ending_style.setter
    def ending_style(self, ending_style):
        """
        Sets the ending_style of this PolygonAnnotation.
        Gets or sets the style of second line ending.

        :param ending_style: The ending_style of this PolygonAnnotation.
        :type: LineEnding
        """

        self._ending_style = ending_style

    @property
    def intent(self):
        """
        Gets the intent of this PolygonAnnotation.
        Gets or sets the intent of the polygon or polyline annotation.

        :return: The intent of this PolygonAnnotation.
        :rtype: PolyIntent
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """
        Sets the intent of this PolygonAnnotation.
        Gets or sets the intent of the polygon or polyline annotation.

        :param intent: The intent of this PolygonAnnotation.
        :type: PolyIntent
        """

        self._intent = intent

    @property
    def vertices(self):
        """
        Gets the vertices of this PolygonAnnotation.
        Gets or sets an array of points representing the horizontal and vertical coordinates of each vertex.

        :return: The vertices of this PolygonAnnotation.
        :rtype: list[Point]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        """
        Sets the vertices of this PolygonAnnotation.
        Gets or sets an array of points representing the horizontal and vertical coordinates of each vertex.

        :param vertices: The vertices of this PolygonAnnotation.
        :type: list[Point]
        """
        if vertices is None:
            raise ValueError("Invalid value for `vertices`, must not be `None`")

        self._vertices = vertices

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
        if not isinstance(other, PolygonAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
