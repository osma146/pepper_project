# Pepper Project — pepper_APPS

This project is a project to make a highly editable app sofware for pepper 2.5, as pepper 2.7 even though in android lack the ability to have specific programability. 

For an old machin like pepper with out version change updating the software becomes a chalenge, this project looks forword to minamize lib installing and highly dependent one outsorce data for advance thinking and interactions.

## 🚀 Features
- Tablet UI served on Pepper’s tablet.
- [in testing] bridge between tablet and robot.
- Motion control service (walk, turn, pose).
- Audio input/output handling.
- PC client for remote control.
- AI connection
- Entertainment

## 🛠 Requirements
- **Robot**: Pepper (NAOqi 2.5, Python 2.7)
- **PC**: Python 3.8+ for client tools
- Network: Pepper and PC on the same LAN

## 📂 Project Structure
    pepper_apps/
    ├─ apps/
    │ ├─ com.wonder.pepper.front/ ...           # front of page, used for login and user identify
    │ ├─ com.wonder.pepper.home/ ...            # home page, used for listing application
    │ └─ com.wonder.pepper.temp/ ...            # template for all apps
    ├─ deploy/
    │ ├─ git_update.py                              # update the folder to git
    │ └─ deploy.py                              # update all file in apps to pepper
    ├─ docs/
    │ ├─ protocal.md                            # protocals when encountor bugs
    │ └─ runbook.md                             # codes for what to run
    ├─ python_pc/
    │ ├─ open_pepper_exe/ ...                   # exe for simple users to use for open and closing pepper
    │ └─ tools/ ...                             # tools for debug and coding
    ├─ test/
    │ ├─ home11/ ...                            # example for a mini app system
    │ └─ test_name/                             # use for testing
    │   └─ README.md                            # info of this test
    ├─ LICENSE       
    ├─ TODO.md                                  # TODO list
    ├─ README.md                                # Project documentation
    └─ .gitignore                               # Git ignore rules for unnecessary files

## ⚙️ Setup & Deployment
1. Clone this repo:
   ```bash
   git clone https://github.com/osma146/pepper_project.git
   cd pepper-project
    ```
2. follow pepper_apps/docs/runbook.md

## 📋 TODO
See TODO.md for full task list.

## 🧩 Development Notes
>Notes, tips, or quirks to remember while developing.

Pepper tablet runs an old WebView → use ES5 JavaScript only.

Avoid CSS variables; use fixed colors or preprocessor.

Append ?ver=<timestamp> to tablet URLs to bust cache.

## 📜 License
This project is licensed under the MIT License — see LICENSE for details.