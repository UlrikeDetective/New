import PIL.Image
import PIL.ExifTags

def get_exif_data_method1(image_path):
    img = PIL.Image.open(image_path)
    exif_data = {
        PIL.ExifTags.TAGS[i]: j
        for i, j in img._getexif().items()
        if i in PIL.ExifTags.TAGS
    }
    return exif_data

if __name__ == "__main__":
    image_path = "/Users/ulrike_imac_air/Library/Mobile Documents/com~apple~CloudDocs/Bilder/2023_Lightroom_Drucken/company/2023_Drucken-216.jpg" 
    
    exif_data = get_exif_data_method1(image_path)
    print(exif_data)