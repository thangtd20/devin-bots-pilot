import csv
from pathlib import Path

from fastapi import FastAPI

app = FastAPI(title="Deployment Progress Pilot")
SAMPLE_CSV = Path(__file__).with_name("sample.csv")


@app.get("/projects")
def list_projects() -> list[dict[str, str]]:
    with SAMPLE_CSV.open(encoding="utf-8", newline="") as csv_file:
        return list(csv.DictReader(csv_file))
