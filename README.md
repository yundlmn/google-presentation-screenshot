# google-presentation-screenshot
A script to capture screenshots from Google Slides presentations. In the event of limited access and not being able to download a presentation from Google Slides - this will allow to automatically take screenshots of slides from multiple presentation URLs and place it into separate folders on your machine.

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
   
   python google-presentation-screenshot.py

3. Screenshots will be saved in separate directories within slides_screenshots.

# Project Structure

google-presentation-screenshot/
│
├── google-presentation-screenshot.py
├── README.md
└── slides_screenshots/
