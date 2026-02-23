#!/usr/bin/env python3
"""
Echo server: receives packets and echoes them back.
Prints its destination hash on startup - pass this to the echo client.
"""

import RNS
import time

APP_NAME = "reticulum_pi_mesh"
ASPECT = "echo"
server_destination = None


def packet_received(message, packet):
    text = message.decode("utf-8", errors="replace")
    print(f"[Server] Received: {text}")
    packet.reply(("Echo: " + text).encode("utf-8"))


def main():
    r = RNS.Reticulum()
    identity = RNS.Identity()
    global server_destination
    server_destination = RNS.Destination(
        identity, RNS.Destination.IN, RNS.Destination.SINGLE,
        APP_NAME, ASPECT
    )
    server_destination.set_proof_strategy(RNS.Destination.PROVE_ALL)
    server_destination.set_packet_callback(packet_received)
    server_destination.announce()
    print(f"[Server] Listening at: {RNS.prettyhexrep(server_destination.hash)}")
    print("[Server] Pass the hash above to the echo client.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Server] Shutting down.")


if __name__ == "__main__":
    main()
