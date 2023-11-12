employee_ids = [int(input()) for _ in range(5)]
if (employee_ids[0] + employee_ids[1]) % 2 == 0 and \
   (employee_ids[1] + employee_ids[2]) % 2 == 0 and \
   (employee_ids[2] + employee_ids[3]) % 2 == 0 and \
   (employee_ids[3] + employee_ids[4]) % 2 == 0 and \
   (employee_ids[4] + employee_ids[0]) % 2 == 0:
       print("\nYes the Meeting will be Conducted")
else:
    print("\nNo the Meeting will not be Conducted")
