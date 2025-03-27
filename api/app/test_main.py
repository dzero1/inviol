from fastapi.testclient import TestClient
import faker
import random
import datetime
import json
import os

from .main import app

os.environ["event_id"] = "0"

# Init Test Client
client = TestClient(app)

# Create a faker instance
fake = faker.Faker()



def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

# Keep event_id global for next events
def test_create_event():
    event = {
                "device_id": fake.uuid4(),
                "timestamp": datetime.datetime.now(),
                "description": random.choice(["temperature reading", "startup", "shutdown", "error log"]),
                "meta": {},
            }

    response = client.post("/events", data=json.dumps(event, default=str))
    assert response.status_code == 200
    assert response.json()['device_id'] == event['device_id']

    os.environ["event_id"] = str(response.json()["id"])
    print("event_id: " + os.environ["event_id"])

def test_get_events():
    response = client.get("/events")
    assert response.status_code == 200
    # assert response is list

def test_get_one_event():
    response = client.get("/events/"+os.environ["event_id"])
    assert response.status_code == 200
    assert response.json()['id'] == int(os.environ["event_id"])

def test_update_event():
    event = {
            "device_id": fake.uuid4(),
            "timestamp": datetime.datetime.now(),
            "description": random.choice(["temperature reading", "startup", "shutdown", "error log"]),
            "meta": {},
        }

    response = client.put("/events/"+os.environ["event_id"], data=json.dumps(event, default=str))
    assert response.status_code == 200
    assert response.json()['device_id'] == event["device_id"]

def test_delete_event():
    response = client.delete("/events/"+os.environ["event_id"])
    assert response.status_code == 200

