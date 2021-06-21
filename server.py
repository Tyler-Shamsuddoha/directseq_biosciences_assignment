#!/usr/bin/env python3
# Server File
#

import socket
import pickle

basecallings = {"A": 329.0525, "C": 305.0413, "G": 345.0474, "U": 306.0253}
returnlist_with_dup = []


def send_answer(connection):
    """Sends list of tuples back to client."""
    print("return list is: " + str(returnlist_with_dup))
    if not returnlist_with_dup:
        # List is empty, nothing was found
        d = pickle.dumps([])
        connection.send(d)
    else:
        # Remove any duplicates by type casting to a set and back to a list
        returnlist = list(set(returnlist_with_dup))
        # Send data back to the client
        e = pickle.dumps(returnlist)
        connection.send(e)


def server_program():
    """ Starts the server. Handles the procedure of the server."""
    print("Server has started... waiting for connection")
    hostName = socket.gethostname()
    port = 9999

    server_socket = socket.socket()
    server_socket.bind((hostName, port))
    server_socket.listen(2)  # How many connections
    conn, address = server_socket.accept()  # Accept a new connection
    print("Connection from: " + str(address))
    data = "Connected to the server."
    # Sending initial welcome message
    conn.send(data.encode())
    while True:
        # Receive pickled, object data from client, do not need to decode
        floats_list = pickle.loads(conn.recv(4096))
        print(floats_list)
        find_basecallings(floats_list)
        send_answer(conn)
        # Clear the list after we send the data to client
        returnlist_with_dup.clear()


def check_approximately_equal(ans1, ans2, floats, i, j):
    """Adds values if they are considered approximately equal to the dictionary values.

    Keyword arguments:
        ans1 -- the first result number being checked against the dictionary values
        ans2 -- the second result number being checked against the dictionary values
        floats -- the list of floating point numbers
        i -- the index of the first number in the list
        j -- the index of the second number in the list
    """
    for key, value in basecallings.items():
        if 0 <= (ans1 - value) <= 0.00000001 or 0 <= (value - ans1) <= 0.00000001:
            # Instead of returning, add tuple to the list after checking that it isn't in already
            returnlist_with_dup.append((floats[i], floats[j], key))
            break
        if 0 <= (ans2 - value) <= 0.00000001 or 0 <= (value - ans2) <= 0.00000001:
            # Check that the tuple isn't in the list already, if it isn't then add it
            returnlist_with_dup.append((floats[i], floats[j], key))
            break


def find_basecallings(floats):
    """Evaluates every two-combination of numbers from the floats list.

    Keyword arguments:
        floats -- list of floating point numbers
    """
    for i in range(0, len(floats)):
        for j in range(len(floats) - 1, -1, -1):
            if i == j:
                break
            ans1 = floats[i] - floats[j]
            ans2 = floats[j] - floats[i]
            check_approximately_equal(ans1, ans2, floats, i, j)


if __name__ == '__main__':
    server_program()
