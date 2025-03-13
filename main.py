from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="E-commerce Backend API", docs_url="/docs")

# Include API routes
app.include_router(router)
