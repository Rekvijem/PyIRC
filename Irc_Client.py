from Tkinter import *
from tkMessageBox import *
from ttk import *
import sys, os, socket, string, thread, datetime
class pyIRC:
    def __init__(self):
        pass
    def connect(self):
        wcm.withdraw()
        self.gui2()
        thread.start_new_thread(self.listen, (1024,))
    def checker(self):
        if nick.get() == "Nickname" or ident.get() == "Identity" or realname.get() == "Realname":
            showwarning("Error","Please fill out all of the credentials boxes.")
        else:
            self.connect()
    def gui(self):
        wcm.update()
        wcm.deiconify()
    def gui2(self):
        root.update()
        root.deiconify()
    def listen(self,pckts): #PACKETS Def: 1024 
        global s
        host2 = host.get()
        port2 = int(port.get())
        nick2 = nick.get()
        ident2 = ident.get()
        realname2 = realname.get()
        try:
            s=socket.socket()
            s.connect((host2,port2))
        except:
            showwarning("Error","Unable to connect to server.")
        try:
            s.send("NICK {0}\r\n".format(nick2))
            s.send("USER {0} {1} bla :{2}\r\n".format(ident2,host2,realname2))
        except:
            showwarning("Error","User credentials are incorrect")
        
        #LISTENING#
        readbuffer = ""
        while 1:
            readbuffer=readbuffer+s.recv(pckts)
            #tb.insert(END,readbuffer)
            readbuffer += "\r"
            splitmsg = readbuffer.split()
def msgHandle(self,msg,rdbf):
    splitmsg = msg.split()
    print splitmsg
    if msg.replace(' ','') == "":
        pass
    else:
        if splitmsg[0].find(":") != -1:
            splitmsg[0] = splitmsg[0].replace(":","")
        '''
        if msg.find("NOTICE AUTH :") != -1:
            msg = msg.replace("NOTICE AUTH :","")
        if msg.find("PRIVMSG {0}:".format(nickname)):
        '''
        if splitmsg[0].find("NOTICE") != -1 and splitmsg[1].find("AUTH") != -1:
            splitmsg[0] = ""
            splitmsg[1] = ""
            if splitmsg[2] == ":":
                splitmsg[2] = ""
        if splitmsg[0].find
            if splitmsg[3].find('VERSION') != -1 or splitmsg[3].find('\\001VERSION\\001') != -1 or splitmsg[3].find('\001VERSION\001') != -1:
                print "Version requested by: {0}".format(splitmsg[0].split('!')[0])
                print "PRIVMSG {0} :\001VERSION PyIRC/PyRC:Beta 1.0:Multiplatform Windows and Linux\001".format(splitmsg[0].split('!')[0])
            elif splitmsg[3].find('SOURCE') != -1 or splitmsg[3].find('\\001SOURCE\\001') != -1 or splitmsg[3].find('\001SOURCE\001') != -1:
                print "Source requested by: {0}".format(splitmsg[0].split('!')[0])
                print "PRIVMSG {0} :\001SOURCE None:None:None\001".format(splitmsg[0].split('!')[0])
            elif splitmsg[3].find('TIME') != -1 or splitmsg[3].find('\\001TIME\\001') != -1 or splitmsg[3].find('\001TIME\001') != -1:
                timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                print "Time requested by: %s" % (splitmsg[0].split('!')[0])
                print "PRIVMSG {0} :\001TIME (Format: YYYY/MM/DD HH/MM/SS) {1}\001".format(splitmsg[0].split('!')[0],timenow)
            else:
                print "Private Message From {0}: {1}".format((splitmsg[0].split('!')[0]), msg.split(':'))               
        newmsg = ''.join(splitmsg)
        tb.insert()


##########REFERENCES##########
#:hilts!hilts@mesothelioma.sucks PRIVMSG Rekvijem :VERSION
#[':this!this@this.com', 'PRIVMSG', 'Rekvijem:', 'VERSION']
#NOTICE nick : VERSION PyIRC by Anthrax Beta V1.0



#Old, Bad, and Not Working Message Handling
'''
    def msgHandle(self,line):
        checkfor = ['PRIVMSG','NOTICE','JOIN','PART','NICK','QUIT','PING','TIME','353','433','001','002','003','004','005','250','251','252','253','254','255','265','266','366','375','376','439']
        asd = False
        found = ""
        for i in checkfor:
            if line.find(i) != -1:
                asd = True
                found = i
        if asd:
            if found == "PING":
                self.handleCTCP("PING",line)
            if found == "VERSION":
                self.handleCTCP("VERSION",line)
            if found == "TIME":
                self.handleCTCP("TIME",line)
            
    def handleCTCP(self,arg,line): #VERSION, TIME, PING
        if arg == "PING":
            s.send("PONG %s\r\n" % line[1])
        if arg == "VERSION":
            nick = line[0].split("!")[0]
            nick = nick.replace(':','')
            s.send(":NOTICE %s :\001VERSION PyIRC BETA 1.0 by Anthrax\001" % nick)
        if arg == "TIME":
            nick = line[0].split("!")
            nick = nick.replace(':','')
            now = datetime.now()
            sec = str(now.second())
            minu = str(now.minute())
            hour = str(now.hour())
            day = str(now.day())
            month = str(now.month())
            year = str(now.year())
            s.send(":NOTICE %s :TIME %s %s %s %s:%s:%s" % (nick,day,month,year,hour,minu,sec))
    def handlePM(self,line):
        pass
'''
ircinstance = pyIRC()
###############
#####GUI 1#####
###############
wcm = Tk()
wcm.geometry("200x250")
wcm.title("PyIRC")
Label(wcm,text="Connection Info").pack()
host = Entry(wcm)
host.insert(0,"IP")
host.pack()
port = Entry(wcm)
port.insert(0,"Port")
port.pack()
Label(wcm,text="").pack()
Label(wcm,text="User Credentials").pack()
nick = Entry(wcm)
nick.insert(0,"Nickname")
nick.pack()
ident = Entry(wcm)
ident.insert(0,"Identity")
ident.pack()
realname = Entry(wcm)
realname.insert(0,"Realname")
realname.pack()
Button(wcm,text="Connect",command=ircinstance.checker).pack()


###############
#####GUI 2#####
###############
root = Tk()
root.geometry('750x422')
root.title("PyIRC")
tb = Text(root)
tb.place(x=3,y=3)
snd = Entry(root,width=92)
snd.insert(0,"Enter Message")
snd.place(x=3,y=396)
Button(root,text="Send Message").place(x=561,y=395)

###############

root.withdraw()
wcm.withdraw()

###############
if __name__ == "__main__":
    ircinstance.gui()
    mainloop()
