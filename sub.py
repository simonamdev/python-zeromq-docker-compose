import zmq

print('Starting Client...')

context = zmq.Context()

socket = context.socket(zmq.SUB)
socket.connect("tcp://publisher:5555")
socket.setsockopt(zmq.SUBSCRIBE, ''.encode('ascii'))

print('Starting Client loop now!')
while True:
    print('Waiting for message...')
    message = socket.recv_string()
    print('Received message: {}'.format(message))
