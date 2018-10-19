
import zipfile
import os
import datetime as dt
import pandas
import io
import psutil

print("memory", psutil.virtual_memory())

with open('/Users/hnguyen/Desktop/pum2013/unix_pus.zip') as archive:
    # zip.write('/Users/hnguyen/Desktop/pum2013/csv_hvt.zip','test')
    print("xxx1")
    x = zipfile.ZipFile(archive)

    print("xxx2")
    t={}
    t["filename"]=""
    t["size"]=0
    for y in x.infolist():
        assert isinstance(y,zipfile.ZipInfo)
        print(y.filename,y.file_size)
        if y.file_size>t["size"]:
            t["filename"]=y.filename
            t["size"]=y.file_size
    print(t)
    with io.BufferedReader(x.open(t["filename"],'r')) as xfile:
    #with x.read(t["filename"], 'r') as xfile:
        #print(t.datetime.now())
        #print(type(xfile))

        #print(type(x),len(x),len(y))
        #print(io.StringIO(x))
        #x=xfile.read()
        #zz=io.BytesIO(x.read(t["filename"]))
        #zz=io.BytesIO(xfile.read())
        print('reading')
        zz=xfile.read()
        print("memory",psutil.virtual_memory())
        print("file_type",type(zz))
        df = pandas.read_sas(io.BytesIO("".join(zz)), format='sas7bdat', encoding='iso-8859-1', chunksize=1, iterator=True)
        print(df)
    print(dt.datetime.now())


    print("memory",psutil.virtual_memory())