import time
import threading

class Chronometer:
    def __init__(self):
        self.current_time_unit = 0
        self.stop_timer = False
        self._thread = None
        self.total_time_elapsed = 0
        self.total_time = []

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
            self.total_time_elapsed += 1 
            # print(f"Current time unit is {self.current_time_unit}")
            # time.sleep(0.5)
            time.sleep(0.1)


    def get_current_time(self):
        """
        This function provides the current time unit.
        """
        return self.current_time_unit
    
    def get_total_time(self):
        """
        This function provides the total time unit.
        """
        self.total_time.append(self.total_time_elapsed)
        return self.total_time_elapsed        

    def stop(self):
        """
        This function stops the timer.
        """
        self.stop_timer = True
        if self._thread:
            self._thread.join()        