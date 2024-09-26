from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def test():
    return {"Test": "Done"}


@app.predict("/predict")
def prdict():
    pre = "mirror"
    return pre
