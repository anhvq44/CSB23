# De: tao chuc nang forward, backward cho web browser
# su dung 2 stack de luu
# Lop Browser: visit_page, back, forward

class Browser:
    def __init__(self):
        self.current_page = "Home"
        self.back_history = []
        self.forward_history = []
        
    def visit_page(self, page_name):
        self.back_history.append(self.current_page)
        self.current_page = page_name
        self.forward_history.clear()
        return f'Visited: {self.current_page}'
        
    def back(self):
        if not self.back_history:
            return "No back history"
        self.forward_history.append(self.current_page)
        self.current_page = self.back_history.pop()
        return f"Back to: {self.current_page}"
        
    def forward(self):
        if not self.forward_history: return "No forward history"
        self.back_history.append(self.current_page)
        self.current_page = self.forward_history.pop()
        return f"Forward to: {self.current_page}"
        
def testdrive():
    browser = Browser()
    
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'
    
    function_table = """ Use number 1, 2, 3, 4 to navigate:
    1. Visit page: Input page name
    2. <- Back
    3. -> Forward
    4. Exit
    """
    request = ""
    print(function_table)
    request = input(f"{BLUE}Request number: {RESET}")
    while request != "4":
        match request:
            case "1":
                page_name = input(f"{BLUE}Page name: {RESET}").strip()
                if not page_name:
                    print(f"{RED}Page name can not be empty {RESET}")
                    request = ""
                    continue
                print(browser.visit_page(page_name))
            case "2":
                print(browser.back())
            case "3":
                print(browser.forward())
            case _:
                print(f"{RED}Invalid request number. Please try again {RESET}")
        print(" ")
        request = input(f"{BLUE}Request number: {RESET}")
    print(f"{GREEN}Exit program.{RESET}")
                
testdrive()