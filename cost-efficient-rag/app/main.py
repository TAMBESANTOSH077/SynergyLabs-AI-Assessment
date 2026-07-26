from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router

app = FastAPI(
    title="Cost Efficient RAG API",
    description="AI-powered Retrieval-Augmented Generation using Gemini and ChromaDB",
    version="1.0.0",
)

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# API Routes
# -----------------------------
app.include_router(router)

# -----------------------------
# Static Frontend
# -----------------------------
app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend",
)

# -----------------------------
# Home Page
# -----------------------------
@app.get("/", include_in_schema=False)
async def home():
    return FileResponse("frontend/index.html")


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy",
        "application": "Cost Efficient RAG",
        "version": "1.0.0"
    }


# -----------------------------
# Favicon
# -----------------------------
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("frontend/favicon.ico")


# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
async def startup_event():
    print("=" * 60)
    print("🚀 Cost Efficient RAG Started Successfully")
    print("🌐 Home     : http://127.0.0.1:8000")
    print("📘 Swagger  : http://127.0.0.1:8000/docs")
    print("=" * 60)


# -----------------------------
# Shutdown Event
# -----------------------------
@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 Cost Efficient RAG Server Stopped")