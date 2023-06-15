from sanic import text, json, Sanic

app = Sanic("MyHelloWorldApp")

@app.get("/hello")
async def hello_world(request):
    return text("Hello, world.")

@app.get("/hello-json")
async def hello_json(request):
    return json({1:122})