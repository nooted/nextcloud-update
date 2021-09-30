import time
import watchdog.events
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import re
import watchdog.observers
import time
import fnmatch
import os
import logging
import datetime
import yagmail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
class Handler(watchdog.events.PatternMatchingEventHandler):

    def __init__(self):

           watchdog.events.PatternMatchingEventHandler.__init__(self,
                ignore_patterns=['.*\\.(db-wal|db-shm|swp|tmp)' , '.*appdata_ocefm1chq2v3/.*'],
                ignore_directories=False, case_sensitive=False)

    def getMailDict(self, filename):
        inFile = open(filename, "r")
        allData = inFile.readlines()
        inFile.close()
        mailDict = {}
        for line in allData:
            emails = []
            line = line.replace("\n", "")
            line = line.split(" ")
            if len(line)>1:
                name = line[0]
                for email in line[1:]:
                    emails.append(email)
                mailDict[name] = emails

        return mailDict


    def on_created(self, event):

        execluded = ['appdata_ocefm1chq2v3', 'Serve', 'files_encryption' , 'files_trashbin']
        for item in execluded:
            if item in event.src_path:
                 return
        current_date_time = str(datetime.datetime.now())
        new_file = event.src_path
        split_new_file = new_file.split("data/",1)[1]
        with open('/root/names.txt') as f:
             file_text = f.readlines()
        name_dict = self.getMailDict('/root/names.txt')
#        print(file_text)
#        for line in file_text:
#             emails = []
#             line = line.replace("\n", "")
#             line = line.split(" ")
#             if len(line)>1:
#                 name = line[0]
#                 for email in line[1:]:
#                    emails.append(email)
#                 name_dict[name] = emails
        s1 = str(split_new_file)
        print(s1)
        s1_split = (s1.split('/'))
        search_string = (s1_split[0])
        print(name_dict)
        print(search_string)
        if search_string not in name_dict:
           print("No email account")
           return
        print("Name:", search_string, "Mail:", name_dict[search_string])
        emails = name_dict[search_string]
        #else:
         #   email = ""
          #  print("No email account")
        #if search_string in file_text:
        #  email = file_text.split(search_string)[1].split("\n")[0].strip()
        #  print(email)
      #  for email in emails:
         #   print("->" + " " + "New File Create with name : " + " " + split_new_file)
          #  content = "New File Create with Name" + " " +  split_new_file + " " + "at" + " " + current_date_time
          #  user = 'salman143107@gmail.com'
          #  app_password = 'pmnkacuntynxdudm'
         #   receiver_address = email
        #    subject = 'New File Creation'
       #     mail_content = '''New File Create''' + " " + split_new_file + " " + "at" + " " + current_date_time
      #      message = MIMEMultipart()
     #       message['From'] = user
    #        message['To'] = receiver_address
   #         message['Subject'] = 'New File Create'   #The subject line
  #          message.attach(MIMEText(mail_content, 'plain'))
 #           session = smtplib.SMTP('smtp.gmail.com', 587)
#            session.starttls()
#            session.login(user, app_password)
#            text = message.as_string()
#            session.sendmail(user, receiver_address, text)
#            session.quit()
#            print('Mail Sent')
#            with yagmail.SMTP(user, app_password) as yag:
#                yag.send(receiver_address, subject, content)
#                print("[INFO] Email Sent to :" + " " + receiver_address)


if __name__ == '__main__':

    app_start_time = datetime.datetime.now()
    logger=logging.getLogger()
    logging.basicConfig(level=logging.INFO)
    src_path = r"/var/www/html/nextcloud/data"
    logger.info(
        '\n'
        '-----------------------------------------------------------\n'
        '    Running {0}\n'
        '    PID: {1}\n'
        '    Started on: {2}\n'
        '-----------------------------------------------------------\n'
        .format(__file__, os.getpid(), app_start_time.isoformat())
    )

    print ("**** Detecing new files in :" + src_path + " " + "****")

    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        uptime = datetime.datetime.now()-app_start_time
        logger.info(
            '\n'
            '-----------------------------------------------------------\n'
            '    Stopped {0}\n'
            '    Uptime: {1}\n'
            '-----------------------------------------------------------\n'
            .format(__file__, str(uptime))
        )
