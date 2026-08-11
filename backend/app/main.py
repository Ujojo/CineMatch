from fastapi import FastAPI

app = FastAPI(title="CineMatch API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API CineMatch opérationnelle !"}