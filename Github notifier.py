import time
from plyer import notification

if __name__ == "__main__":

    notification.notify(
            title = "GITHUB commit notification",
            message = "It's time to commit on GITHUB!!",
            app_icon = "Danleech-Simple-Github.ico",
            timeout = 5

        )
    
  # We can use while loop to set the timer.
