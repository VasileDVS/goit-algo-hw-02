import queue
import random
import time

# Initialize a queue to hold incoming requests
request_queue = queue.Queue()

# Function to create a new request
def create_request():
    # Generate a unique request ID
    request_id = random.randint(1, 1000)
    print(f"New request created: {request_id}")
    # Enqueue the request
    request_queue.put(request_id)

# Function to handle and process requests from the queue
def handle_request():
    # Check if there are any requests in the queue
    if not request_queue.empty():
        # Dequeue the next request
        request_id = request_queue.get()
        # Simulate request processing
        print(f"Handling request: {request_id}")
    else:
        # Indicate that the queue is currently empty
        print("No requests to process")

# Main loop to generate and process requests continuously
try:
    while True:
        # Generate a new request
        create_request()
        # Process a request from the queue
        handle_request()
        # Wait for a short period before the next iteration
        time.sleep(1)

except KeyboardInterrupt:
    # Gracefully handle the termination of the program
    print("Shutting down the application.")