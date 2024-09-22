from collections import deque
from datetime import datetime, timedelta
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.requests = {}
        self.max_requests = max_requests
        self.time_window = timedelta(seconds=time_window)
        self.lock = Lock()

    def allow_request(self, user_id):
        with self.lock:
            now = datetime.now()
            if user_id not in self.requests:
                self.requests[user_id] = deque()

            # Remove requests that are outside the time window
            while self.requests[user_id] and self.requests[user_id][0] < now - self.time_window:
                self.requests[user_id].popleft()

            # Check if the user has quota to make a new request
            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(now)
                return True
            else:
                return False

    def __cleanup(self, user_id):
        # Optional: Clean up request history for users who haven't made requests for a while
        if not self.requests[user_id]:
            del self.requests[user_id]

# Example Usage
rate_limiter = RateLimiter(max_requests=5, time_window=60)

def make_request(user_id: str):
    if rate_limiter.allow_request(user_id):
        print(f"Request from {user_id} allowed.")
    else:
        print(f"Request from {user_id} denied.")

# Testing with multiple requests
user_id = "user_1"
for i in range(7):  # Trying 7 requests
    make_request(user_id)
