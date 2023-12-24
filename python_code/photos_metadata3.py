import os
import csv
from PIL import Image, ExifTags

def get_exif_data(image_path):
    img = Image.open(image_path)
    exif_data = img._getexif()
    gps_info = exif_data.get(34853)  # GPSInfo tag number
    date_time = exif_data.get(36867)  # DateTimeOriginal tag number

    gps_data = None
    date_data = None
    time_data = None

    if gps_info:
        gps_data = f"{gps_info[2][0]}° {gps_info[2][1]}' {gps_info[2][2]}'' {gps_info[1]}, {gps_info[4][0]}° {gps_info[4][1]}' {gps_info[4][2]}'' {gps_info[3]}, Altitude: {gps_info[6]}"
    
    if date_time:
        date_time_original = date_time.split()  # Splitting date and time
        date_data = date_time_original[0]
        time_data = date_time_original[1]

    return gps_data, date_data, time_data

if __name__ == "__main__":
    folder_path = "/Users/ulrike_imac_air/Downloads/Sitzen"  # Replace with the folder containing your images
    csv_file_path = "exif_gps_date_time.csv"

    csv_columns = ['ImageName', 'GPSData', 'Date', 'Time']

    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()

        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # Check if it's an image file
                image_path = os.path.join(folder_path, filename)
                gps_data, date_data, time_data = get_exif_data(image_path)
                writer.writerow({'ImageName': filename, 'GPSData': gps_data, 'Date': date_data, 'Time': time_data})
