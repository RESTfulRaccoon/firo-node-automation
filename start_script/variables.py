from sendnodes import args
import local_fun as local_fun
import distro
from pathlib import Path
from subprocess import run, PIPE

### CLIENT DISTRO SPICIFIC INFORMATION

dist = distro.id()
home = str(Path.home())

if dist == 'ubuntu' or 'debian' or 'macos':
	keypath=home+'/home/$USER/.ssh/'
elif dist == "windows":
	keypath=home+'\\.ssh\\'

### REQUIRED
ext = args.server_ip
supass = args.superuser_pass
walletpass = args.wallet_password

### VERBOSE

if args.verbose==True:
	def verbose(text):
		print(text)
else:
	def verbose(text):
		text

### RPC USERNAME

if args.rpc_user == None:
    a = local_fun.username_gen(10).lower()
else:
	a = args.rpc_user.lower()
local_fun.usr(a)
rpc_usrname = a

### RPC PASSWORD

if args.rpc_pass == None:
	b = local_fun.rpc_passwd_gen(60)
else:
	b = args.rpc_pass
local_fun.rpc_pass(b)
rpc_passwd = b

### SSH PORT
if args.port != None and args.keep_port == True:
	c = args.port
elif args.keep_port == True:
	c = 22
elif args.port == None:
	c = local_fun.port_gen()
else:
	c = args.port
local_fun.port(c)
port = c

### UNPRIVLAGED USERNAME

if args.usr == 'firo':
	d = 'firo'
else:
	d = args.usr.lower()
local_fun.usr(d)
usr = d

### UNPRIVLAGED USERPASSWORD
if args.passwd == None:
	e = local_fun.usr_passwd_gen(15)
else:
	e = args.passwd
passwd = e

### SUPER USER NAME
suusr = args.superuser

### (OPTIONAL) SSH KEY PASSWORD
sshkeypass = args.sshkeypass
### SSH KEY
try:
    sshkey = run(['ssh-keygen','-t','ed25519','-f','/home/'+usr+'/.ssh/ed25519_firo_0','-N',sshkeypass],stdout=PIPE,universal_newlines=True)
    verbose(sshkey.stdout)
except:
    run(['firo-cli','stop'])
    exit()
