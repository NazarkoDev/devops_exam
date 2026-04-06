from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привіт! Це фінальне завдання Назарія Теслюка. Працює в Kubernetes!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}