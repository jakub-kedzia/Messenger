import threading
import socket
import json
import queue

client_queues = {}


def handle_client(client_socket):
    stop_event = threading.Event()

    while not stop_event.is_set():
        data_json = client_socket.recv(1024).decode()
        data = json.loads(data_json)
        name = data["sender"]

        if data["request"] == "message":
            print("Message received from ", data["sender"], " for ", data["receiver"])

            if data["receiver"] in client_queues:
                message_object = {
                    "sender": data["sender"],
                    "message": data["message"]
                }
                client_queues[data["receiver"]].put(message_object)
                print("Przyjeto wiadomosc \n")
            else:
                message_object = {
                    "sender": "Serwer",
                    "message": "Nie istnieje taki odbiorca. \n"
                }
                message_json = json.dumps(message_object)
                client_socket.send(message_json.encode())
                print("Nie ma takiego uzytkownika w bazie \n")

        if data["request"] == "login":
            client_queues[name] = queue.Queue()
            message_object = {
                "sender": "Server",
                "message": "It's your server, you've logged in succesfully! \n"
            }
            message_json = json.dumps(message_object)
            client_socket.send(message_json.encode())

        if data["request"] == "quit":
            client_queues.pop(name)
            stop_event.set()

        if (client_queues[name].empty() == False):
            message_object = client_queues[name].get()
            message_json = json.dumps(message_object)
            client_socket.send(message_json.encode())


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen()
    print("Server is listening on 127.0.0.1 on port 12345.")

    while True:
        client_socket, client_address = server.accept()

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    start_server()
