from zipimport import zipimporter
from fastapi import FastAPI

app = FastAPI()

@app.get("/itemsx/{x}")
@app.get("/itemsy/{y}")
@app.get("/itemsz/{z}")

async def read_itemx(x: int):
    return {"item_idx": x}

async def read_itemy(y: int):
    return {"item_idy": y}

async def read_itemz(z: int):
    return {"item_idz": z}