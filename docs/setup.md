# Setup Guide

## Prerequisites

- Raspberry Pi (any model) or any Linux machine
- Python 3.8+
- Go 1.21+ (for the integration layer)
- Network connectivity (Ethernet or WiFi)

---

## 1. Clone the Repository

```bash
git clone https://github.com/5hay196/reticulum-pi-mesh.git
cd reticulum-pi-mesh
```

## 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure RNS

```bash
mkdir -p ~/.config/reticulum
cp rns/config/config ~/.config/reticulum/config
```

Edit the config if needed. To connect to a second node on your LAN, uncomment the `TCPClientInterface` section and set `target_host` to that node's IP.

## 4. Run the Node

```bash
python3 rns/node.py
```

Output will look like:

```
[Node] Identity: <hash>
[Node] Destination: <hash>
[Node] Announcing every 300s. Ctrl+C to stop.
```

## 5. Test with Echo Examples

**Machine A (server):**

```bash
python3 rns/examples/echo_server.py
# Note the destination hash printed on startup
```

**Machine B (client):**

```bash
python3 rns/examples/echo_client.py <destination_hash> "Hello from Pi!"
```

## 6. Go Integration Layer

```bash
cd integration
go run main.go
```

---

## Testing on a Single Machine

You can run two RNS instances on one machine using separate config directories with different TCP ports. Point one instance's `TCPClientInterface` at the other's `TCPServerInterface` port.

---

## Next Steps

- Add more nodes on your LAN
- See [hardware.md](hardware.md) to add a LoRa (RNode) interface for off-grid mesh
