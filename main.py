import logging

from fastapi import FastAPI, HTTPException, Query
from lorem_text import lorem

from models.echo_request import EchoRequest
from models.success_response import SuccessResponse

LOGGER = logging.getLogger(__name__)

app = FastAPI()


@app.get("/lipsum/")
async def lipsum(
    lines: int | None = Query(default=None, ge=1, le=1000),
    words: int | None = Query(default=None, ge=1, le=1000),
):
    LOGGER.info(f"lipsum called with lines={lines} and words={words}")
    if lines and words:
        LOGGER.warning(f"Both lines and words can not be specified")
        raise HTTPException(
            status_code=422, detail="Both lines and words can not be specified"
        )
    elif lines:
        LOGGER.info(f"Returning {lines} lines of lorem ipsum")
        return SuccessResponse(message=lorem.paragraphs(lines))
    elif words:
        LOGGER.info(f"Returning {words} words of lorem ipsum")
        return SuccessResponse(message=lorem.words(words))
    LOGGER.info(f"Returning lorem ipsum sentence")
    return SuccessResponse(message=lorem.sentence())


@app.post("/echo/")
async def echo(echo_request: EchoRequest):
    return echo_request
