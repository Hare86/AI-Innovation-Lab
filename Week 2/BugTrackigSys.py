

class BugTracker:
    def __init__(self):
        self.bugs = {}

    def add_bug(self, bug_id, description, severity):
        self.bugs[bug_id] = {
            "description": description,
            "severity": severity,
            "status": "Open"
        }

    def update_status(self, bug_id, new_status):
        if bug_id in self.bugs:
            self.bugs[bug_id]["status"] = new_status
        else:
            print(f"Bug ID {bug_id} not found.")

    def list_all_bugs(self):
        print("Bug Records:")
        for bug_id, details in self.bugs.items():
            print(f"Bug ID: {bug_id}")
            print(f"  Description: {details['description']}")
            print(f"  Severity: {details['severity']}")
            print(f"  Status: {details['status']}")
            print("-" * 30)


if __name__ == "__main__":
    
    tracker = BugTracker()

    
    tracker.add_bug("BUG001", "Login button not working", "High")
    tracker.add_bug("BUG002", "Typo in homepage title", "Low")
    tracker.add_bug("BUG003", "Crash on submitting form", "Critical")

    
    tracker.update_status("BUG001", "In Progress")
    tracker.update_status("BUG003", "Closed")

    
    tracker.list_all_bugs()
