import ftplib
import os
from os import path
from datetime import datetime,date,timedelta
from zipfile import ZipFile

def fstop():
     os.system('pause')



time = datetime.now()
print(time)
today = date.today()
start = datetime.now()
#today = today - timedelta(days = 1)
# mm/dd/y
d3 = today.strftime("%m-%d-%Y")
print("d3 =", d3)
print(type(d3))

working_path = f'C:/Users/Defender/Documents/DKs_sir/DS/EPGdown/{d3}'

FTP_HOST = "epg.dishhome.com.np"
FTP_USER = "epg"
FTP_PASS = "dmn@epg11"
# FTP_HOST = "192.168.1.1"
# FTP_USER = "admin"
# FTP_PASS = "586290929699"


def epg_extract(d_file):
    name= d_file[0].split(".")[0]
    newpath = d_file[1].split(".")[0]
    os.chdir(working_path)
    print("newpath",working_path)
    #creating folder respective zip name
    dir_check_folder(f'{working_path}/{name}')
    print('checkin;',os.path.isfile(d_file[0]))
    

    # Create a ZipFile Object and load sample.zip in it
    with ZipFile(d_file[0], 'r') as zObject:
    # Extracting specific file in the zip
    # into a specific location.
        zObject.extractall(newpath)
    zObject.close()

def dir_check_folder(checkpath):
     
     print(path.isdir(checkpath))
     if not os.path.exists(checkpath):
          os.makedirs(checkpath)
          print(f"The new directory {checkpath}is created!")
    



def ftp_downloading():   
    #Defining Path follow
    pathed =f'/files/{d3}/Regular'
    print(pathed)

    # force UTF-8 encoding
    ftp.encoding = "utf-8"
    # print the welcome message
    print(ftp.getwelcome())
    # change the current working directory to 'pub' folder and 'maps' subfolder
    ftp.cwd(pathed)

    # LIST a directory
    print("*"*50, "LIST", "*"*50)
    ftp.dir()



    # initialize the latest file info
    latestFileTime = None
    latestFilename = None

    for fName in ftp.nlst():
    # print(fName)
    # mdtm may not be supported for folder is IIS based FTP server, so wrapping with try except
        try:
            fTimeInfo = ftp.voidcmd(f"MDTM {fName}")
            fTime = fTimeInfo.split(" ")[1]
            if latestFileTime!=None:
                if fTime >= latestFileTime:
                    latestFileTime = fTime
                    latestFilename = fName
            else:
                latestFileTime = fTime
                latestFilename = fName
        except:
            print(f"error while processing {fName}")

    # print(latestFile)

    print(f"The latest file name is - {latestFilename}")

    # # Enter File Name with Extension

    # #latestFilename =

    # # the name of file you want to download from the FTP server
    filename = latestFilename
    # with open(filename, "wb") as file:
    #     # use FTP's RETR command to download the file
    #     ftp.retrbinary(f"RETR {filename}", file.write)
    # Update New dir
    downloaded_dir = f'{working_path}/{filename}' 
    # Print out the files
    print("Downloading..." + filename)
    print("os.path",working_path)
    ftp.retrbinary("RETR " + filename ,open(downloaded_dir, 'wb').write)
    


    # quit and close the connection
    ftp.quit()

    end = datetime.now()
    diff = end - start
    print('All files downloaded for ' + str(diff.seconds) + 's')
    return filename,downloaded_dir
    

#initialize FTP session
# try:
dir_check_folder(working_path)
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
d_file= ftp_downloading()

epg_extract(d_file)
    # try :
    #     epg_extract(ter)
    # except:
    #      print("Extration Error")
# except ftplib.all_errors:
#         print('Unbale to connect FTP Server. Please Contact Bajra')
#         print(ftplib.all_errors)
#         fstop()
