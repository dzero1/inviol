from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import events
from .dependencies import create_db_and_tables

# Initialize FastAPI
app = FastAPI()

# Configure CORS, make sure to update this when deploying to production
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(events.router)

# On startup, create the database and tables
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
