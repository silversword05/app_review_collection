import pandas as pd
from google_play_scraper import Sort, reviews
from openpyxl import load_workbook
from os import path


def collect_reviews(count=10000):
    sheet_names = ["VR+AR+Edu", "VR", "VR+Edu", "Edu", "AR", "AR+Edu", "VR+AR"]

    for sheet_name in sheet_names:
        df = pd.read_excel('marked_apps.xlsx', sheet_name=sheet_name)
        df_new = pd.DataFrame(columns=["app_id", "title", "user_name", "content", "score", "thumbsUpCount", "reviewCreatedVersion", "time"])
        for index, row in df.iterrows():
            try:
                result, continuation_token = reviews(row['app_id'], lang='en', country='in', sort=Sort.NEWEST, count=count)
                print("Working for app", row['title'])
                for review in result:
                    row_new = {"user_name": str(review['userName']), "content": str(review['content']), "score": int(review['score']), "app_id": str(row['app_id']), "title": str(row['title']),
                               "thumbsUpCount": int(review['thumbsUpCount']), "reviewCreatedVersion": str(review['reviewCreatedVersion']), "time": review['at']}
                    df_new = df_new.append(row_new, ignore_index=True)
            except:
                f = open('error_reviews.txt', 'a')
                f.write(row['app_id'] + '\n')
                f.close()
        writer = pd.ExcelWriter('collected_reviews.xlsx', engine='xlsxwriter')
        try:
            book = load_workbook('collected_reviews.xlsx')
            writer.book = book
        except:
            pass
        # try:
        df_new = df_new.applymap(lambda x: x.encode('unicode_escape').decode('utf-8') if isinstance(x, str) else x)
        df_new.to_excel(writer, index=False, sheet_name=sheet_name, engine='xlsxwriter')
        # except:
        #     f.write(sheet_name + '\n\n')
        writer.save()
        writer.close()
        print("Sheet name completed", sheet_name, '\n')


if path.isfile('collected_reviews.xlsx') or path.isfile('error_reviews.txt'):
    print('Please keep a backup or delete the following files before running the code. Remove from the current folder.')
    print('collected_reviews.xlsx and error_reviews.txt')
    exit(0)
cnt = int(input("Enter the number of reviews to collect per app "))
collect_reviews(count=cnt)
