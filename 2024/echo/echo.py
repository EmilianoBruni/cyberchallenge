#!/usr/bin/env python3

import platform
import asyncio

PORT_ECHO_UDP = 4002
PORT_ECHO_TCP = 5002
INADDR_ANY = "0.0.0.0"

SERVER_NAME = platform.node()

async def main():
    loop = asyncio.get_running_loop()

    print(f"Starting UDP server on port {PORT_ECHO_UDP}")
    await loop.create_datagram_endpoint(
        lambda: UdpEchoServer(),
        local_addr=(INADDR_ANY, PORT_ECHO_UDP))

    print(f"Starting TCP server on port {PORT_ECHO_TCP}")
    tcp_server = await loop.create_server(
        lambda: TcpEchoServer(),
        INADDR_ANY, PORT_ECHO_TCP)

    async with tcp_server:
        await tcp_server.serve_forever()

class UdpEchoServer:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        in_msg = data.decode().strip()
        print(f'UDP: Received {in_msg} from {addr}')
        out_msg = f'{in_msg}\n'
        self.transport.sendto(out_msg.encode(), addr)


class TcpEchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print(f'TCP: Connection from {self.peername}')
        self.transport = transport

    def data_received(self, data):
        in_msg = data.decode().strip()
        print(f'TCP: Received: {in_msg} from {self.peername}')
        out_msg = f'{in_msg}\n'
        self.transport.write(out_msg.encode())

asyncio.run(main())