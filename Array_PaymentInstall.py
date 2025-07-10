import datetime

class PaymentInstallment:
  def __init__(self, due_date, amount, status='Scheduled'):
    self.due_date = due_date
    self.amount = amount
    self.status = status

  def __str__(self):
    return f"Due: {self.due_date.strftime('%Y-%m-%d')} | Amount: ${self.amount:,.2f} |  Status: {self.status}"

class Array:
  def __init__(self):
    # initialized to an empty list 
    self.data = []

  def append(self, value):
    # adds a value to the end of the list
    self.data.append(value)

  def get(self, index):
    # access via index and retrieves the value 
    if 0 <= index < len(self.data):
        return self.data[index]
    else:
        raise IndexError("index out of bounds")

  def update(self, index, value):
    # updates the value at given index with a new one 
    if 0 <= index < len(self.data):
        self.data[index] = value 
    else:
        raise IndexError("index out of bounds")

  def remove_at(self, index):
    # deletes a value at the given index
    if 0 <= index < len(self.data):
        return self.data.pop(index)
    else:
        raise IndexError("index out of bounds")

  def __len__(self):
    # return the number of items in the array 
    return len(self.data)

  def __str__(self):
    return "[\n  " + ",\n  ".join(str(item) for item in self.data) + "\n]"

# --- Financial Problem Demonstration | Payment Installation ---
if __name__ == "__main__":
    print(" ----- Management of a Customer's Loan Repayment Schedule -----")

    # new loan payment schedule
    schedule = Array()
    print("\nInitial Loan Schedule:", schedule)
    print(f"Total installments: {len(schedule)}")

    # adding installments, 4 months
    schedule.append(PaymentInstallment(datetime.date(2025, 8, 1), 250.00))
    schedule.append(PaymentInstallment(datetime.date(2025, 9, 1), 250.00))
    schedule.append(PaymentInstallment(datetime.date(2025, 10, 1), 250.00))
    schedule.append(PaymentInstallment(datetime.date(2025, 11, 1), 250.00))
    print("\nSchedule after initial setup (4 installments):", schedule)
    print(f"Total installments: {len(schedule)}")

    # retrieve details of a particular installment
    try:
        third_installment = schedule.get(2) # index 2 is the 3rd installment
        print(f"\nDetails of the 3rd installment: {third_installment}")
    except IndexError as e:
        print(f"Error: {e}")

    # updating an installment's details (like when 2nd payment amount changes due to rate adjustment)
    print("\n----- SCENARIO: Loan terms change, 2nd installment amount is adjusted -----")
    try:
        original_second_installment = schedule.get(1)
        print(f"Original 2nd installment: {original_second_installment}")

        # need to create a new updated installment object
        updated_second_installment = PaymentInstallment(
            original_second_installment.due_date,
            265.50, # new amount
            original_second_installment.status
        )
        schedule.update(1, updated_second_installment) # update at index 1
        print("Schedule after updating the 2nd installment:", schedule)
    except IndexError as e:
        print(f"Error updating: {e}")

    # remove an installment 
    print("\n----- SCENARIO: Customer makes a partial early payment, covering the 3rd installment -----")
    try:
        removed_installment = schedule.remove_at(2) # remove the 3rd installment (at index 2)
        print(f"Removed installment: {removed_installment}")
        print("Schedule after removing the 3rd installment:", schedule)
        print(f"Total installments now: {len(schedule)}")
    except IndexError as e:
        print(f"Error removing: {e}")

    # error handling, accessing an out-of-bounds index 
    print("\n----- Attempting to access/modify out-of-bounds -----")
    try:
        schedule.get(10)
    except IndexError as e:
        print(f"Caught expected error: {e}")

    try:
        schedule.update(5, PaymentInstallment(datetime.date(2026, 1, 1), 100.00))
    except IndexError as e:
        print(f"Caught expected error: {e}")

    print("\nFinal Loan Schedule:", schedule)