# Client File
# Author: Tyler Shamsuddoha

import socket
import pickle


def handle_base_callings(client_socket):
    """Handles the information to be displayed back on the client side."""
    list_basecallings = pickle.loads(client_socket.recv(4096))
    if len(list_basecallings) > 0:
        print("Success. Below are the tuples of the found basecallings:\n")
        print(*list_basecallings, sep="\n")
        print()
    else:
        print("No basecallings were found in the given floats.")


def run_client():
    """ Runs the client. Handles the procedure of the client side. """
    hostName = socket.gethostname()  # localHost
    port = 9999

    client_socket = socket.socket()
    client_socket.connect((hostName, port))
    welcome_message = client_socket.recv(4096).decode()
    print(welcome_message)
    while True:
        # Getting user input and sending to the server
        message = pickle.dumps(get_floats())
        client_socket.send(message)
        handle_base_callings(client_socket)


def get_floats():
    """Gets a list of floats from the user"""
    print("Enter the floats to send, separated by a comma.")
    while True:
        try:
            floats_list = [float(x) for x in input("Press Enter when finished\n").replace(" ", "").split(',')]
            print("\nYou have entered:\n",floats_list)
            return floats_list
        except ValueError:
            print("Invalid input, please enter floats separated by a comma")


if __name__ == '__main__':
    run_client()
