from aiohttp import web
from tomodachi import http

from service.base import BaseService


class Nangijala(BaseService):
    name = "nangijala.lauri.af"

    @http(("GET", "POST"), r"/switch/(?P<switch_uuid>[^/]+?)/renew/?")
    async def cards(self, request: web.Request, switch_uuid: str) -> web.Response:
        return web.json_response({"status": "ok"}, status=200)
