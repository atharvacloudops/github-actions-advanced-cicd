from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GitHub Actions Advanced CI/CD", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "1.0.0", "environment": "production"}