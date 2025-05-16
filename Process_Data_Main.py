#   Import the functions we wrote in Calculation_Functions.py
import Calculation_Functions as cf

#   Step 1: Read event data from the bookings CSV file
event_data = cf.read_csv("Event_Bookings.csv")  # Loads all event rows

#   Step 2: Calculate attendance rate (%) for each event
event_data = cf.calculate_attendance_rates(event_data)  # Adds 'AttendanceRate' to each row

#   Step 3: Find most and least popular events
most_popular = cf.get_most_popular_event(event_data)     # Event with highest attendance
least_popular = cf.get_least_popular_event(event_data)   # Event with lowest attendance

#   Step 4: Print summary info to screen (optional)
print("Most Popular Event:", most_popular['EventName'], "-", most_popular['AttendanceRate'], "% attendance")
print("Least Popular Event:", least_popular['EventName'], "-", least_popular['AttendanceRate'], "% attendance")

#   Step 5: Write full event summary report to a text file
cf.write_summary_report(event_data, "Event_Summary_Report.txt")  # Output report saved in the same folder
print("\n✅ Report saved as 'Event_Summary_Report.txt'")
