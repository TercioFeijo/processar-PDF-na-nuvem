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


class WordCountResponse(object):
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
        'code': 'int',
        'status': 'str',
        'words_per_page': 'WordCount'
    }

    attribute_map = {
        'code': 'Code',
        'status': 'Status',
        'words_per_page': 'WordsPerPage'
    }

    def __init__(self, code=None, status=None, words_per_page=None):
        """
        WordCountResponse - a model defined in Swagger
        """

        self._code = None
        self._status = None
        self._words_per_page = None

        self.code = code
        if status is not None:
          self.status = status
        if words_per_page is not None:
          self.words_per_page = words_per_page

    @property
    def code(self):
        """
        Gets the code of this WordCountResponse.
        Response status code.

        :return: The code of this WordCountResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this WordCountResponse.
        Response status code.

        :param code: The code of this WordCountResponse.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def status(self):
        """
        Gets the status of this WordCountResponse.
        Response status.

        :return: The status of this WordCountResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WordCountResponse.
        Response status.

        :param status: The status of this WordCountResponse.
        :type: str
        """

        self._status = status

    @property
    def words_per_page(self):
        """
        Gets the words_per_page of this WordCountResponse.
        WordCount with words per page info.

        :return: The words_per_page of this WordCountResponse.
        :rtype: WordCount
        """
        return self._words_per_page

    @words_per_page.setter
    def words_per_page(self, words_per_page):
        """
        Sets the words_per_page of this WordCountResponse.
        WordCount with words per page info.

        :param words_per_page: The words_per_page of this WordCountResponse.
        :type: WordCount
        """

        self._words_per_page = words_per_page

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
        if not isinstance(other, WordCountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
