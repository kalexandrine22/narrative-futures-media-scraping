from asyncio import run
from playwright.async_api import async_playwright

USER_AGENT = " ".join(
    [
        "Mozilla/5.0",
        "(Windows NT 10.0; Win64; x64)",
        "AppleWebKit/537.36",
        "(KHTML, like Gecko)",
        "Chrome/128.0.0.0",
        "Safari/537.36",
    ]
)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(user_agent=USER_AGENT)

        page = await context.new_page()

        await page.goto("https://taz.de/")
        await page.screenshot(path ='playwright_result.png')
        await context.close()
        await browser.close()

if __name__ == "__main__":
    run(main())
