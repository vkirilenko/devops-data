## _Задача 1_

- Вопрос 1:  
  "Открыть инструкцию по пользованию приложением awk. Найти секцию про использование переменных окружения. Сохранить эту секцию в отдельный файл.."   
    
   __Result:__  
   
vladimir@localhost:~$ man awk | sed -En '/ENVIRONMENT/{:n; N; /effect/ {p; q}; bn}' | tee awkENV.txt
ENVIRONMENT VARIABLES
   The AWKPATH environment variable can be used to provide a  list  of  directories  that  gawk
   searches when looking for files named via the -f and --file options.

   For  socket communication, two special environment variables can be used to control the num‐
   ber of retries (GAWK_SOCK_RETRIES), and the interval between retries (GAWK_MSEC_SLEEP).  The
   interval  is in milliseconds. On systems that do not support usleep(3), the value is rounded
   up to an integral number of seconds.

   If POSIXLY_CORRECT exists in the environment, then gawk behaves exactly as  if  --posix  had
   been  specified  on  the  command line.  If --lint has been specified, gawk issues a warning
   message to this effect.
vladimir@localhost:~$ ll
total 248
drwx------.  6 vladimir vladimir    279 Dec  8 09:49 ./
drwxr-xr-x. 15 root     root        184 Dec  8 07:39 ../
-rw-rw-r--.  1 vladimir vladimir     24 Dec  3 09:49 abs_path.txt
-rw-rw-r--.  1 vladimir vladimir    777 Dec  8 09:49 awkENV.txt
-rw-------.  1 vladimir vladimir 102927 Dec  8 09:31 .bash_history
-rw-r--r--.  1 vladimir vladimir   3368 Nov 29 14:35 .bashrc
drwx------.  3 vladimir vladimir     18 Dec  7 13:39 .config/
drwxrwxr-x.  3 vladimir vladimir     18 Dec  6 14:22 Download/
-rwxrwxr-x.  1 vladimir vladimir    645 Dec  3 11:14 ls_abs.sh*
-rw-rw-r--.  1 vladimir vladimir    139 Nov 29 14:38 .profile
-rwxrwxr-x.  1 vladimir vladimir    320 Dec  3 09:26 script_up.sh*
drwxrwxr-x.  2 vladimir vladimir      6 Dec  3 11:39 Share/
-rw-------.  1 vladimir vladimir 102400 Nov 29 20:51 .swp
drwxrwxr-x.  2 vladimir vladimir      6 Dec  3 09:46 Temp/
-rw-rw-r--.  1 vladimir vladimir    967 Dec  7 13:47 .toprc  

  
  
  
## _Задача 2_

- Вопрос 1:  
  "Написать скрипт, который создаёт файл "task2.txt" директорией выше своего местоположения. В случае ошибки текст ошибки записывается в err.log а пользователю выдаётся сообщение "Error.""     
    
- Вопрос 2:  
  "Если файл уже существует, выдаётся одна ошибка, а если нет прав для его создания - другая."  

   __Result:__  
   
vladimir@localhost:~$ ./script_up.sh
Your rights are insufficient
vladimir@localhost:~$ cat err.log
touch: cannot touch ‘../task2.txt’: Permission denied
vladimir@localhost:~$ cd Temp
vladimir@localhost:~/Temp$ ../script_up.sh
vladimir@localhost:~/Temp$ ../script_up.sh
The file already exists
vladimir@localhost:~/Temp$ cat ../script_up.sh

\#!/bin/bash

\#Create task2.txt to upper directory
\#Save log to err.log if raise the error & show error msg "Error."

[[ ! -e ../task2.txt ]] && ( touch ../task2.txt 2>./err.log \\
                        || echo "Your rights are insufficient" ) \\
                        || echo "The file already exists" |&tee ./err.log

  
  
## _Задача 3_

- Вопрос 1:  
  "Создать 2 файла: 1-й - текстовый с указанием абслютного пути до директории. 2-й - скрипт, который при выполнении выводит содержимое директории по указанному в первом файле."  
   
- Вопрос 2:  
  "Скрипт выводит отдельно количество файлов и количество директорий."  
    
- Вопрос 3:  
  "Скрипт принимает любое количество записей в первом файле и обрабатывает их последовательно."  

   __Result:__  
   
vladimir@localhost:~$ ./ls_abs.sh

==== List of  /home/vladimir
abs_path.txt  Download  errors.txt  script_up.sh  task2.txt
awkENV.txt    err.log   ls_abs.sh   Share         Temp


Files count: 7
Directories count: 3


==== List of  /var/log
anaconda           btmp           firewalld           messages-20211203  tuned                wtmp
audit              btmp-20211203  grubby              rhsm               vboxadd-install.log  yum.log
boot.log           chrony         grubby_prune_debug  secure             vboxadd-setup.log
boot.log-20211129  cron           lastlog             secure-20211203    vboxadd-setup.log.1
boot.log-20211203  cron-20211203  maillog             spooler            vboxadd-setup.log.2
boot.log-20211206  dmesg          maillog-20211203    spooler-20211203   vboxadd-setup.log.3
boot.log-20211208  dmesg.old      messages            tallylog           vboxadd-setup.log.4


Files count: 32
Directories count: 5

vladimir@localhost:~$ cat abs_path.txt
/home/vladimir
/var/log
vladimir@localhost:~$ cat ls_abs.sh
\#!/bin/bash

\# Get the path records from file 'abs_path.txt' in the same directory
\# and show all files and directories on these paths

[[ -e ./abs_path.txt  ]] || (echo "The script requires abs_path.txt in the same directory" |&tee errors.txt && exit 2)

IFS=$'\n'

fl=0
dr=0

for i in $(cat ./abs_path.txt)

 do
   echo " "
   echo "==== List of  $i"
   ls $i --color=auto
   echo " "

   for entry in $i/*
     do
       if   [ -f "$entry" ]
         then ((fl++))
       elif [ -d "$entry" ]
         then ((dr++))
       fi
     done

   echo "Files count: $fl "
   echo "Directories count: $dr "
   echo " "

 fl=0
 dr=0

 done
	
  