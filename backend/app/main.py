from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.endpoints as endpoints



def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(endpoints.router)
    return app


app = create_app()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)