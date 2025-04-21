from flask import Flask
from src.db.database import engine, Base
from src.models.models import User, Order

app = Flask(__name__)

@app.route("/")


@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
