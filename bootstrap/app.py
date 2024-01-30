from starlette.staticfiles import StaticFiles

import db
import api
import middlewares
import scheduler
from config import settings
from . import hook
from . import page
from fastapi import FastAPI
from config import settings
from services import docker

application = FastAPI(debug=settings.DEBUG, title=settings.PROJECT_NAME)

db.init(application)
api.init(application)
page.init(application)
middlewares.init(application)
docker.init(application)
scheduler.init(application)
