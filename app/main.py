import socket

def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")
        
        # Receive the HTTP request from the client
        request_data = connection.recv(1024).decode('utf-8')
        print("Received request:")
        print(request_data)
        
        # Extract the path from the first line of the request
        first_line = request_data.split("\r\n")[0]  # Split the request into lines and get the first line
        path = first_line.split(' ')[1]  # Split the first line by space and get the second element, which is the path
        
        # Prepare the HTTP response
        if path == '/':
            http_response = "HTTP/1.1 200 OK\r\n\r\nWelcome to the homepage!"
        else:
            http_response = "HTTP/1.1 404 Not Found\r\n\r\nThe requested resource was not found on this server."
        
        # Send the HTTP response
        connection.sendall(http_response.encode('utf-8'))
        
    finally:
        connection.close()

if __name__ == "__main__":
    main()
