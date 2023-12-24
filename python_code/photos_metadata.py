import exifread

def get_exif_data_method2(image_path):
    with open(image_path, 'rb') as file:
        tags = exifread.process_file(file)
    return tags

if __name__ == "__main__":
    image_path = "/Users/ulrike_imac_air/Library/Mobile Documents/com~apple~CloudDocs/Bilder/2023_Lightroom_Drucken/company/2023_Drucken-216.jpg"  # Replace this with the actual path of your image
    exif_data = get_exif_data_method2(image_path)
    print(exif_data)