from fastapi import FastAPI

app = FastAPI()
# teste do pipeline
@app.get("/")
async def root():
        return {"Hello! CI/CD está funcionando."}
