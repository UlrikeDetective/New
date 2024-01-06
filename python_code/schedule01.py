import schedule
import time
import os

def open_reminder_file(file_path):
    # Open the reminder file
    try:
        os.system(f'open {Users/ulrike_imac_air/projects/Trial_and_error/Stories/data_story.txt}')  # Using f-string for file path
    except Exception as e:
        print(f"Error: {e}")

def schedule_reminder(file_path, reminder_time):
    schedule.every().day.at(reminder_time).do(open_reminder_file, file_path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    file_path = "/Users/ulrike_imac_air/projects/Trial_and_error/Stories/data_story.txt"
    reminder_time = "21:15"  # Set the time to open the file (in HH:MM format)
    
    schedule_reminder(file_path, reminder_time)
