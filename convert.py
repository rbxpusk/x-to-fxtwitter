import pyperclip
import time
import re
import threading

def convert_twitter_link(url):
    """
    Convert standard Twitter/X links to FxTwitter links.
    
    Args:
        url (str): The original Twitter/X link
    
    Returns:
        str: Converted FxTwitter link or original URL if not a valid Twitter link
    """
    twitter_pattern = r'^https?://(www\.)?(x|twitter)\.com/([^/]+)/status/(\d+)'
    
    match = re.match(twitter_pattern, url)
    if match:
        converted_url = f'https://fxtwitter.com/{match.group(3)}/status/{match.group(4)}'
        return converted_url
    
    return url

def clipboard_monitor():
    """
    Continuously monitor clipboard for Twitter links and convert them.
    """
    previous_clipboard = pyperclip.paste()
    
    while True:
        try:
            current_clipboard = pyperclip.paste()
            
            if current_clipboard != previous_clipboard:
                converted_link = convert_twitter_link(current_clipboard)
                
                if converted_link != current_clipboard:
                    pyperclip.copy(converted_link)
                    print(f"Converted: {current_clipboard} → {converted_link}")
                
                previous_clipboard = current_clipboard
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
        time.sleep(0.5)

def main():
    print("Converting links started")
    print("Press Ctrl+C to exit.")
    
    try:
        clipboard_monitor()
    
    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped.")

if __name__ == "__main__":
    main()
    
