# 📝 Pepper Project To-Do Lists

## ✅ Main Checklist 


- [ ] basic setup script (git pull and push)
- [ ] pepper setup script (update single and globle apps)
- [ ] temp app finish coding
- [ ] add home app
- [ ] add context apps
- [ ] code sound app (sound supresion)
- [ ] understand ai connection (event sending and recive)
- [ ] find vidio stream ( image update ) / cam vid representation
- [ ] slam possibility
- [ ] life mode
- [ ] logic supresion
- [ ] UI update
- [ ] UI event
- [ ] UI setting
- [ ] globle setting
- [ ] start up app


### Test needed
- [ ] camra connection
- [x] html idex launch in app in app ==F==
- [ ] sound supretion
- [ ] robot ROS setting extraction
- [ ] UI speed / loading screan
- [ ] port / web socket connection duel
- [ ] depth cam
- [ ] animation / behavour package
- [ ] ssh upload from bash win and py
- [ ] ssh launch from bash win and py

## 📦 Project Structure Tasks

### app temp setup
- [ ] Create base app folder: `com.jeff.pepper.base`
- [x] Add `manifest.xml`, 
- [ ] Add `config/default.json`
- [ ] test respond from xrt 
- [ ] add server V
- [ ] Create `python/services/tablet_bridge.py`
- [ ] Add motion server (`python/services/motion_server.py`)
- [ ] Add audio server (`python/services/audio_server.py`)
- [ ] Add vidio server
- [ ] Add js scrpt
- [ ] Add resopnd to config
- [ ] Add update to .xml .xar and .ini

#### Tablet UI
- [ ] Basic `index.html`, `css/app.css`, `js/app.js`
- [ ] Implement reconnect logic
- [ ] get logo
- [ ] get app icon
- [ ] get audio base
- [ ] get loading screan


### Client
- [ ] Basic client.py with connect/send/receive
- [ ] Logging and reconnect
- [ ] data transmition to connect with tasks

## 📅 prioritys
- **(A)** – finish base apps (temp home front + one entertainment)
- **(B)** – update development tools and connection with ai
- **(C)** – slam video strean and sound supretion

## 📌 Notes & References
- Pepper tablet runs an **old WebView**, so:
  - No ES6+ JS (use ES5 syntax only).
  - Avoid CSS variables.
  - Use `XMLHttpRequest` instead of `fetch()`.
  - Alservece is not on tablet so js can't use it
- ALMemory event naming pattern:  
    app_name/event_type/event_name/data -> com.wonder.pepper.temp/say/ttssay/{"text":"hello world"}

## 🔗 Links (internal & external)
- [Pepper NAOqi API Reference](http://doc.aldebaran.com/2-5/index.html)(http://doc.aldebaran.com/2-5/naoqi/index.html)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Local file example](./config/default.json)
