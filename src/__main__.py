import asyncio
import uvicorn

from src.handlers.kafka import consumer_handler

from src.settings import HTTP_PORT


async def main():
    try:
        config = uvicorn.Config("src:app", port=HTTP_PORT)
        server = uvicorn.Server(config)
        await server.serve()
    except KeyboardInterrupt:
        return None


loop = asyncio.get_event_loop()
loop.create_task(consumer_handler())
loop.run_until_complete(main())

