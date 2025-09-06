from fastapi import FastAPI
from app.routers.upload import router as upload_router

app: FastAPI = FastAPI(
    title="Briefly FastAPI Server",
    description="Summary uploaded document into insights.",
)


@app.get("/")
def get_health() -> str:
    return "Okay"


app.include_router(upload_router, prefix="/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=80, reload=True, workers=1)
