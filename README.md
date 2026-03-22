# 🌐 Replit Talking to Pi

> Control a Raspberry Pi from anywhere in the world — bridged by ngrok and powered by Claude.

---

## 🧠 About This Project

**Replit Talking to Pi** is a networking project that establishes a live two-way communication channel between a Replit-hosted web app and a Raspberry Pi 5. Using ngrok to punch through the local network, the app can send commands to the Pi and receive responses in real time — from anywhere, on any device.

Claude handles the intelligent layer, processing commands and generating responses between the two ends of the connection.

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| **Hardware** | Raspberry Pi 5 |
| **Tunnel / Networking** | ngrok |
| **AI** | Claude (Anthropic API), Gemini (Google) |
| **App Platform** | Replit |
| **Language** | Python |

---

## ⚙️ How It Works

1. **Pi runs a local server** — A Python server starts on the Raspberry Pi, listening for incoming requests
2. **ngrok creates a public URL** — ngrok tunnels the Pi's local port to a public HTTPS endpoint, making it reachable from the internet
3. **Replit app connects** — The Replit-hosted app sends commands to the ngrok URL, which forwards them to the Pi
4. **Claude processes** — Claude handles the intelligence layer, interpreting messages and generating smart responses
5. **Pi responds** — The Pi executes the command and sends a response back through the tunnel to the app

---

## 🔗 The Architecture

```
Replit App  ──────►  ngrok Public URL  ──────►  Raspberry Pi 5
    ▲                                                  │
    └──────────────────  Response  ───────────────────┘
                    (Claude in the middle)
```

---

## 💡 Key Learnings

- Using ngrok to expose a local device to the public internet
- Building a client-server architecture across two completely different platforms
- Combining cloud-hosted apps with physical hardware in one pipeline
- Understanding tunneling, ports, and HTTP requests at a practical level

---

## 🚀 Part of the AI Bootcamp

This project was built during the **Week 2 Physical AI** phase of a 15-day AI Developer Bootcamp.  
See the full bootcamp repo → [The AI Bootcamp](../README.md)

---

*Your Pi, accessible from anywhere on Earth.* 🌍
