import faker
import random
import datetime
import json

from ..models.event import Event

# Create a faker instance
fake = faker.Faker()

def generate_data(count):
    fake_events = []

    for _ in range(count):
        """Generates random data in the specified format"""
        fake_event = Event(
            device_id=fake.uuid4(),
            timestamp=datetime.datetime.now(),
            description=random.choice(["temperature reading", "startup", "shutdown", "error log"]),
            meta=json.dumps(fake.json()),
        )

        fake_events.append(fake_event)

    return fake_events