from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Set up the WebDriver (ensure ChromeDriver is in your PATH)
driver = webdriver.Chrome()

# List of Google Slides presentation URLs
presentation_urls = [
    'https://docs.google.com/presentation/1',
    'https://docs.google.com/presentation/2'
    # Replace with actual presentation URLs and add more as needed
]

def create_output_directory(presentation_name):
    """Create a directory for the given presentation name."""
    output_dir = os.path.join('slides_screenshots', presentation_name)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def capture_screenshots(url):
    """Capture screenshots from each slide in the presentation."""
    presentation_name = url.split('/')[-2]  # Extract presentation ID from URL
    output_dir = create_output_directory(presentation_name)
    
    driver.get(url)
    time.sleep(3)

    slide_index = 1
    while True:
        # Take a screenshot of the current slide
        screenshot_path = os.path.join(output_dir, f'slide_{slide_index}.png')
        driver.save_screenshot(screenshot_path)
        print(f'Screenshot saved: {screenshot_path}')

        # Check if the "Next" button is enabled before clicking
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.punch-viewer-navbar-next.goog-inline-block.goog-flat-button')
            if "disabled" in next_button.get_attribute("class"):
                print("No more slides available.")
                break  # Exit loop if "Next" button is disabled

            next_button.click()
            time.sleep(3)  # Wait for the next slide to load
            slide_index += 1  # Increment slide index only if navigation is successful

        except Exception as e:
            print(f'Error navigating to next slide: {e}')
            break  # Exit loop if there are no more slides or an error occurs

# Loop through each presentation URL and capture slides
for url in presentation_urls:
    capture_screenshots(url)

# Close the browser
driver.quit()