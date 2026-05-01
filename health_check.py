from fastapi import FastAPI


API_VERSION = "2.1"

app = FastAPI()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "version": API_VERSION}
