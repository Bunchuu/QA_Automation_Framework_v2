class ProgressBar:
    def __init__(self, page):
        self.page = page
        self.url = "http://uitestingplayground.com/progressbar"
        self.start_location = page.locator('#startButton')
        self.stop_location = page.locator('#stopButton')
        self.progress_bar = page.locator('#progressBar')
        self.result = page.locator('#result')

    def navigate(self):
        self.page.goto(self.url, wait_until="domcontentloaded")

    def start(self):
        self.start_location.click()

    def stop(self):
        self.stop_location.click()

    def wait_for_threshold(self, threshold: int = 75):
        while True:
            value = int(self.progress_bar.get_attribute("aria-valuenow"))
            if value >= threshold:
                break
        self.page.wait_for_timeout(50)
