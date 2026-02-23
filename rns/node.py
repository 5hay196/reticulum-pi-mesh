#!/usr/bin/env python3
"""
reticulum-pi-mesh: Main RNS node.
Initialises Reticulum, registers a destination, and announces periodically.
"""

import RNS
import time
import argparse

APP_NAME = "reticulum_pi_mesh"
ANNOUNCE_INTERVAL = 300  # seconds


def on_packet_received(message, packet):
    text = message.decode("utf-8", errors="replace")
    print(f"[Node] Packet received: {text}")


def main():
    parser = argparse.ArgumentParser(description="Reticulum Pi Mesh Node")
    parser.add_argument("--config", default=None, help="Path to RNS config directory")
    args = parser.parse_args()

    r = RNS.Reticulum(args.config)
    identity = RNS.Identity()
    print(f"[Node] Identity: {RNS.prettyhexrep(identity.hash)}")

    destination = RNS.Destination(
        identity,
        RNS.Destination.IN,
        RNS.Destination.SINGLE,
        APP_NAME,
        "node"
    )
    destination.set_proof_strategy(RNS.Destination.PROVE_ALL)
    destination.set_packet_callback(on_packet_received)

    print(f"[Node] Destination: {RNS.prettyhexrep(destination.hash)}")
    print(f"[Node] Announcing every {ANNOUNCE_INTERVAL}s. Ctrl+C to stop.")

    try:
        while True:
            destination.announce()
            print("[Node] Announced.")
            time.sleep(ANNOUNCE_INTERVAL)
    except KeyboardInterrupt:
        print("\n[Node] Shutting down.")


if __name__ == "__main__":
    main()
