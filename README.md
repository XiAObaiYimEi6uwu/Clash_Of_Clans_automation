# Clash_Of_Clans_automation

A starting point for automating interactions with Clash of Clans (research/automation tooling).

Features
- Screen scanning and image recognition using pyautogui
- Automated clicks and troop deployment
- Configurable coordinates and bias for natural input
- Example automation sequences for battle flow

## Quickstart

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate     # Windows (PowerShell)
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


3. Make sure all required image files are downloaded and saved in the same folder as script.py
      - attack_map.png
      - find_match.png
      - battle_button.png
      - q.png
      - w.png
      - e.png
      - r.png
      - a.png
      - z.png
      - esc.png
      - surrender_button.png
      - return_home.png


4. Run the main script:
   ```bash
   python -script.py


