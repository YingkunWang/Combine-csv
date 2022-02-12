# Combine-csv
- I use `python3` to combine multiple tables into a large table
- I assume all files are from "./fixtures/" path
- The main idea is to read all files, and append them into a list
- Then add a column to indicate each row's origional file name
- At last, use *pd.concat* to combine all tables and export it.

The command in the terminal is 
`python3 csv-combiner.py >> combined.csv`
