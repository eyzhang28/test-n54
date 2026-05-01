from fastapi import FastAPI


API_VERSION = "2.1"

app = FastAPI()


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the service health status and API version."""
    return {"status": "ok", "version": API_VERSION}
