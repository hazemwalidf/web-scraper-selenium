from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://catalog.aucegypt.edu/content.php?catoid=36&navoid=1738")

f = open('data.txt', 'w')

expand = driver.find_elements_by_tag_name("driver, .width a")
for x in expand:
    time.sleep(0.3)
    x.click()

try:
    data = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "coursepadding"))
    )
    for k in data:
        f.writelines(k.text)
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("NEWLINE\n")

except:
    print("Error")

for page in range(2, 26):
    driver.get("http://catalog.aucegypt.edu/content.php?catoid=36&catoid=36&navoid=1738&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D="+str(page)+"#acalog_template_course_filter")

    expand = driver.find_elements_by_tag_name("driver, .width a")
    for y in expand:
        time.sleep(0.3)
        y.click()

    try:
        data = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "coursepadding"))
        )
        for z in data:
            f.writelines(z.text)
            f.write("\n")
            f.write("\n")
            f.write("\n")
            f.write("NEWLINE\n")

    except:
        continue

    mylines = []
    with open('data.txt', 'r') as myfile:
        for line in myfile:
            mylines.append(line)

        length = len(mylines)
        mylines = [sub.removesuffix('\n') for sub in mylines]

        for x in range(length):
            if mylines[x] == 'NEWLINE':
                mylines = [x.replace('NEWLINE', '\n') for x in mylines]
            mylines = [x.removesuffix('Description') for x in mylines]
            mylines = [x.removesuffix('Prerequisites') for x in mylines]
            mylines = [x.removesuffix('Notes') for x in mylines]
            mylines = [x.removesuffix('When Offered') for x in mylines]
            mylines = [x.removesuffix('Add to Portfolio (opens a new window) [Print Course (opens a new window)]') for x
                       in mylines]

        while "" in mylines:
            mylines.remove("")
        print(mylines)

        with open('new.csv', 'w') as newfile:
            new_writer = csv.writer(newfile)

            with open('new.csv', 'r') as readerfile:
                new_reader = csv.reader(readerfile)
                for row in mylines:
                    if 'Prerequisites' not in mylines:
                        mylines.insert(3, 'Prerequisites')

            new_writer.writerow(mylines)