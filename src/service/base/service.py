import os

import tomodachi
from aiohttp import web
from tomodachi.transport.http import http, http_error

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class BaseService(tomodachi.Service):
    options = {
        "http": {
            "port": 80,
            "content_type": "application/json",
            "charset": "utf-8",
            "access_log": os.path.join(ROOT_PATH, "logs", "access.log"),
        }
    }

    @http(("GET", "POST"), r"/health/?", ignore_logging=[200])
    async def http_health_check(self, request: web.Request) -> web.Response:
        return web.json_response({"status": "ok"}, status=200)

    @http_error(status_code=403)
    async def http_error_403(self, request: web.Request) -> web.Response:
        return web.json_response({"status": "invalid credentials"}, status=403)

    @http_error(status_code=404)
    async def http_error_404(self, request: web.Request) -> web.Response:
        return web.json_response({"status": "not found"}, status=404)

    @http_error(status_code=405)
    async def http_error_405(self, request: web.Request) -> web.Response:
        return web.json_response({"status": "method not allowed"}, status=405)

    @http_error(status_code=500)
    async def http_error_500(self, request: web.Request) -> web.Response:
        return web.json_response({"status": "internal server error"}, status=500)
