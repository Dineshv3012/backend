from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend connection (important for websites)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is running on Render 🚀"}

@app.get("/hello")
def hello(name: str = "Dinesh"):
    return {"message": f"Hello {name} 🔥"}

@app.get("/ai")
def fake_ai(prompt: str):
    return {"response": f"You asked: {prompt}"}
