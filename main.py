from fastapi import FastAPI, Request,HTTPException

app = FastAPI()
import aiofiles

# Upload file
@app.post("/upload/face-reco")
async def faceRecognSimulator(request: Request):
    try:
        # Extract the filename from the request headers.(none extra protect)
        filename = request.headers['filename']
        async with aiofiles.open(filename, 'wb') as f:
            async for chunk in request.stream():
                await f.write(chunk)
        return {"username": filename}
    except Exception:
        raise HTTPException(status_code=408, detail="Error uploading")

@app.post("/upload/face-anti")
async def faceAntiSimulator(request: Request):
    try:
        # Extract the filename from the request headers.(none extra protect)
        filename = request.headers['filename']
        async with aiofiles.open(filename, 'wb') as f:
            async for chunk in request.stream():
                await f.write(chunk)
        if(filename == "capture.jpg"):
            return HTTPException(status_code=200, detail="Success")
        else:
            raise HTTPException(status_code=411, detail="Error FaceAntiSpoofing")
    except Exception:
        raise HTTPException(status_code=408, detail="Error uploading")

# Action
@app.post("/balance/deposit", tags=["balance"])
async def deposit(request: Request):
    data = await request.json()
    try:
        user_id = data.get("user_id")
        currency = data.get("currency")
        amount = data.get("amount")
    except Exception:
        raise HTTPException(status_code=405, detail="Balance not found")
    raise HTTPException(status_code=200, detail="Success")

@app.post("/account/balance/change", tags=["balance"])
async def change(request: Request):
    data = await request.json()
    try:
        user_id = data.get("user_id")
        currency = data.get("currency")
        amount = data.get("amount")
    except Exception:
        raise HTTPException(status_code=405, detail="Balance not found")
    raise HTTPException(status_code=200, detail="Success")
# Get function
@app.get("/account/face/{faceId}")
async def userIdSimulator(faceId: str):
    return {"userID": "233"}

@app.get("/account/card/{userId}/{currency}")
async def balanceSimulator(userId: str, currency: str):
    return {"balance": 2333}

#ping-pong
@app.get("/ping")
async def pong():
    return {"ping": "pong"}

@app.post("/ping")
async def pong(request: Request):
    data = await request.json()
    return {"pong": data}