class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://practicetestautomation.com/practice-test-login/"
        self.userame_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.submit_button = page.locator('#submit')
        self.error_banner = page.locator('#error')
        self.login_success = page.locator('h1.post-title')
        self.logout_button = page.locator("a:has-text('Log out')")

    def navigate(self):
        self.page.goto(self.url, wait_until="domcontentloaded")

    def login(self, username, password):
        self.userame_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click(no_wait_after=True)
