import logging

from fastapi import FastAPI, Query
from lorem_text import lorem

LOGGER = logging.getLogger(__name__)

app = FastAPI()


@app.get("/lipsum/")
async def lipsum(
    lines: int | None = Query(default=None, ge=1, le=1000),
    words: int | None = Query(default=None, ge=1, le=1000),
):
    LOGGER.info(f"lipsum called with lines={lines} and words={words}")
    if lines and words:
        LOGGER.error(f"Both lines and words can not be specified")
        return {"error": "Please specify either lines or words"}
    elif lines:
        LOGGER.info(f"Returning {lines} lines of lorem ipsum")
        return {"message": lorem.paragraphs(lines)}
    elif words:
        LOGGER.info(f"Returning {words} words of lorem ipsum")
        return {"message": lorem.words(words)}
    LOGGER.info(f"Returning lorem ipsum sentence")
    return {"message": lorem.sentence()}
