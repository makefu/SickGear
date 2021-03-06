# Stubs for tornado_py3.curl_httpclient (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tornado_py3.httpclient import AsyncHTTPClient, HTTPError, HTTPRequest, HTTPResponse
from typing import Any, Callable, Dict, Optional

curl_log: Any

class CurlAsyncHTTPClient(AsyncHTTPClient):
    def initialize(self, max_clients: int=..., defaults: Optional[Dict[str, Any]]=...) -> None: ...
    def close(self) -> None: ...
    def fetch_impl(self, request: HTTPRequest, callback: Callable[[HTTPResponse], None]) -> None: ...
    def handle_callback_exception(self, callback: Any) -> None: ...

class CurlError(HTTPError):
    errno: Any = ...
    def __init__(self, errno: int, message: str) -> None: ...
