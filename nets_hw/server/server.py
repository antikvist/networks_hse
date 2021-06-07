# server

import socket
import pickle
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (sys.argv[1], int(sys.argv[2]))
logger.info('argv[1] = %s', sys.argv[1])
logger.info('argv[2] = %s', sys.argv[2])

logger.info('addr = %s', addr)


sock.bind(addr)

ack_seq = 0
answer = []

logger.info('before')

while True:
    logger.info("before recv")
    data, tmp_addr = sock.recvfrom(5000)
    logger.info("after recv")
    data = pickle.loads(data)
    seq = data[0]
    message = data[1]
    amount = data[2]

    logger.info('Deliver seq = %s', seq)

    if seq == ack_seq:
        answer.append(message)
        ack_seq += 1

        # message = pickle.dumps(['ack', seq])
        # sock.sendto(message, ("client", 30))
        # logging.info('Sent ACK seq = %s', seq)

    message = pickle.dumps(['ack', seq])
    sock.sendto(message, tmp_addr)
    # logging.info('Sent ACK tmp adress = %s', tmp_addr)
    logging.info('Sent ACK seq = %s', seq)

    if ack_seq >= amount:
        break

logging.info('Final answer : \n %s', answer)

sock.close()