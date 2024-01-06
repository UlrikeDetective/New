import schedule
import time
import os

def open_reminder_file(file_path):
    # Open the reminder file
    try:
        os.system(f'open {/Users/ulrike_imac_air/projects/Trial_and_error/goals/goals.txt}')  # Using f-string for file path
    except Exception as e:
        print(f"Error: {e}")

def schedule_reminder(file_path):
    # Schedule reminder every week on Sunday at 10 am
    schedule.every().sunday.at("10:00").do(open_reminder_file, file_path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    file_path = "/Users/ulrike_imac_air/projects/Trial_and_error/goals/goals.txt"
    
    schedule_reminder(file_path)
