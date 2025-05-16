import csv  # To handle reading CSV files

#  Function to read a CSV file and return the data as a list of dictionaries
def read_csv(filename):
    data = []  # Empty list to store each row of the CSV
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Reads the CSV and maps headers to values
            for row in reader:
                data.append(row)  # Add each row (as a dictionary) to the list
    except FileNotFoundError:
        print("File not found:", filename)  # Show error if file is missing
    return data  # Return the list of rows

#  Function to calculate attendance rate for each event
def calculate_attendance_rates(event_data):
    for event in event_data:
        try:
            # Convert string numbers to integers
            total = int(event['TotalTickets'])  # Total tickets booked
            attended = int(event['Attended'])   # How many people actually showed up

            # Calculate attendance rate as a percentage
            rate = (attended / total) * 100
            event['AttendanceRate'] = round(rate, 2)  # Add new value to the event
        except:
            event['AttendanceRate'] = 0  # In case of error (e.g., missing data), set to 0
    return event_data  # Return the updated data list

#  Function to find the event with the highest attendance rate
def get_most_popular_event(event_data):
    highest = event_data[0]  # Start by assuming the first event is the highest
    for event in event_data:
        if event['AttendanceRate'] > highest['AttendanceRate']:
            highest = event  # Replace if a higher rate is found
    return highest  # Return the best-attended event

#  Function to find the event with the lowest attendance rate
def get_least_popular_event(event_data):
    lowest = event_data[0]  # Start by assuming the first event is the lowest
    for event in event_data:
        if event['AttendanceRate'] < lowest['AttendanceRate']:
            lowest = event  # Replace if a lower rate is found
    return lowest  # Return the least-attended event

#  Function to write a summary report to a text file
def write_summary_report(event_data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("📊 Event Summary Report\n\n")
            for event in event_data:
                file.write("Event Name: " + event['EventName'] + "\n")
                file.write("Venue: " + event['Venue'] + "\n")
                file.write("Total Bookings: " + event['TotalTickets'] + "\n")
                file.write("Total Attendance: " + event['Attended'] + "\n")
                file.write("Attendance Rate: " + str(event['AttendanceRate']) + "%\n")
                file.write("Date: " + event['Date'] + "\n")
                file.write("------------------------\n")
    except:
        print("Something went wrong while writing the report.")
