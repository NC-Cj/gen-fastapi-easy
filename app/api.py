from fastapi import APIRouter

app = APIRouter()


@app.get('/test')
def test():
    return {"code": 0, "message": "pone!"}
