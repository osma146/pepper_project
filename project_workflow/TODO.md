# 📝 Pepper Project To-Do Lists

## ✅ Quick Checklist (Basic Syntax)
- [x] Example completed task
- [ ] Example incomplete task
- [ ] Use `[ ]` for open, `[x]` for done.
- [ ] Keep related tasks grouped under headings.

---

## 📦 Project Structure Tasks
### Robot Side
- [x] Create base app folder: `com.jeff.pepper.home`
- [x] Add `manifest.xml`, `config/default.json`
- [ ] Create `python/services/tablet_bridge.py`
- [ ] Add motion server (`python/services/motion_server.py`)
- [ ] Add audio server (`python/services/audio_server.py`)

### Tablet UI
- [x] Basic `index.html`, `css/app.css`, `js/app.js`
- [ ] Implement reconnect logic
- [ ] Add multiple pages (Home, Motion, Audio)

### PC Client
- [ ] Basic client.py with connect/send/receive
- [ ] Logging and reconnect

---

## 📅 Timeline Example (Dates + Priorities)
- **(A) High Priority** – Deploy base app to Pepper **by 2025-08-15**
- **(B) Medium** – Test WS between tablet & robot
- **(C) Low** – Style tablet UI with animations

---

## 📌 Notes & References
> **Tip:** Use blockquotes like this to highlight tips or important reminders.

- Pepper tablet runs an **old WebView**, so:
  - No ES6+ JS (use ES5 syntax only).
  - Avoid CSS variables.
  - Use `XMLHttpRequest` instead of `fetch()`.
- ALMemory event naming pattern:  
  `App/<feature>/<action>` → e.g., `App/Tablet/Toggle`.

---

## 🔗 Links (internal & external)
- [Pepper NAOqi API Reference](http://doc.aldebaran.com/2-5/index.html)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Local file example](./config/default.json)

---

## 📊 Table Example
| Task                  | Status | Owner | Notes |
|-----------------------|--------|-------|-------|
| Tablet bridge         | ⏳     | Jeff  | Waiting on Pepper IP |
| Motion server         | ❌     | Jeff  | To be implemented |
| Audio server          | ❌     | Jeff  | Needs mic driver test |
| Tablet UI animations  | ✅     | Jeff  | Works in ES5 |

---

## 🔢 Numbered Steps Example
1. SSH into Pepper.
2. Deploy app with `scp`.
3. Run `scripts/start_services.sh`.
4. Show tablet with `scripts/start_tablet.sh`.

---

## 💡 Code Blocks
### Inline code
Run `qicli call ALTextToSpeech.say "Hello"` to test.

### Multi-line code
```sh
# Deploy app
scp -r ./apps/com.jeff.pepper.home nao@<PEPPER_IP>:/home/nao/.local/share/PackageManager/apps/
