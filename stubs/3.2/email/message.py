# Stubs for email.message (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Undefined, Any

class Message:
    policy = Undefined(Any)
    preamble = Undefined(Any)
    defects = Undefined(Any)
    def __init__(self, policy=Undefined): pass
    def as_string(self, unixfrom=False, maxheaderlen=0, policy=None): pass
    def __bytes__(self): pass
    def as_bytes(self, unixfrom=False, policy=None): pass
    def is_multipart(self): pass
    def set_unixfrom(self, unixfrom): pass
    def get_unixfrom(self): pass
    def attach(self, payload): pass
    def get_payload(self, i=None, decode=False): pass
    def set_payload(self, payload, charset=None): pass
    def set_charset(self, charset): pass
    def get_charset(self): pass
    def __len__(self): pass
    def __getitem__(self, name): pass
    def __setitem__(self, name, val): pass
    def __delitem__(self, name): pass
    def __contains__(self, name): pass
    def __iter__(self): pass
    def keys(self): pass
    def values(self): pass
    def items(self): pass
    def get(self, name, failobj=None): pass
    def set_raw(self, name, value): pass
    def raw_items(self): pass
    def get_all(self, name, failobj=None): pass
    def add_header(self, _name, _value, **_params): pass
    def replace_header(self, _name, _value): pass
    def get_content_type(self): pass
    def get_content_maintype(self): pass
    def get_content_subtype(self): pass
    def get_default_type(self): pass
    def set_default_type(self, ctype): pass
    def get_params(self, failobj=None, header='', unquote=True): pass
    def get_param(self, param, failobj=None, header='', unquote=True): pass
    def set_param(self, param, value, header='', requote=True, charset=None, language='',
                  replace=False): pass
    def del_param(self, param, header='', requote=True): pass
    def set_type(self, type, header='', requote=True): pass
    def get_filename(self, failobj=None): pass
    def get_boundary(self, failobj=None): pass
    def set_boundary(self, boundary): pass
    def get_content_charset(self, failobj=None): pass
    def get_charsets(self, failobj=None): pass

class MIMEPart(Message):
    def __init__(self, policy=None): pass
    @property
    def is_attachment(self): pass
    def get_body(self, preferencelist=Undefined): pass
    def iter_attachments(self): pass
    def iter_parts(self): pass
    def get_content(self, *args, *, content_manager=None, **kw): pass
    def set_content(self, *args, *, content_manager=None, **kw): pass
    def make_related(self, boundary=None): pass
    def make_alternative(self, boundary=None): pass
    def make_mixed(self, boundary=None): pass
    def add_related(self, *args, **kw): pass
    def add_alternative(self, *args, **kw): pass
    def add_attachment(self, *args, **kw): pass
    def clear(self): pass
    def clear_content(self): pass

class EmailMessage(MIMEPart):
    def set_content(self, *args, **kw): pass
