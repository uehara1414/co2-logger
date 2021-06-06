# Imports the Google Cloud client library
from google.cloud import datastore


def main():
    # Instantiates a client
    datastore_client = datastore.Client()

    # The kind for the new entity
    kind = "Task"
    # The name/ID for the new entity
    name = "sampletask1"
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, name)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task["description"] = "Buy milk"

    # Saves the entity
    datastore_client.put(task)

    print(f"Saved {task.key.name}: {task['description']}")


if __name__ == '__main__':
    main()
