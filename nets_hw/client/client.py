# client

import socket
import pickle
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

addr = (sys.argv[1], int(sys.argv[2]))
logger.info('argv[1] = %s', sys.argv[1])
logger.info('argv[2] = %s', sys.argv[2])


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(("localhost", 5000))


seq = 0
amount = 0
messages = []

file = open('input.txt', 'r')

logger.info('before reading')

# divide file into pieces with 4096 bytes each
while True:
    cur = file.read(512)
    logger.info('read = %s', cur)
    if not cur:
        break
    messages.append(cur)
    amount += 1
file.close()

logging.info('Amount of sequences = %s', amount)


# new_data = input()
# # print(new_data)
# last_pos = 0
# while True:
#     cur = new_data[last_pos: min(last_pos + 512, len(new_data))]
#     last_pos += 512
#     amount += 1
#     messages.append(cur)
#     if last_pos >= len(new_data):
#         break
# logging.info('Amount of sequences = %s', amount)



sock.settimeout(3)
logger.info('addr = %s', addr)

while True:
    if seq >= amount:
        break

    logger.info('addr = %s', addr)

    message = pickle.dumps([seq, messages[seq], amount])
    sock.sendto(message, addr)
    logger.info('Transmit seq = %s', seq)

    try:
        logging.info('i try')
        data, tmp_addr = sock.recvfrom(5000)
        # logging.info('Received data = %s', data)
    except:
        continue

    message = pickle.loads(data)
    ack = message[1]
    # print(ack)
    logging.info('Received ACK seq = %s', ack)

    if ack == seq:
        logging.info('Received correct ACK')
        seq += 1

sock.close()