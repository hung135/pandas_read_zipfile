import zipfile
import os
import datetime as t
import pandas
import io

dir_path="/Users/hnguyen/Desktop/pum2013"

x=os.listdir(dir_path)
print(type(x))
for i in x:
    pass
    #print(i)

zip=zipfile.ZipFile('/Users/hnguyen/Desktop/csv_pus.zip','a')
for item in zip.infolist():
    assert isinstance(item,zipfile.ZipInfo)
    #print(item.filename,item.file_size)
zip.close()
with open('/Users/hnguyen/Desktop/csv_pus.zip') as archive:
#zip.write('/Users/hnguyen/Desktop/pum2013/csv_hvt.zip','test')
    print("xxx1")
    x=zipfile.ZipFile(archive)
    print("xxx2")
    #with io.BufferedReader(x.open('test','r')) as xfile:
    with x.open('ss13pusa.csv','r') as xfile:
        print(t.datetime.now())
        #x=io.BytesIO(xfile.readline())

        df = pandas.read_csv(xfile,chunksize=5)
        print(type(df))

        print(t.datetime.now())
        #print(x)
        print(type(x))

        assert isinstance(df,pandas.io.parsers.TextFileReader)
        print(type(df))
        print(df,"xxxx")
        for a in df:
            print(type(a))
            print(a)
            break


        print(t.datetime.now())