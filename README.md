Advanced reCAPTCHA v3 Human Emulation with Playwright
A sophisticated Python script that simulates human-like behavior to interact with reCAPTCHA v3 test pages. This project demonstrates advanced browser automation techniques including realistic mouse movements, random delays, and stealth configurations.

📋 Features
Realistic Mouse Movements: Uses Bezier curves to simulate natural human mouse paths

Stealth Configuration: Multiple browser fingerprint modifications to avoid detection

Human-like Behavior: Random delays, scrolling patterns, and interaction sequences

reCAPTCHA v3 Testing: Specifically designed for reCAPTCHA v3 test pages

Score Analysis: Returns the reCAPTCHA score for performance evaluation

🚀 Quick Start
Prerequisites
Python 3.7+

Playwright

Installation
bash
# Clone the repository
git clone https://github.com/ahmedelseseiy/recaptcha-human-emulation.git
cd recaptcha-human-emulation

# Install dependencies
pip install playwright
playwright install chromium
Usage
bash
python recaptcha_human_emulation.py
📁 Project Structure
text
recaptcha-human-emulation/
│
├── recaptcha_human_emulation.py    # Main script
├── README.md                        # Documentation
├── requirements.txt                  # Dependencies
└── .gitignore                        # Git ignore file
requirements.txt
text
playwright>=1.40.0
🔧 How It Works
The script uses Playwright to control a Chromium browser with multiple stealth techniques:

Browser Launch: Starts Chromium with automation-disabling flags

Fingerprint Modification: Injects JavaScript to modify browser properties

Human Emulation: Simulates mouse movements using Bezier curves

Interaction: Navigates to the target page and clicks the reCAPTCHA button

Score Retrieval: Parses and displays the reCAPTCHA v3 score

📊 Understanding reCAPTCHA Scores
reCAPTCHA v3 returns a score between 0.0 and 1.0:

Score Range	Interpretation
0.9 - 1.0	Very likely human
0.7 - 0.9	Likely human
0.3 - 0.7	Suspicious
0.0 - 0.3	Likely bot
🎯 Factors That Influence the Score
Parameters That IMPROVE the Score ✓
Parameter	Implementation	Impact
Realistic Mouse Movement	Bezier curves with control points	High
Random Delays	time.sleep(random.uniform(0.003, 0.01))	Medium
Browser Fingerprint	Modified navigator properties	High
WebGL Fingerprint	Custom GPU vendor strings	Medium
Viewport Size	Maximized window	Low
Interaction Timing	Variable delays between actions	Medium
Parameters That LOWER the Score ✗
Parameter	Why It's Detected	Avoidance
Direct Clicking	No mouse movement between points	Always use Bezier curves
Fixed Delays	Predictable timing patterns	Use random.uniform()
Missing Chrome Object	window.chrome is undefined	Add chrome.runtime
navigator.webdriver	Flag set to true	Override to undefined
Plugins Array	Empty in headless browsers	Populate with realistic values
Languages Array	Too few or unnatural	Use ['en-US', 'en', 'ar']
Hardware Concurrency	Often 2 in VMs	Set to 4-8
Device Memory	Often undefined	Set to 4-8 GB
Platform	Headless gives different values	Set to 'Win32'
🛠️ Key Stealth Techniques Explained
1. WebDriver Concealment
javascript
Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
2. Chrome Object Emulation
javascript
window.chrome = { runtime: {}, app: {}, csi: function() {}, loadTimes: function() {} };
3. Plugin Array Simulation
javascript
Object.defineProperty(navigator, 'plugins', {get: () => [
    {name: 'Chrome PDF Plugin'},
    {name: 'Chrome PDF Viewer'},
    {name: 'Native Client'}
]});
4. WebGL Fingerprinting
javascript
const getParameter = WebGLRenderingContext.prototype.getParameter;
WebGLRenderingContext.prototype.getParameter = function(parameter) {
    if (parameter === 37445) return 'Intel Inc.';
    if (parameter === 37446) return 'Intel UHD Graphics';
    return getParameter(parameter);
};
5. Bezier Curve Mouse Movement
python
def bezier_curve(start, end, control1, control2, steps=40):
    points = []
    for i in range(steps):
        t = i / steps
        x = (1-t)**3 * start[0] + 3*(1-t)**2*t * control1[0] + 3*(1-t)*t**2 * control2[0] + t**3 * end[0]
        y = (1-t)**3 * start[1] + 3*(1-t)**2*t * control1[1] + 3*(1-t)*t**2 * control2[1] + t**3 * end[1]
        points.append((x, y))
    return points
📈 Performance Optimization Tips
Increase Randomness: Vary delay ranges and movement patterns

Session Rotation: Close and restart browsers periodically

IP Rotation: Use proxies for distributed testing

Browser Profile: Use persistent contexts with real user data

Timing Variations: Add longer pauses between actions (2-5 seconds)

⚠️ Legal and Ethical Considerations
This tool is for educational purposes only. Always:

Respect website terms of service

Check robots.txt before scraping

Implement rate limiting

Use ethically and responsibly

Comply with local laws and regulations

🤝 Contributing
Contributions are welcome! Feel free to:

Open issues for bugs or suggestions

Submit pull requests with improvements

Share your test results and findings

📝 License
MIT License - see LICENSE file for details

🙏 Acknowledgments
Playwright team for the excellent automation framework

reCAPTCHA for providing the test page

Open source community for stealth techniques
