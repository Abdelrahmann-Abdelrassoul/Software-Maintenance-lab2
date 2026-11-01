"""Screenshot the SonarQube dashboard and issues page (logs in as admin)."""
import os
from playwright.sync_api import sync_playwright

URL = "http://localhost:9000"
PW = os.environ["SONAR_PW"]
os.makedirs("results", exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 1000})
    pg.goto(f"{URL}/sessions/new")
    pg.fill("input[name=login], #login-input", "admin")
    pg.fill("input[name=password], #password-input", PW)
    pg.keyboard.press("Enter")
    pg.wait_for_timeout(5000)
    for name, path in [("dashboard", "/dashboard?id=flasky"),
                       ("issues", "/project/issues?id=flasky&resolved=false"),
                       ("hotspots", "/security_hotspots?id=flasky")]:
        pg.goto(URL + path)
        pg.wait_for_timeout(8000)
        pg.screenshot(path=f"results/{name}.png", full_page=True)
    b.close()
