import os


def take_screenshot(driver, name):

    os.makedirs("screenshots", exist_ok=True)

    path = f"screenshots/{name}.png"

    driver.save_screenshot(path)

    return path
