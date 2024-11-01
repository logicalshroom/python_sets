# Task 1: Duplicate Entries Clean Up

# This should be super easy, we can convert the list to a set using the set command and print it
# The dupes should get kicked automatically

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def dupeclean(cust_ids):
    customer_set = sorted(set(cust_ids)) #lets also sort them so that they appear in order
    print(f"Here's your Customer IDs, with Duplicates removed:\n{customer_set}")

dupeclean(customer_ids)