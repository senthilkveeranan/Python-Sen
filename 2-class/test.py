import getpass                                                                                             
import smtplib                                                                        
HOST = ('smtp.gmail.com')                                                                                     
PORT = 465
username = ('senthil.veeranan@gmail.com')                                                                            
password = getpass.getpass('Provide Gmail password: ')
input('Provide Gmail password:')
server = smtplib.SMTP_SSL(HOST, PORT)