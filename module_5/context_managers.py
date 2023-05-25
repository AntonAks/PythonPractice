import time

""" Example 1: Timer context manager to measure code execution time: """
class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")

# Usage
with Timer():
    # Code block to measure execution time
    time.sleep(2)


""" Example 2: Database connection context manager: """
class DatabaseConnection:
    def __enter__(self):
        # Perform database connection setup
        print("Connecting to the database...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Perform database connection teardown
        print("Disconnecting from the database")


# Usage
with DatabaseConnection():
    # Code block that requires a database connection
    print("Executing SQL queries...")



""" Example 3: Context manager for acquiring and releasing resources: """
class ResourceManager:
    def __enter__(self):
        # Acquire the resource
        print("Acquiring the resource...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Release the resource
        print("Releasing the resource")


# Usage
with ResourceManager():
    # Code block that requires the resource
    print("Performing operations with the resource...")
