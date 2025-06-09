import threading
import socket
import json
import time
import sys

receiver = ""
stop_event = threading.Event()


def receive_message(client):
    global receiver
    while not stop_event.is_set():
        message_json = client.recv(1024).decode()
        message_object = json.loads(message_json)
        print(message_object["sender"], ": ", message_object["message"], "\n")
        if receiver == "" and not message_object["sender"] == "Server":
            receiver = message_object["sender"]

def send_message(client, receiver, sender):
    while not stop_event.is_set():
        message = input(">>>")

        if (message.startswith("\\addr")):
            receiver = message[5:]
            print("Recipient set to ", receiver, "\n")
            continue
        elif message == "\\curr":
            if receiver == "":
                print("No recipient set currently. \n")
            else:
                print("Current recipient is ", receiver, "\n")
            continue
        elif message == "\\quit":
            if input("Are you sure you want to quit the app? Y/n \n") == 'Y':
                client.send(json.dumps({"request": "quit"}).encode())
                # client.close()
                stop_event.set()
                sys.exit()
            continue

        if (receiver == ""):
            receiver = input("No recipient chosen, who would you like to talk to? \n")

        data = {
            "request": "message",
            "sender": sender.strip(),
            "receiver": receiver.strip(),
            "message": message
        }
        data_json = json.dumps(data)
        client.send(data_json.encode())
        time.sleep(0.5)

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))

    receiving_thread = threading.Thread(target=receive_message, args=(client,))
    receiving_thread.start()

    name = input("What is your name? \n")
    name.strip()
    login_request = {
        "request": "login",
        "sender": name
    }
    client.send(json.dumps(login_request).encode())

    sending_thread = threading.Thread(target=send_message, args=(client, receiver, name))
    sending_thread.start()

if __name__ == "__main__":
    start_client()