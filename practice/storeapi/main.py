import logging

from fastapi import FastAPI

from storeapi import post

logging.config.fileConfig("./storeapi/logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(post.router)
