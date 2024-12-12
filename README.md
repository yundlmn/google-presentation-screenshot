# google-presentation-screenshot
A script to capture screenshots from Google Slides presentations

# Requirements

- Python 3.12
- Selenium

# Installation

1. Clone the repository:
   
   git clone https://github.com/yundlmn/google-presentation-screenshot.git
   
   cd google-presentation-screenshot

2. Install required Python packages:
   
   pip install selenium

3. Ensure you have ChromeDriver installed and it's in your PATH.
   
   pip install chromedriver-py

# Usage

1. Update the presentation_urls list in the script with the URLs of your Google Slides presentations.

2. Run the script:
   
   python screenshot_script.py

3. Screenshots will be saved in separate directories within slides_screenshots.

# Project Structure
google-presentation-screenshot/
│
├── screenshot_script.py
├── README.md
└── slides_screenshots/
