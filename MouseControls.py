import pyautogui
import time

def move_mouse(x, y, duration):
    """
    Moves the mouse cursor from its current position by (x, y) over a specified duration.
    
    :param x: The distance to move the mouse along the x-axis.
    :param y: The distance to move the mouse along the y-axis.
    :param duration: The time (in seconds) over which to move the mouse.
    """
    start_x, start_y = pyautogui.position()
    end_x = start_x + x
    end_y = start_y + y
    
    steps = int(duration * 10)
    for i in range(steps):
        pyautogui.moveTo(
            start_x + (end_x - start_x) * (i + 1) / steps,
            start_y + (end_y - start_y) * (i + 1) / steps
        )
        time.sleep(duration / steps)

def click(button='left'):
    """
    Performs a mouse click with the specified button.
    
    :param button: The button to click, either 'left', 'right', or 'middle'. Defaults to 'left'.
    """
    if button not in ['left', 'right', 'middle']:
        raise ValueError("Button must be 'left', 'right', or 'middle'.")
    pyautogui.click(button=button)

def right_click():
    """
    Performs a right mouse click.
    """
    click('right')

def left_click():
    """
    Performs a left mouse click.
    """
    click('left')

def middle_click():
    """
    Performs a middle mouse click.
    """
    click('middle')