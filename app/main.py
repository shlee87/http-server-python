import socket

def main():
    print("Logs from your program will appear here!")

    # Create a TCP/IP socket
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    # Wait for a client to connect
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")

        # Receive the request from the client (not processing it in this stage)
        _ = connection.recv(1024)

        # Send HTTP response
        http_response = "HTTP/1.1 200 OK\r\n\r\n"
        connection.sendall(http_response.encode('utf-8'))

    finally:
        # Clean up the connection
        connection.close()

if __name__ == "__main__":
    main()
