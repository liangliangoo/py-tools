from sanic import text, json, Sanic

from common import response
from common.response import Response

app = Sanic("MyHelloWorldApp")


@app.get("/hello")
async def hello_world(request):
    return text("Hello, world.")


@app.get("/hello-json")
async def hello_json(request):
    return json(Response.success(1000, "ok", "hello response"))
