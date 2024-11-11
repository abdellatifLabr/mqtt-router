from dataclasses import dataclass

from mqtt_router import MQTTRouter


@dataclass
class Message:
    topic: str
    message: str

    def __str__(self):
        return self.message


router = MQTTRouter()


@router.add("telemetry/devices/<str:streaming_key>/<int:count>/meta")
def handle_meta(message: Message, streaming_key: str, count: int):
    print("Received meta '%s' with count '%d' from device '%s'" % (message, count, streaming_key))


def on_message(message: Message):
    router.route(message)


def main():
    on_message(Message(topic="telemetry/devices/key/1234/meta", message="Hello there!"))


if __name__ == "__main__":
    main()
