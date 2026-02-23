#!/usr/bin/env python3
"""
Echo client: sends a message to the echo server.
Usage: python3 echo_client.py <destination_hash> <message>
"""

import RNS
import sys
import time

APP_NAME = "reticulum_pi_mesh"
ASPECT = "echo"
TIMEOUT = 15


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 echo_client.py <destination_hash> <message>")
        sys.exit(1)

    dest_hex = sys.argv[1]
    message = " ".join(sys.argv[2:])
    r = RNS.Reticulum()

    try:
        dest_hash = bytes.fromhex(dest_hex)
    except ValueError:
        print("[Client] Invalid destination hash.")
        sys.exit(1)

    if not RNS.Transport.has_path(dest_hash):
        print("[Client] No path known - requesting...")
        RNS.Transport.request_path(dest_hash)
        start = time.time()
        while not RNS.Transport.has_path(dest_hash):
            time.sleep(0.1)
            if time.time() - start > TIMEOUT:
                print("[Client] Path request timed out.")
                sys.exit(1)

    identity = RNS.Identity.recall(dest_hash)
    if identity is None:
        print("[Client] Could not recall identity.")
        sys.exit(1)

    destination = RNS.Destination(
        identity, RNS.Destination.OUT, RNS.Destination.SINGLE,
        APP_NAME, ASPECT
    )
    packet = RNS.Packet(destination, message.encode("utf-8"))
    receipt = packet.send()
    print(f"[Client] Sent: {message}")

    start = time.time()
    while receipt.status != RNS.PacketReceipt.DELIVERED:
        time.sleep(0.1)
        if time.time() - start > TIMEOUT:
            print("[Client] No reply within timeout.")
            sys.exit(1)
    print("[Client] Delivered.")


if __name__ == "__main__":
    main()
