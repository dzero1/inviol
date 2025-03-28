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

        metadata = json.loads(fake.json(data_columns=[('Name', 'name'), ('Points', 'pyint', {'min_value':50, 'max_value':100})], num_rows=1))
        fake_event = Event(
            device_id=fake.uuid4(),
            timestamp=datetime.datetime.now(),
            description=random.choice(["temperature reading", "startup", "shutdown", "error log"]),
            meta = metadata,
        )

        fake_events.append(fake_event)

    return fake_events