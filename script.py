import time
import pyautogui as pag
import random
from pynput.keyboard import Key, Controller
import os
from pynput import keyboard

pag.FAILSAFE = True
kb = Controller()

# --- Helper Functions ---
def on_press(key):
    try:
        if key == keyboard.Key.f9:
            print("F9 pressed, exiting program.")
            os._exit(0)
    except Exception:
        pass

def press_esc(delay=0.05):
    kb.press(Key.esc)
    time.sleep(delay)
    kb.release(Key.esc)

def press_together(keys, hold_time=0.2):
    # Press all keys down
    for k in keys:
        kb.press(k)
    time.sleep(hold_time)
    # Release all keys
    for k in keys:
        kb.release(k)

def scan_and_click(image_path, confidence=0.65, max_retries=10, delay=0.09, post_wait=0.05):
    """Scan screen for an image and click its center if found."""
    for attempt in range(max_retries):
        try:
            location = pag.locateOnScreen(image_path, confidence=confidence)
        except pag.ImageNotFoundException:
            location = None
        if location:
            point = pag.center(location)
            pag.moveTo(point, duration=0.1)
            pag.click()
            print(f"Clicked {image_path}")
            time.sleep(post_wait + random.uniform(0.2, 0.5))
            return True
        time.sleep(delay)
    print(f"Could not find {image_path}")
    return False

def generate_line_points(p1, p2, num_points=11, bias=5):
    """Generate evenly spaced points between p1 and p2 with gradient and bias."""
    x1, y1 = p1
    x2, y2 = p2
    points = []
    for i in range(num_points):
        t = i / (num_points - 1)
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        x += random.randint(-bias, bias)
        y += random.randint(-bias, bias)
        points.append((int(x), int(y)))
    return points

def click_position(pos, delay=0.01):
    pag.moveTo(pos[0], pos[1], duration=0.05)
    pag.click()
    time.sleep(delay + random.uniform(0.02, 0.08))

def click_center_screen(num_clicks=11, bias=20):
    """
    Click around the center of the screen with small random offsets.
    num_clicks = how many clicks to perform
    bias = max random offset in pixels from center
    """
    screen_width, screen_height = pag.size()
    center_x, center_y = screen_width // 2, screen_height // 2

    for i in range(num_clicks):
        x = center_x + random.randint(-bias, bias)
        y = center_y + random.randint(-bias, bias)
        pag.moveTo(x, y, duration=0.05)
        pag.click()
        time.sleep(0.01 + random.uniform(0.02, 0.08))
        print(f"Clicked at ({x}, {y}) around center")

# --- Main Sequence ---
def main():
    while True:

        # Step 1: Scan for attack map
        scan_and_click("attack_map.png")
        # Step 2: Scan for find match
        scan_and_click("find_match.png")
        # Step 3: Scan for battle button
        scan_and_click("battle_button.png")
        # Step 4: Provide two coordinates for each direction
        top_start, top_end       = (417,735), (1364,63)
        bottom_start, bottom_end = (1531,81), (2372,730)
        left_start, left_end     = (365,938), (1218,1568)
        right_start, right_end   = (1635,1586), (2483,926)
        # Step 5: Generate 11 points per line
        top_points    = generate_line_points(top_start, top_end)
        bottom_points = generate_line_points(bottom_start, bottom_end)
        left_points   = generate_line_points(left_start, left_end)
        right_points  = generate_line_points(right_start, right_end)
        # Step 6: Replay sequence
        time.sleep(2)
        scan_and_click("1.png")
        for p in top_points: click_position(p)
        for p in bottom_points: click_position(p)
        for p in left_points: click_position(p)
        for p in right_points: click_position(p)
        scan_and_click("q.png")
        for p in top_points[3:6]: click_position(p)
        scan_and_click("w.png")
        for p in right_points[4:7]: click_position(p)
        scan_and_click("e.png")
        for p in bottom_points[4:7]: click_position(p)
        scan_and_click("r.png")
        for p in left_points[4:7]: click_position(p)
        press_together(['q', 'w', 'e', 'r'], hold_time=0.3)
        scan_and_click("a.png")
        click_center_screen(num_clicks=11, bias=300)
        scan_and_click("z.png")
        click_position(right_points[5])
        time.sleep(10)
        # Step 7: Scan for surrender and return home
        press_esc(delay=0.05)
        scan_and_click("ok.png")
        scan_and_click("return_home.png")
        print("Automation sequence complete.")


listener = keyboard.Listener(on_press=on_press)
listener.start()



if __name__ == "__main__":
    print("Program running... Press F9 to quit.")
    time.sleep(3)
    main()










