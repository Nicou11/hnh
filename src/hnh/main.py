from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def test():
    return {"Test": "Done"}


@app.get("/predict")
def prdict():
    pre = {"result": "Hot dog"}
    return pre
