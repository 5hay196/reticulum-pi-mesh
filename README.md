# reticulum-pi-mesh

Experimenting with decentralised, encrypted mesh networking on Raspberry Pi using the [Reticulum Network Stack](https://reticulum.network/) (RNS).

## Overview

- **Python (RNS layer):** Runs the Reticulum stack, handles node configuration, destinations, and announcements
- **Go (integration layer):** Communicates with the Python RNS process via the local shared instance interface

## Goals

- [ ] Get a TCP/LAN Reticulum node running on Raspberry Pi
- [ ] Send and receive encrypted messages between nodes on the same LAN
- [ ] Add LoRa (RNode) interface for off-grid mesh
- [ ] Bridge Reticulum traffic to the Go integration layer

## Project Structure

```
.
... rns/
...... config/         # RNS configuration
...... examples/       # echo_server.py, echo_client.py
...... node.py         # Main node entry point
... integration/
...... main.go
...... go.mod
... docs/
...... setup.md
...... hardware.md
... requirements.txt
... .gitignore
```

## Quick Start

See [docs/setup.md](docs/setup.md) for full setup instructions.

```bash
pip install rns
python3 rns/node.py
```

## Requirements

- Python 3.8+
- Raspberry Pi (or any Linux machine)
- Go 1.21+ (integration layer)

## Hardware (LoRa phase)

See [docs/hardware.md](docs/hardware.md) for RNode / LoRa HAT setup.

## License

MIT
