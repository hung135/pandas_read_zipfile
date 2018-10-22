import zipfile
import os
import datetime as t
import pandas
import io
import re

dir_path="/Volumes/500gb/2011_ACSSF_By_State_By_Sequence_Table_Subset/"
re_data_file= re.compile(r'^.*\.csv$')
x=os.listdir(dir_path)
column_counts=set()
print(type(x))
for i in x:

    print(i)
    dir=os.path.join(dir_path,i)
    if os.path.isdir(dir):
        sub=os.listdir(dir)
        for ii in sub:
            print(ii)
            zip=zipfile.ZipFile('/Users/hnguyen/Desktop/csv_pus.zip','a')
            for item in zip.infolist():
                assert isinstance(item,zipfile.ZipInfo)
                if re_data_file.search(item.filename):
                    print(item.filename)
                    with zip.open(item.filename,'r') as data_file:
                        df = pandas.read_csv(data_file,chunksize=1)
                        assert isinstance(df,pandas.io.parsers.TextFileReader)
                        for chunk in df:
                            assert isinstance(chunk,pandas.core.frame.DataFrame)
                            #print("\t"+str(len(chunk.columns.values)))
                            x.append(len(chunk.columns.values))
                            break
            zip.close()
print(column_counts)

"""
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
"""