# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2019 Aspose.PDF Cloud
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



    OpenAPI spec version: 2.0
    
"""


from pprint import pformat
from six import iteritems
import re


class Signature(object):
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
        'signature_path': 'str',
        'signature_type': 'SignatureType',
        'password': 'str',
        'appearance': 'str',
        'reason': 'str',
        'contact': 'str',
        'location': 'str',
        'visible': 'bool',
        'rectangle': 'Rectangle',
        'form_field_name': 'str',
        'authority': 'str',
        'date': 'str',
        'show_properties': 'bool'
    }

    attribute_map = {
        'signature_path': 'SignaturePath',
        'signature_type': 'SignatureType',
        'password': 'Password',
        'appearance': 'Appearance',
        'reason': 'Reason',
        'contact': 'Contact',
        'location': 'Location',
        'visible': 'Visible',
        'rectangle': 'Rectangle',
        'form_field_name': 'FormFieldName',
        'authority': 'Authority',
        'date': 'Date',
        'show_properties': 'ShowProperties'
    }

    def __init__(self, signature_path=None, signature_type=None, password=None, appearance=None, reason=None, contact=None, location=None, visible=None, rectangle=None, form_field_name=None, authority=None, date=None, show_properties=None):
        """
        Signature - a model defined in Swagger
        """

        self._signature_path = None
        self._signature_type = None
        self._password = None
        self._appearance = None
        self._reason = None
        self._contact = None
        self._location = None
        self._visible = None
        self._rectangle = None
        self._form_field_name = None
        self._authority = None
        self._date = None
        self._show_properties = None

        self.signature_path = signature_path
        self.signature_type = signature_type
        if password is not None:
          self.password = password
        if appearance is not None:
          self.appearance = appearance
        if reason is not None:
          self.reason = reason
        if contact is not None:
          self.contact = contact
        if location is not None:
          self.location = location
        self.visible = visible
        if rectangle is not None:
          self.rectangle = rectangle
        if form_field_name is not None:
          self.form_field_name = form_field_name
        if authority is not None:
          self.authority = authority
        if date is not None:
          self.date = date
        self.show_properties = show_properties

    @property
    def signature_path(self):
        """
        Gets the signature_path of this Signature.
        Gets or sets the signature path.

        :return: The signature_path of this Signature.
        :rtype: str
        """
        return self._signature_path

    @signature_path.setter
    def signature_path(self, signature_path):
        """
        Sets the signature_path of this Signature.
        Gets or sets the signature path.

        :param signature_path: The signature_path of this Signature.
        :type: str
        """
        if signature_path is None:
            raise ValueError("Invalid value for `signature_path`, must not be `None`")

        self._signature_path = signature_path

    @property
    def signature_type(self):
        """
        Gets the signature_type of this Signature.
        Gets or sets the type of the signature.

        :return: The signature_type of this Signature.
        :rtype: SignatureType
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """
        Sets the signature_type of this Signature.
        Gets or sets the type of the signature.

        :param signature_type: The signature_type of this Signature.
        :type: SignatureType
        """
        if signature_type is None:
            raise ValueError("Invalid value for `signature_type`, must not be `None`")

        self._signature_type = signature_type

    @property
    def password(self):
        """
        Gets the password of this Signature.
        Gets or sets the signature password.

        :return: The password of this Signature.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this Signature.
        Gets or sets the signature password.

        :param password: The password of this Signature.
        :type: str
        """

        self._password = password

    @property
    def appearance(self):
        """
        Gets the appearance of this Signature.
        Sets or gets a graphic appearance for the signature. Property value represents an image file name.

        :return: The appearance of this Signature.
        :rtype: str
        """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance):
        """
        Sets the appearance of this Signature.
        Sets or gets a graphic appearance for the signature. Property value represents an image file name.

        :param appearance: The appearance of this Signature.
        :type: str
        """

        self._appearance = appearance

    @property
    def reason(self):
        """
        Gets the reason of this Signature.
        Gets or sets the reason of the signature.

        :return: The reason of this Signature.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this Signature.
        Gets or sets the reason of the signature.

        :param reason: The reason of this Signature.
        :type: str
        """

        self._reason = reason

    @property
    def contact(self):
        """
        Gets the contact of this Signature.
        Gets or sets the contact of the signature.

        :return: The contact of this Signature.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this Signature.
        Gets or sets the contact of the signature.

        :param contact: The contact of this Signature.
        :type: str
        """

        self._contact = contact

    @property
    def location(self):
        """
        Gets the location of this Signature.
        Gets or sets the location of the signature.

        :return: The location of this Signature.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Signature.
        Gets or sets the location of the signature.

        :param location: The location of this Signature.
        :type: str
        """

        self._location = location

    @property
    def visible(self):
        """
        Gets the visible of this Signature.
        Gets or sets a value indicating whether this  is visible. Supports only when signing particular page.

        :return: The visible of this Signature.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        Sets the visible of this Signature.
        Gets or sets a value indicating whether this  is visible. Supports only when signing particular page.

        :param visible: The visible of this Signature.
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")

        self._visible = visible

    @property
    def rectangle(self):
        """
        Gets the rectangle of this Signature.
        Gets or sets the visible rectangle of the signature. Supports only when signing particular page.

        :return: The rectangle of this Signature.
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle of this Signature.
        Gets or sets the visible rectangle of the signature. Supports only when signing particular page.

        :param rectangle: The rectangle of this Signature.
        :type: Rectangle
        """

        self._rectangle = rectangle

    @property
    def form_field_name(self):
        """
        Gets the form_field_name of this Signature.
        Gets or sets the name of the signature field. Supports only when signing document with particular form field.

        :return: The form_field_name of this Signature.
        :rtype: str
        """
        return self._form_field_name

    @form_field_name.setter
    def form_field_name(self, form_field_name):
        """
        Sets the form_field_name of this Signature.
        Gets or sets the name of the signature field. Supports only when signing document with particular form field.

        :param form_field_name: The form_field_name of this Signature.
        :type: str
        """

        self._form_field_name = form_field_name

    @property
    def authority(self):
        """
        Gets the authority of this Signature.
        Gets or sets the name of the person or authority signing the document..

        :return: The authority of this Signature.
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """
        Sets the authority of this Signature.
        Gets or sets the name of the person or authority signing the document..

        :param authority: The authority of this Signature.
        :type: str
        """

        self._authority = authority

    @property
    def date(self):
        """
        Gets the date of this Signature.
        Gets or sets the time of signing.

        :return: The date of this Signature.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this Signature.
        Gets or sets the time of signing.

        :param date: The date of this Signature.
        :type: str
        """

        self._date = date

    @property
    def show_properties(self):
        """
        Gets the show_properties of this Signature.
        Gets or sets the showproperties in signature field

        :return: The show_properties of this Signature.
        :rtype: bool
        """
        return self._show_properties

    @show_properties.setter
    def show_properties(self, show_properties):
        """
        Sets the show_properties of this Signature.
        Gets or sets the showproperties in signature field

        :param show_properties: The show_properties of this Signature.
        :type: bool
        """
        if show_properties is None:
            raise ValueError("Invalid value for `show_properties`, must not be `None`")

        self._show_properties = show_properties

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
        if not isinstance(other, Signature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
