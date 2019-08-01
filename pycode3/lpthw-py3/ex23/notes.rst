encodings
=========
DBES - Decode bytes and encode strings

``str.encode`` function to get bytes from str
::

    Docstring:
    S.encode(encoding='utf-8', errors='strict') -> bytes

    Encode S using the codec registered for encoding. Default encoding
    is 'utf-8'. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle UnicodeEncodeErrors.
    Type:      method_descriptor

``bytes.decode`` function to get string from bytes
::

    Signature: bytes.decode(self, /, encoding='utf-8', errors='strict')
    Docstring:
    Decode the bytes using the codec registered for encoding.

    encoding
      The encoding with which to decode the bytes.
    errors
      The error handling scheme to use for the handling of decoding errors.
      The default is 'strict' meaning that decoding errors raise a
      UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
      as well as any other name registered with codecs.register_error that
      can handle UnicodeDecodeErrors.
    Type:      method_descriptor

