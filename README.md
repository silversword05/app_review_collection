# App review collection
Review collection for apps to perform sentiment analysis on them. Uses Indian market to collect the reviews.

## Installation
Use `pip install` for the installation. Required packages are:
- pandas
- google_play_scraper
- openpyxl
- xlrd
- wheel

## Code Execution
Before executing the code, please verify these two facts:
- [ ] Files `collected_reviews.xlsx` and `error_reviews.txt` are not in the current folder, either deleted or a backup is kept.
- [ ] marked_apps.xlsx is in the same folder.

The code will ask for number of reviews to collect per app. Put it 3000/5000 as per requirement.

## Code Failure
The code is well equiped with try-catch block and should not fail. In case of failure (will fail most likely if the internet connection is interrupted), remove the files `collected_reviews.xlsx` and `error_reviews.txt` (keep a backup if necessary) from the current directory/folder and rerun the code. 

### Not necessary
To reduce time, go to line number 8 of 'collect_reviews_only.py' and remove the sheet names which are already complete. Keep in mind not to remove the sheet name for which the error occured as that sheet is not saved. In that case, keep a backup of `collected_reviews.xlsx` and `error_reviews.txt`. The list of completed sheets can be found in the console with the message `Sheet name completed <sheetname>`.
