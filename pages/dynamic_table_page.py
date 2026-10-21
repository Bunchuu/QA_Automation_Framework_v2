class DynamicTablePage:
    def __init__(self, page):
        self.page = page
        self.url = "http://uitestingplayground.com/dynamictable"
        self.headers = page.get_by_role("columnheader")
        self.rows = page.get_by_role("row")
        self.warning_label = page.locator(".bg-warning")

    def navigate(self):
        self.page.goto(self.url)

    def get_chrome_cpu_from_table(self) -> str:
        header_texts = self.headers.all_inner_texts()
        cpu_index = header_texts.index("CPU")
        chrome_row = self.rows.filter(has_text="Chrome")
        cpu_cell = chrome_row.get_by_role("cell").nth(cpu_index)
        return cpu_cell.inner_text()

    def get_warning_text(self) -> str:
        return self.warning_label.inner_text()