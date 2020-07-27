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


class OptimizeOptions(object):
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
        'allow_reuse_page_content': 'bool',
        'compress_images': 'bool',
        'image_quality': 'int',
        'link_duplcate_streams': 'bool',
        'remove_unused_objects': 'bool',
        'remove_unused_streams': 'bool',
        'unembed_fonts': 'bool',
        'resize_images': 'bool',
        'max_resolution': 'int',
        'subset_fonts': 'bool',
        'remove_private_info': 'bool',
        'image_encoding': 'ImageEncoding',
        'image_compression_version': 'ImageCompressionVersion'
    }

    attribute_map = {
        'allow_reuse_page_content': 'AllowReusePageContent',
        'compress_images': 'CompressImages',
        'image_quality': 'ImageQuality',
        'link_duplcate_streams': 'LinkDuplcateStreams',
        'remove_unused_objects': 'RemoveUnusedObjects',
        'remove_unused_streams': 'RemoveUnusedStreams',
        'unembed_fonts': 'UnembedFonts',
        'resize_images': 'ResizeImages',
        'max_resolution': 'MaxResolution',
        'subset_fonts': 'SubsetFonts',
        'remove_private_info': 'RemovePrivateInfo',
        'image_encoding': 'ImageEncoding',
        'image_compression_version': 'ImageCompressionVersion'
    }

    def __init__(self, allow_reuse_page_content=None, compress_images=None, image_quality=None, link_duplcate_streams=None, remove_unused_objects=None, remove_unused_streams=None, unembed_fonts=None, resize_images=None, max_resolution=None, subset_fonts=None, remove_private_info=None, image_encoding=None, image_compression_version=None):
        """
        OptimizeOptions - a model defined in Swagger
        """

        self._allow_reuse_page_content = None
        self._compress_images = None
        self._image_quality = None
        self._link_duplcate_streams = None
        self._remove_unused_objects = None
        self._remove_unused_streams = None
        self._unembed_fonts = None
        self._resize_images = None
        self._max_resolution = None
        self._subset_fonts = None
        self._remove_private_info = None
        self._image_encoding = None
        self._image_compression_version = None

        if allow_reuse_page_content is not None:
          self.allow_reuse_page_content = allow_reuse_page_content
        if compress_images is not None:
          self.compress_images = compress_images
        if image_quality is not None:
          self.image_quality = image_quality
        if link_duplcate_streams is not None:
          self.link_duplcate_streams = link_duplcate_streams
        if remove_unused_objects is not None:
          self.remove_unused_objects = remove_unused_objects
        if remove_unused_streams is not None:
          self.remove_unused_streams = remove_unused_streams
        if unembed_fonts is not None:
          self.unembed_fonts = unembed_fonts
        if resize_images is not None:
          self.resize_images = resize_images
        if max_resolution is not None:
          self.max_resolution = max_resolution
        if subset_fonts is not None:
          self.subset_fonts = subset_fonts
        if remove_private_info is not None:
          self.remove_private_info = remove_private_info
        if image_encoding is not None:
          self.image_encoding = image_encoding
        if image_compression_version is not None:
          self.image_compression_version = image_compression_version

    @property
    def allow_reuse_page_content(self):
        """
        Gets the allow_reuse_page_content of this OptimizeOptions.
        If true page contents will be reused when document is optimized for equal pages.

        :return: The allow_reuse_page_content of this OptimizeOptions.
        :rtype: bool
        """
        return self._allow_reuse_page_content

    @allow_reuse_page_content.setter
    def allow_reuse_page_content(self, allow_reuse_page_content):
        """
        Sets the allow_reuse_page_content of this OptimizeOptions.
        If true page contents will be reused when document is optimized for equal pages.

        :param allow_reuse_page_content: The allow_reuse_page_content of this OptimizeOptions.
        :type: bool
        """

        self._allow_reuse_page_content = allow_reuse_page_content

    @property
    def compress_images(self):
        """
        Gets the compress_images of this OptimizeOptions.
        If this flag is set to true images will be compressed in the document. Compression level is specified with ImageQuality property.

        :return: The compress_images of this OptimizeOptions.
        :rtype: bool
        """
        return self._compress_images

    @compress_images.setter
    def compress_images(self, compress_images):
        """
        Sets the compress_images of this OptimizeOptions.
        If this flag is set to true images will be compressed in the document. Compression level is specified with ImageQuality property.

        :param compress_images: The compress_images of this OptimizeOptions.
        :type: bool
        """

        self._compress_images = compress_images

    @property
    def image_quality(self):
        """
        Gets the image_quality of this OptimizeOptions.
        Specifies level of image compression when CompressImages flag is used.

        :return: The image_quality of this OptimizeOptions.
        :rtype: int
        """
        return self._image_quality

    @image_quality.setter
    def image_quality(self, image_quality):
        """
        Sets the image_quality of this OptimizeOptions.
        Specifies level of image compression when CompressImages flag is used.

        :param image_quality: The image_quality of this OptimizeOptions.
        :type: int
        """

        self._image_quality = image_quality

    @property
    def link_duplcate_streams(self):
        """
        Gets the link_duplcate_streams of this OptimizeOptions.
        If this flag is set to true, Resource streams will be analyzed. If duplicate streams are found (i.e. if stream contents is equal), then thees streams will be stored as one object.  This allows to decrease document size in some cases (for example, when same document was concatenated multiple times).

        :return: The link_duplcate_streams of this OptimizeOptions.
        :rtype: bool
        """
        return self._link_duplcate_streams

    @link_duplcate_streams.setter
    def link_duplcate_streams(self, link_duplcate_streams):
        """
        Sets the link_duplcate_streams of this OptimizeOptions.
        If this flag is set to true, Resource streams will be analyzed. If duplicate streams are found (i.e. if stream contents is equal), then thees streams will be stored as one object.  This allows to decrease document size in some cases (for example, when same document was concatenated multiple times).

        :param link_duplcate_streams: The link_duplcate_streams of this OptimizeOptions.
        :type: bool
        """

        self._link_duplcate_streams = link_duplcate_streams

    @property
    def remove_unused_objects(self):
        """
        Gets the remove_unused_objects of this OptimizeOptions.
        If this flag is set to true, all document objects will be checked and unused objects (i.e. objects which does not have any reference) are removed from document.

        :return: The remove_unused_objects of this OptimizeOptions.
        :rtype: bool
        """
        return self._remove_unused_objects

    @remove_unused_objects.setter
    def remove_unused_objects(self, remove_unused_objects):
        """
        Sets the remove_unused_objects of this OptimizeOptions.
        If this flag is set to true, all document objects will be checked and unused objects (i.e. objects which does not have any reference) are removed from document.

        :param remove_unused_objects: The remove_unused_objects of this OptimizeOptions.
        :type: bool
        """

        self._remove_unused_objects = remove_unused_objects

    @property
    def remove_unused_streams(self):
        """
        Gets the remove_unused_streams of this OptimizeOptions.
        If this flag set to true, every resource is checked on it's usage. If resource is never used, then resources is removed. This may decrease document size for example when pages were extracted from document. 

        :return: The remove_unused_streams of this OptimizeOptions.
        :rtype: bool
        """
        return self._remove_unused_streams

    @remove_unused_streams.setter
    def remove_unused_streams(self, remove_unused_streams):
        """
        Sets the remove_unused_streams of this OptimizeOptions.
        If this flag set to true, every resource is checked on it's usage. If resource is never used, then resources is removed. This may decrease document size for example when pages were extracted from document. 

        :param remove_unused_streams: The remove_unused_streams of this OptimizeOptions.
        :type: bool
        """

        self._remove_unused_streams = remove_unused_streams

    @property
    def unembed_fonts(self):
        """
        Gets the unembed_fonts of this OptimizeOptions.
        Make fonts not embedded if set to true. 

        :return: The unembed_fonts of this OptimizeOptions.
        :rtype: bool
        """
        return self._unembed_fonts

    @unembed_fonts.setter
    def unembed_fonts(self, unembed_fonts):
        """
        Sets the unembed_fonts of this OptimizeOptions.
        Make fonts not embedded if set to true. 

        :param unembed_fonts: The unembed_fonts of this OptimizeOptions.
        :type: bool
        """

        self._unembed_fonts = unembed_fonts

    @property
    def resize_images(self):
        """
        Gets the resize_images of this OptimizeOptions.
        If this flag set to true and CompressImages is true images will be resized if image resolution is greater then specified MaxResolution parameter.

        :return: The resize_images of this OptimizeOptions.
        :rtype: bool
        """
        return self._resize_images

    @resize_images.setter
    def resize_images(self, resize_images):
        """
        Sets the resize_images of this OptimizeOptions.
        If this flag set to true and CompressImages is true images will be resized if image resolution is greater then specified MaxResolution parameter.

        :param resize_images: The resize_images of this OptimizeOptions.
        :type: bool
        """

        self._resize_images = resize_images

    @property
    def max_resolution(self):
        """
        Gets the max_resolution of this OptimizeOptions.
        Specifies maximum resolution of images. If image has higher resolution it will be scaled.

        :return: The max_resolution of this OptimizeOptions.
        :rtype: int
        """
        return self._max_resolution

    @max_resolution.setter
    def max_resolution(self, max_resolution):
        """
        Sets the max_resolution of this OptimizeOptions.
        Specifies maximum resolution of images. If image has higher resolution it will be scaled.

        :param max_resolution: The max_resolution of this OptimizeOptions.
        :type: int
        """

        self._max_resolution = max_resolution

    @property
    def subset_fonts(self):
        """
        Gets the subset_fonts of this OptimizeOptions.
        Fonts will be converted into subsets if set to true.

        :return: The subset_fonts of this OptimizeOptions.
        :rtype: bool
        """
        return self._subset_fonts

    @subset_fonts.setter
    def subset_fonts(self, subset_fonts):
        """
        Sets the subset_fonts of this OptimizeOptions.
        Fonts will be converted into subsets if set to true.

        :param subset_fonts: The subset_fonts of this OptimizeOptions.
        :type: bool
        """

        self._subset_fonts = subset_fonts

    @property
    def remove_private_info(self):
        """
        Gets the remove_private_info of this OptimizeOptions.
        Remove private information (page piece info).

        :return: The remove_private_info of this OptimizeOptions.
        :rtype: bool
        """
        return self._remove_private_info

    @remove_private_info.setter
    def remove_private_info(self, remove_private_info):
        """
        Sets the remove_private_info of this OptimizeOptions.
        Remove private information (page piece info).

        :param remove_private_info: The remove_private_info of this OptimizeOptions.
        :type: bool
        """

        self._remove_private_info = remove_private_info

    @property
    def image_encoding(self):
        """
        Gets the image_encoding of this OptimizeOptions.
        Image encode which will be used.

        :return: The image_encoding of this OptimizeOptions.
        :rtype: ImageEncoding
        """
        return self._image_encoding

    @image_encoding.setter
    def image_encoding(self, image_encoding):
        """
        Sets the image_encoding of this OptimizeOptions.
        Image encode which will be used.

        :param image_encoding: The image_encoding of this OptimizeOptions.
        :type: ImageEncoding
        """

        self._image_encoding = image_encoding

    @property
    def image_compression_version(self):
        """
        Gets the image_compression_version of this OptimizeOptions.
        Version of compression algorithm. Possible values are: \"Standard\" - standard compression, \"Fast\" - fast (improved compression which is faster then standard but may be applicable not for all images), \"Mixed\" - mixed (standard compression is applied to images which can not be compressed by  faster algorithm, this may give best compression but more slow then \"Fast\" algorithm. Version \"Fast\" is not applicable for resizing images (standard method will be used). Default is \"Standard\".

        :return: The image_compression_version of this OptimizeOptions.
        :rtype: ImageCompressionVersion
        """
        return self._image_compression_version

    @image_compression_version.setter
    def image_compression_version(self, image_compression_version):
        """
        Sets the image_compression_version of this OptimizeOptions.
        Version of compression algorithm. Possible values are: \"Standard\" - standard compression, \"Fast\" - fast (improved compression which is faster then standard but may be applicable not for all images), \"Mixed\" - mixed (standard compression is applied to images which can not be compressed by  faster algorithm, this may give best compression but more slow then \"Fast\" algorithm. Version \"Fast\" is not applicable for resizing images (standard method will be used). Default is \"Standard\".

        :param image_compression_version: The image_compression_version of this OptimizeOptions.
        :type: ImageCompressionVersion
        """

        self._image_compression_version = image_compression_version

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
        if not isinstance(other, OptimizeOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
