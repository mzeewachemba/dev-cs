import time
import threading

class Chronometer:
    def __init__(self):
        self.current_time_unit = 0
        self.stop_timer = False
        self._thread = None

    def start(self):
        if not self._thread or not self._thread.is_alive():
            self.stop_timer = False
            self._thread = threading.Thread(target=self.run)
            self._thread.start()

    def run(self):
        """
        This function runs the timer.
        """
        while not self.stop_timer:
            self.current_time_unit += 1
            print(f"Current time unit is {self.current_time_unit}")
            time.sleep(0.5)

    def get_current_time(self):
        """
        This function provides the current time unit.
        """
        return self.current_time_unit

    def stop(self):
        """
        This function stops the timer.
        """
        self.stop_timer = True
        if self._thread:
            self._thread.join()

if __name__ == "__main__":
    chronometer = Chronometer()
    chronometer.start()


        while True:
            # Check the current time every 0.1 seconds
            time.sleep(0.1)
            current_time = chronometer.get_current_time()
            if current_time == 5:
                print(f"Current time (accessed from main): {current_time}")
                chronometer.stop()
                print("Chronometer stopped.")
                break
