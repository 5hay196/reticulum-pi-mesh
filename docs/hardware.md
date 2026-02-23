# Hardware Guide - LoRa / RNode

This guide covers adding a LoRa interface for off-grid mesh (future phase).

## Why LoRa?

LoRa allows Reticulum nodes to communicate without any IP infrastructure,
over distances of several kilometres at low data rates. Combined with Reticulum's
built-in encryption and mesh routing, this enables truly resilient off-grid communications.

---

## Compatible Hardware

| Device | Notes |
|---|---|
| [RNode](https://unsigned.io/rnode/) | Official device by Mark Qvist. Best supported. |
| LILYGO T-Beam | Popular ESP32 + LoRa board |
| LILYGO LoRa32 | Compact option |
| Heltec LoRa32 | Common and affordable |
| RAK Wireless modules | Enterprise-grade |
| LoRa HATs for Raspberry Pi | Connect via GPIO / serial |

---

## Flashing RNode Firmware

```bash
pip install rnodeconf
rnodeconf /dev/ttyUSB0 --autoinstall
```

---

## RNS Config for RNode

Add to `~/.config/reticulum/config`:

```
[interface:RNodeInterface]
  type = RNodeInterface
  enabled = True
  port = /dev/ttyUSB0
  frequency = 868000000
  bandwidth = 125000
  txpower = 14
  spreadingfactor = 8
  codingrate = 5
```

### Frequency by Region

| Region | Frequency |
|---|---|
| Europe | 868 MHz |
| US / Canada | 915 MHz |
| Asia | 433 MHz |

---

## Raspberry Pi GPIO / HAT

Enable serial in raspi-config:

```bash
sudo raspi-config
# Interface Options -> Serial Port -> Enable
```

Then set `port = /dev/ttyAMA0` (or `/dev/serial0`) in the RNS config.
