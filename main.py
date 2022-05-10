import socket
import pydirectinput

SERVER = "irc.chat.twitch.tv"
PORT = 6667
NICKNAME = "your nickname"
AUTH_TOKEN = "your auth token"
CHANNEL = "#channelname"

sock = socket.socket()
sock.connect((SERVER, PORT))
sock.send(f"PASS {AUTH_TOKEN}\nNICK {NICKNAME}\nJOIN {CHANNEL}\n".encode("utf-8"))

keys = ["q", "w", "e", "r", "d", "f"]


def check_response():
    response = sock.recv(1024).decode("utf-8")
    print(response)
    message = response.split(":")[2].split("\r\n")[0]
    message = message.lower()
    if message in keys:
        pydirectinput.press(message)


def send_message(socket, message):
    msg = f"PRIVMSG {CHANNEL} :{message}"
    socket.send(f"{msg}\n".encode("utf-8"))


send_message(sock, "The bot has joined")
send_message(sock, "here's how it works: Q W E R D F")

while True:
    check_response()
