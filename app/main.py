from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/")
def get_health() ->str:
    return "Okay"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=80, reload=True, workers=1)