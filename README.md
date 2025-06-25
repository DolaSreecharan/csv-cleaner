# 🧼 CSV Cleaner Tool using Python + pandas

A command-line tool to clean messy CSV files by removing null values and duplicates. Saves a cleaned version while keeping the original file safe.


## ✅ Features

- View original CSV content
- Remove duplicate rows
- Remove null rows
- Apply both cleaning steps together
- Save cleaned file as `cleaned_<original>.csv`

## 💻 Tech Stack

- Python
- pandas
- csv module

## 📂 Files Included

- `cleaner.py` – main script  
- `dirty_students.csv` – sample input  
- `cleaned_dirty_students.csv` – sample output  
- `README.md` – documentation  

## 🚀 How to Run

1. Place a `.csv` file in the project folder (e.g., `dirty_students.csv`)

2. Run the script:
```bash
python cleaner.py

3. Select your cleaning operation:

1. Remove Duplicates  
2. Remove Nulls  
3. Both  
4. View File  
5. Exit

4. The cleaned file will be saved as cleaned_<filename>.csv

##🏆 Author

Built  by Sree Charan
