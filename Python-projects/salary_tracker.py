# --- Work Hours & Salary Tracker ---
# This project demonstrates how to use functions, loops, and file handling.
# It records daily work hours and saves the summary into a text file.
#
# 📊 Execution Screenshot: 
https://github.com/alisip-3/Cyber-Learning-Journey./blob/main/Python-projects/SCREENSHOT%202026-04-08%20081619.png#
# It records daily work hours and saves the summary into a text file.
def calculate_salary(hourly_rate):
    # Initialize totals
    total_days = 0
    total_hours = 0
    total_salary = 0

    # Open a text file to save the data ('w' means write mode)
    file = open("my_salary_report.txt", "w")
    file.write("--- WORK REPORT ---\n\n")

    print(f"System started. Your hourly rate is: {hourly_rate}")

    # Start the loop
    date = input("Enter date (or type 'stop' to finish): ")

    while date != "stop":
        hours = float(input(f"How many hours did you work on {date}? "))

        if hours > 0:
            # Calculate daily pay
            daily_pay = hours * hourly_rate

            # Update the totals
            total_days = total_days + 1
            total_hours = total_hours + hours
            total_salary = total_salary + daily_pay

            # Write daily info to the file
            file.write(f"Date: {date} | Hours: {hours} | Pay: {daily_pay}\n")
            print(f"Saved: {daily_pay} shekels for {date}")

        # Ask for the next date to continue the loop
        date = input("\nEnter next date (or 'stop' to finish): ")

    # After the loop stops, write the final summary
    file.write("\n" + "=" * 20 + "\n")
    file.write(f"Total Days: {total_days}\n")
    file.write(f"Total Hours: {total_hours}\n")
    file.write(f"Total Salary: {total_salary}\n")
    file.write("=" * 20 + "\n")

    # Important: Close the file
    file.close()
    print("\nAll data saved to 'my_salary_report.txt'.")


# Running the function with your rate (56)
calculate_salary(56)
