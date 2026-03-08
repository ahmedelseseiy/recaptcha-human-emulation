# Human-Like reCAPTCHA v3 Interaction Tester

This project demonstrates how browser automation can simulate **human-like interaction patterns** in order to evaluate **Google reCAPTCHA v3 scoring behavior**.

The script uses **Playwright** and implements several techniques that mimic real user behavior such as:

* Human-like mouse movement using **Bezier curves**
* Randomized interaction timing
* Browser fingerprint masking
* Natural scrolling and cursor positioning
* Realistic click targeting

The goal is to analyze how these behaviors affect the **reCAPTCHA v3 score** returned by the verification endpoint.

---

# Overview

Google reCAPTCHA v3 assigns a **risk score** between:

```
0.0 → very likely bot
1.0 → very likely human
```

Instead of solving a challenge, the system evaluates behavioral signals such as:

* Mouse movement
* Timing between actions
* Browser fingerprint
* Interaction patterns
* Network reputation

This script reproduces these signals to test how they influence the returned score.

---

# Features

### Human-like Mouse Movement

The script generates cursor paths using **Bezier curves**, which resemble real human hand movement instead of linear bot movement.

Key function:

```
bezier_curve(start, end, control1, control2)
```

It generates a smooth path between two points with random control points.

---

### Randomized Behavior

The script introduces randomness in several areas:

* Mouse movement paths
* Delay between actions
* Scroll distance
* Click position inside the button

This prevents deterministic automation patterns.

Example:

```
time.sleep(random.uniform(0.5, 1.5))
```

---

### Browser Fingerprint Masking

The script modifies browser properties to resemble a normal Chrome browser.

Examples:

* `navigator.webdriver` removed
* Realistic `navigator.plugins`
* Realistic `navigator.languages`
* Hardware properties
* WebGL GPU vendor

Example snippet:

```
Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
```

---

### Human-like Clicking

Instead of clicking the center of the button every time, the script clicks **a random point inside the button**.

```
x = box['x'] + box['width'] * random.uniform(0.3, 0.7)
y = box['y'] + box['height'] * random.uniform(0.3, 0.7)
```

This mimics natural user behavior.

---

# How the Score is Collected

After clicking the button:

```
result = page.locator("#out").text_content()
score = json.loads(result).get('google_response', {}).get('score')
```

The script extracts the **reCAPTCHA v3 score** from the JSON response printed on the page.

Example output:

```
0.9
```

---

# Parameters That Affect reCAPTCHA Score

Several behavioral and environment parameters influence the score.

## 1 Mouse Movement Quality

Function:

```
human_mouse_move()
```

Important parameter:

```
steps=40
```

Higher steps → smoother movement → more human-like.

Lower steps → robotic movement → lower score.

---

## 2 Timing Between Actions

Example:

```
time.sleep(random.uniform(2,4))
```

More natural delays typically increase the score.

Very fast execution may reduce the score.

---

## 3 Interaction Count

The script performs multiple mouse movements before clicking:

```
for _ in range(random.randint(2,3)):
```

More interaction signals → higher trust.

---

## 4 Scroll Behavior

```
window.scrollTo(...)
```

Scrolling is a strong signal that the user is actively browsing.

No scrolling may reduce score.

---

## 5 Click Accuracy

Instead of clicking the exact center:

```
random.uniform(0.3, 0.7)
```

This simulates human hand imprecision.

Bots often click exact coordinates.

---

## 6 Browser Fingerprint

Modified properties include:

* `navigator.webdriver`
* `navigator.plugins`
* `navigator.languages`
* `hardwareConcurrency`
* `deviceMemory`
* WebGL vendor

These reduce bot detection.

---

# How to Increase the Score

To achieve higher scores:

### Increase movement complexity

```
steps = 60
```

### Add more user activity

```
for _ in range(5):
```

### Add longer delays

```
sleep 3–6 seconds
```

### Simulate more interactions

* extra scrolling
* hovering elements
* clicking non-critical UI elements

### Use residential proxies or real IP addresses

Network reputation significantly affects reCAPTCHA scoring.

---

# How to Lower the Score (Bot Simulation)

To simulate bot-like behavior:

### Remove mouse movement

Click instantly.

### Reduce delays

```
sleep(0)
```

### Use headless browser

```
headless=True
```

### Disable scrolling

### Use linear mouse movement

```
page.mouse.move(x,y)
```

These patterns often produce scores close to **0.1**.

---

# Requirements

Install dependencies:

```
pip install playwright
playwright install
```

---

# Run the Script

```
python script.py
```

The script will:

1. Launch the browser
2. Simulate human interaction
3. Click the verification button
4. Print the returned score

Example output:

```
0.9
```

---

# Disclaimer

This project is intended **only for research and testing purposes** to understand how behavioral signals affect **reCAPTCHA v3 scoring**.
It should not be used to bypass or abuse CAPTCHA protections.

---


reCAPTCHA for providing the test page

Open source community for stealth techniques
