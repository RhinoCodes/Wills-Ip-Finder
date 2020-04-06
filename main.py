import uvicorn, time, pprint

async def app(scope, receive, send):
    body = f"Hello, {scope['client'][0]}!"
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    })
    await send({
        'type': 'http.response.body',
        
        'body': body.encode('utf-8'),
    })

if __name__ == "__main__":
    uvicorn.run("example:app", host="127.0.0.1", port=5000, log_level="info")
