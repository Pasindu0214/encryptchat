import socket
import threading

import rsa

def get_local_ip():
    # Create a temporary socket to find the local IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external address to find the local IP address
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

public_key, private_key = rsa.newkeys(1024)
public_partner = None

choice = input ("Do you want to host (1) or to connect (2)?")


if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp , for UDP you can use socket.SOCK_DGRAM instead of SOCK_STREAM
    local_ip = get_local_ip()
    server.bind((local_ip, 9999)) #replace with your local ip address using ipconfig in cmd or you can use the public IP of your own
    server.listen()

    client, _ = server.accept()

    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_ip = get_local_ip()
    client.connect((local_ip , 9999)) #you can use the same ip in choice 1 or public ip 

    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))

else:
    exit()

def sending_msg(c):
    while True:
        message = input("")
        c.send(rsa.encrypt(message.encode(), public_partner))
        print("You: " + message)

def receiving_msg(c):
    while True:
        print("Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())

threading.Thread(target=sending_msg, args=(client,)).start()
threading.Thread(target=receiving_msg, args=(client,)).start()