import time
import random
from multiprocessing import Pool, cpu_count

from bilbasen_scraper import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def create_driver():
    options = Options()

    # Headless mode (new version is more stable)
    options.add_argument("--headless=new")

    # Window size (important for some sites)
    options.add_argument("--window-size=1920,1080")

    # Anti-detection flags
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Optional: fake user agent
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)

    # Remove webdriver flag
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    return driver


def scrape(url):
    driver = None
    try:
        driver = create_driver()

        driver.get(url)

        # Random delay (helps avoid detection)
        time.sleep(random.uniform(1.5, 3.0))

        html = driver.page_source

        result = {
            "url": url,
            "length": len(html),
            "has_props": "var _props" in html
        }

        return result

    except Exception as e:
        return {"url": url, "error": str(e)}

    finally:
        if driver:
            driver.quit()


def main():
    urls = [
        "https://www.bilbasen.dk/brugt/bil/suzuki/baleno/10-boosterjet-active-5d/6835994",
        "https://www.bilbasen.dk/brugt/bil/bmw/i4/edrive35-m-sport-5d/6826694",
        "https://www.bilbasen.dk/brugt/bil/mercedes/eqb250/progressive-advance-plus-5d/6826693",
        "https://www.bilbasen.dk/brugt/bil/vw/id4/77-pro-5d/6752582",
        "https://www.bilbasen.dk/brugt/bil/bmw/325d/30-touring-5d/5954095",
        "https://www.bilbasen.dk/brugt/bil/renault/clio-iv/09-tce-90-zen-sport-tourer-5d/6827295",
        "https://www.bilbasen.dk/brugt/bil/bmw/x5/30-xdrive30d-aut-5d/6694538",
        "https://www.bilbasen.dk/brugt/bil/skoda/enyaq/80-iv-sportline-5d/6771986",
        "https://www.bilbasen.dk/brugt/bil/hyundai/kona/64-ev-essential-5d/6661540",
        "https://www.bilbasen.dk/brugt/bil/mercedes/eqa350/amg-advance-4matic-5d/6759081",
        "https://www.bilbasen.dk/brugt/bil/nissan/leaf/62-e-n-connecta-5d/6843774",
        "https://www.bilbasen.dk/brugt/bil/skoda/scala/10-tsi-110-tour-de-france-dsg-5d/6843775",
        "https://www.bilbasen.dk/brugt/bil/citron/-c4/50-shine-5d/6767603",
        "https://www.bilbasen.dk/brugt/bil/mitsubishi/space-star/12-invite-5d/6681612",
        "https://www.bilbasen.dk/brugt/bil/bmw/x5/30-xdrive45e-m-sport-aut-5d/6636952",
        "https://www.bilbasen.dk/brugt/bil/opel/mokka-x/16-essentia-5d/6777445",
        "https://www.bilbasen.dk/brugt/bil/vw/id7/86-style-s-tourer-5d/6740070",
        "https://www.bilbasen.dk/brugt/bil/bmw/i5/m60-m-sport-xdrive-4d/6472346",
        "https://www.bilbasen.dk/brugt/bil/vw/t-cross/10-tsi-95-life-5d/6843770",
        "https://www.bilbasen.dk/brugt/bil/tesla/model-y/rwd-5d/6843768",
        "https://www.bilbasen.dk/brugt/bil/skoda/fabia/10-tsi-95-ambition-tour-combi-5d/6843769",
        "https://www.bilbasen.dk/brugt/bil/mini/cooper-se/classic-trim-3d/6843766",
        "https://www.bilbasen.dk/brugt/bil/mini/cooper-se/classic-3d/6839813",
        "https://www.bilbasen.dk/brugt/bil/suzuki/ignis/12-dualjet-active-5d/6826688"
    ]

    # Number of parallel workers (adjust based on your CPU)
    workers = min(10, cpu_count())

    with Pool(workers) as pool:
        results = pool.map(scrape, urls)

    for r in results:
        print(r)


if __name__ == "__main__":
    main()