import pandas as pd

data = {
    "RollNo": [1, 2,None, 4 ,5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "Name": [
        "Aman", None, "Harsh", "Danish", "Akash", "Anand", "Aditi", "Yug", "Riya", "Shivam",
        "Satyam", "Sundar", "Aditya", "Om", "Manikanta", "Parul", "Palak", "Akanksha", "Anika", "Tina"
    ],
    "Phone": [
        None, "2345678901", "3456789012", "4567890123", "5678901234", "6789012345", "7890123456", "8901234567", "9012345678", "1234509876",
        "2345609876", "3456709876", "4567809876", "5678909876", "6789009876", "7890109876", "8901209876", "9012309876", "1234609876", "2345709876"
    ],
    "Class": [
        "10A", "11B", "9A", "5C", "12B", None, "3C", "12B", "2A", "10C",
        "1B", "8A", "7C", "6B", "7A", "8C", "9B", "10A", "11C", "11B"
    ]
}


df = pd.DataFrame(data)

print("First 5 records:")
print(df.head())


print("\nLast 5 records:")
print(df.tail())


print("\nChecking for null values:")
print(df.isnull().sum())