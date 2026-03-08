from playwright.sync_api import sync_playwright
import time
import random
import json
import math

def bezier_curve(start, end, control1, control2, steps=40):
    points = []
    for i in range(steps):
        t = i / steps
        x = (1-t)**3 * start[0] + 3*(1-t)**2*t * control1[0] + 3*(1-t)*t**2 * control2[0] + t**3 * end[0]
        y = (1-t)**3 * start[1] + 3*(1-t)**2*t * control1[1] + 3*(1-t)*t**2 * control2[1] + t**3 * end[1]
        points.append((x, y))
    return points

def human_mouse_move(page, target_x, target_y):
    # نقطة البداية
    start = page.evaluate("({x: window.mouseX || 500, y: window.mouseY || 300})")
    
    # نقاط تحكم لمنحنى طبيعي
    control1 = (start['x'] + (target_x - start['x']) * 0.3 + random.randint(-30, 30),
                start['y'] + (target_y - start['y']) * 0.2 + random.randint(-20, 20))
    control2 = (start['x'] + (target_x - start['x']) * 0.7 + random.randint(-30, 30),
                start['y'] + (target_y - start['y']) * 0.8 + random.randint(-20, 20))
    
    points = bezier_curve((start['x'], start['y']), (target_x, target_y), control1, control2)
    
    for x, y in points:
        page.mouse.move(x, y)
        time.sleep(random.uniform(0.003, 0.01))
    
    page.evaluate(f"window.mouseX = {target_x}; window.mouseY = {target_y}")

with sync_playwright() as p:
    # تشغيل المتصفح
    browser = p.chromium.launch(
        headless=False,
        args=['--start-maximized', '--disable-blink-features=AutomationControlled']
    )
    
    page = browser.new_page()
    
    # تخفي متقدم
    page.add_init_script("""
        // إخفاء WebDriver
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        
        // كائن Chrome حقيقي
        window.chrome = { runtime: {}, app: {}, csi: function() {}, loadTimes: function() {} };
        
        // إضافات حقيقية
        Object.defineProperty(navigator, 'plugins', {get: () => [{name: 'Chrome PDF Plugin'}, {name: 'Chrome PDF Viewer'}, {name: 'Native Client'}]});
        
        // لغات
        Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en', 'ar']});
        
        // Hardware
        Object.defineProperty(navigator, 'hardwareConcurrency', {get: () => 8});
        Object.defineProperty(navigator, 'deviceMemory', {get: () => 8});
        Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
        
        // WebGL fingerprint
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {
            if (parameter === 37445) return 'Intel Inc.';
            if (parameter === 37446) return 'Intel UHD Graphics';
            return getParameter(parameter);
        };
        
        // تتبع الماوس
        window.mouseX = window.mouseY = 0;
        document.addEventListener('mousemove', e => { window.mouseX = e.clientX; window.mouseY = e.clientY; });
    """)
    
    # فتح الموقع
    page.goto("https://cd.captchaaiplus.com/recaptcha-v3-2.php")
    page.wait_for_function("typeof grecaptcha !== 'undefined'", timeout=10000)
    time.sleep(random.uniform(2, 4))
    
    # حركات عشوائية
    for _ in range(random.randint(2, 3)):
        human_mouse_move(page, random.randint(300, 1500), random.randint(200, 700))
        time.sleep(random.uniform(0.5, 1.5))
    
    # تمرير
    page.evaluate(f"window.scrollTo(0, {random.randint(200, 400)})")
    time.sleep(random.uniform(0.5, 1))
    
    # الضغط على الزر
    button = page.locator("#btn").first
    box = button.bounding_box()
    if box:
        x = box['x'] + box['width'] * random.uniform(0.3, 0.7)
        y = box['y'] + box['height'] * random.uniform(0.3, 0.7)
        
        human_mouse_move(page, x-40, y-15)
        time.sleep(random.uniform(0.2, 0.4))
        human_mouse_move(page, x, y)
        time.sleep(random.uniform(0.1, 0.2))
        page.mouse.click(x, y)
    
    # انتظار النتيجة
    time.sleep(3)
    
    # طباعة السكور فقط
    result = page.locator("#out").text_content()
    score = json.loads(result).get('google_response', {}).get('score')
    print(score)
    
    input()
    browser.close()