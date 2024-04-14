# start.py

import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
import getindianname as name

async def start(thread_name, wait_time, meetingcode, passcode, zoom_base_url):
    user = name.randname()  # Generate a random Indian name using getindianname
    print(f"{thread_name} started! User: {user}")

    browser = await launch(
        headless=True,
        executablePath='/usr/bin/brave-browser',  # Specify the correct browser executable path
        args=['--no-sandbox', '--disable-dev-shm-usage']
    )
    page = await browser.newPage()

    # Apply pyppeteer-stealth to mimic a real browser
    await stealth(page)

    await page.goto(f'{zoom_base_url}/wc/join/{meetingcode}')

    try:
        await page.click('//button[@id="onetrust-accept-btn-handler"]', timeout=5000)
    except Exception as e:
        pass

    try:
        await page.click('//button[@id="wc_agree1"]', timeout=5000)
    except Exception as e:
        pass

    try:
        await page.waitForSelector('input[type="text"]', timeout=200000)
        await page.type('input[type="text"]', user)
        await page.type('input[type="password"]', passcode)
        join_button = await page.waitForSelector('button.preview-join-button', timeout=200000)
        await join_button.click()
    except Exception as e:
        pass

    try:
        # Wait for the "Join Audio by Computer" button to become visible
        join_audio_button = await page.waitForXPath('//button[contains(text(), "Join Audio by Computer")]', timeout=400000)
        await join_audio_button.click()
        print(f"{thread_name} mic aayenge.")
    except Exception as e:
        print(f"{thread_name} mic nahe aayenge. ", e)

    # ... (other code)

    print(f"{thread_name} sleep for {wait_time} seconds ...")
    await asyncio.sleep(wait_time)
    print(f"{thread_name} ended!")

    await browser.close()
