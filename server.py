# server

import socket
import pickle
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (sys.argv[1], int(sys.argv[2]))
sock.bind(addr)

ack_seq = 0
answer = []

while True:
    # print("before")
    data, addr = sock.recvfrom(5000)
    # print("after")
    data = pickle.loads(data)
    seq = data[0]
    message = data[1]
    amount = data[2]

    logger.info('Deliver seq = %s', seq)

    if seq == ack_seq:
        answer.append(message)
        ack_seq += 1

        message = pickle.dumps(['ack', seq])
        sock.sendto(message, ("localhost", 5000))
        logging.info('Sent ACK seq = %s', seq)

    if ack_seq >= amount:
        break

logging.info('Final answer : \n %s', answer)

sock.close()