import csv

# Open the CSV file
with open('/Users/ulrike_imac_air/Documents/Programmieren/Python/Vs_code/meta_sitzen.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate through each row
    for row in reader:
        # Split the 'multiple_data' column by commas
        data_points = row['multiple_data'].split(',')
        
        # Assign new columns for each data point (assuming there are 3 data points)
        row['data_point_1'] = data_points[0]
        row['data_point_2'] = data_points[1]
        row['data_point_3'] = data_points[2]
        row['data_point_4'] = data_points[3]
        row['data_point_5'] = data_points[4]
        row['data_point_6'] = data_points[5]
        row['data_point_7'] = data_points[6]
        row['data_point_8'] = data_points[7]
        row['data_point_9'] = data_points[8]
        
        # Do something with the new columns or write them to a new CSV file
        print(row)  # For example, printing the updated row
