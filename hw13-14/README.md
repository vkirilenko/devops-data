## _Задача 1_  

-  "Use rpm for the following tasks:"  
  1. Download sysstat package.  
```
vladimir@localhost:~$ wget http://mirror.centos.org/centos/7/os/x86_64/Packages/sysstat-10.1.5-19.el7.x86_64.rpm  
--2021-12-21 00:58:22--  http://mirror.centos.org/centos/7/os/x86_64/Packages/sysstat-10.1.5-19.el7.x86_64.rpm  
Resolving mirror.centos.org (mirror.centos.org)... 185.50.225.30, 2604:1380:2001:d00::3  
Connecting to mirror.centos.org (mirror.centos.org)|185.50.225.30|:80... connected.  
HTTP request sent, awaiting response... 200 OK  
Length: 323020 (315K) [application/x-rpm]  
Saving to: ‘sysstat-10.1.5-19.el7.x86_64.rpm’  
  
  100%[======================================================>] 323,020    518KB/s   in 0.6s  
  
  2021-12-21 00:58:23 (518 KB/s) - ‘sysstat-10.1.5-19.el7.x86_64.rpm’ saved [323020/323020]  
```  

  2. Get information from downloaded sysstat package file.  

```
vladimir@localhost:~$ rpm -qip sysstat-10.1.5-19.el7.x86_64.rpm  
Name        : sysstat  
Version     : 10.1.5  
Release     : 19.el7  
Architecture: x86_64  
Install Date: (not installed)  
Group       : Applications/System  
Size        : 1172488  
License     : GPLv2+  
Signature   : RSA/SHA256, Sat 04 Apr 2020 12:08:48 AM MSK, Key ID 24c6a8a7f4a80eb5  
Source RPM  : sysstat-10.1.5-19.el7.src.rpm  
Build Date  : Wed 01 Apr 2020 07:36:37 AM MSK  
Build Host  : x86-01.bsys.centos.org  
Relocations : (not relocatable)  
Packager    : CentOS BuildSystem <http://bugs.centos.org>  
Vendor      : CentOS  
URL         : http://sebastien.godard.pagesperso-orange.fr/  
Summary     : Collection of performance monitoring tools for Linux  
Description :  
The sysstat package contains sar, sadf, mpstat, iostat, pidstat, nfsiostat-sysstat,  
tapestat, cifsiostat and sa tools for Linux.  
The sar command collects and reports system activity information. This  
information can be saved in a file in a binary format for future inspection. The  
statistics reported by sar concern I/O transfer rates, paging activity,  
process-related activities, interrupts, network activity, memory and swap space  
utilization, CPU utilization, kernel activities and TTY statistics, among  
others. Both UP and SMP machines are fully supported.  
The sadf command may be used to display data collected by sar in various formats  
(CSV, XML, etc.).  
The iostat command reports CPU utilization and I/O statistics for disks.  
The tapestat command reports statistics for tapes connected to the system.  
The mpstat command reports global and per-processor statistics.  
The pidstat command reports statistics for Linux tasks (processes).  
The nfsiostat-sysstat command reports I/O statistics for network file systems.  
The cifsiostat command reports I/O statistics for CIFS file systems.  
```


  3. Install sysstat package and get information about files installed by this package.   
  
```
vladimir@localhost:~$ sudo rpm -ivh sysstat-10.1.5-19.el7.x86_64.rpm  --nodeps  
Preparing...                          ################################# [100%]  
Updating / installing...  
   1:sysstat-10.1.5-19.el7            ################################# [100%]    
  
vladimir@localhost:~$ rpm -ql sysstat  
/etc/cron.d/sysstat  
/etc/sysconfig/sysstat  
/etc/sysconfig/sysstat.ioconf  
/usr/bin/cifsiostat  
/usr/bin/iostat  
/usr/bin/mpstat  
/usr/bin/nfsiostat-sysstat  
/usr/bin/pidstat  
/usr/bin/sadf  
/usr/bin/sar  
/usr/bin/tapestat  
/usr/lib/systemd/system/sysstat.service  
/usr/lib64/sa  
/usr/lib64/sa/sa1  
/usr/lib64/sa/sa2  
/usr/lib64/sa/sadc  
/usr/share/doc/sysstat-10.1.5  
/usr/share/doc/sysstat-10.1.5/CHANGES  
/usr/share/doc/sysstat-10.1.5/COPYING  
/usr/share/doc/sysstat-10.1.5/CREDITS  
/usr/share/doc/sysstat-10.1.5/FAQ  
/usr/share/doc/sysstat-10.1.5/README  
/usr/share/doc/sysstat-10.1.5/sysstat-10.1.5.lsm  
/usr/share/locale/af/LC_MESSAGES/sysstat.mo  
/usr/share/locale/cs/LC_MESSAGES/sysstat.mo  
/usr/share/locale/da/LC_MESSAGES/sysstat.mo  
/usr/share/locale/de/LC_MESSAGES/sysstat.mo  
/usr/share/locale/eo/LC_MESSAGES/sysstat.mo  
/usr/share/locale/es/LC_MESSAGES/sysstat.mo  
/usr/share/locale/eu/LC_MESSAGES/sysstat.mo  
/usr/share/locale/fi/LC_MESSAGES/sysstat.mo  
/usr/share/locale/fr/LC_MESSAGES/sysstat.mo  
/usr/share/locale/hr/LC_MESSAGES/sysstat.mo  
/usr/share/locale/id/LC_MESSAGES/sysstat.mo  
/usr/share/locale/it/LC_MESSAGES/sysstat.mo  
/usr/share/locale/ja/LC_MESSAGES/sysstat.mo  
/usr/share/locale/ky/LC_MESSAGES/sysstat.mo  
/usr/share/locale/lv/LC_MESSAGES/sysstat.mo  
/usr/share/locale/mt/LC_MESSAGES/sysstat.mo  
/usr/share/locale/nb/LC_MESSAGES/sysstat.mo  
/usr/share/locale/nl/LC_MESSAGES/sysstat.mo  
/usr/share/locale/nn/LC_MESSAGES/sysstat.mo  
/usr/share/locale/pl/LC_MESSAGES/sysstat.mo  
/usr/share/locale/pt/LC_MESSAGES/sysstat.mo  
/usr/share/locale/pt_BR/LC_MESSAGES/sysstat.mo  
/usr/share/locale/ro/LC_MESSAGES/sysstat.mo  
/usr/share/locale/ru/LC_MESSAGES/sysstat.mo  
/usr/share/locale/sk/LC_MESSAGES/sysstat.mo  
/usr/share/locale/sr/LC_MESSAGES/sysstat.mo  
/usr/share/locale/sv/LC_MESSAGES/sysstat.mo  
/usr/share/locale/uk/LC_MESSAGES/sysstat.mo  
/usr/share/locale/vi/LC_MESSAGES/sysstat.mo  
/usr/share/locale/zh_CN/LC_MESSAGES/sysstat.mo  
/usr/share/locale/zh_TW/LC_MESSAGES/sysstat.mo  
/usr/share/man/man1/cifsiostat.1.gz  
/usr/share/man/man1/iostat.1.gz  
/usr/share/man/man1/mpstat.1.gz  
/usr/share/man/man1/nfsiostat-sysstat.1.gz  
/usr/share/man/man1/pidstat.1.gz  
/usr/share/man/man1/sadf.1.gz  
/usr/share/man/man1/sar.1.gz  
/usr/share/man/man1/tapestat.1.gz  
/usr/share/man/man5/sysstat.5.gz  
/usr/share/man/man8/sa1.8.gz  
/usr/share/man/man8/sa2.8.gz  
/usr/share/man/man8/sadc.8.gz  
/var/log/sa  
```  
   
-  "Add NGINX repository (need to find repository config on https://www.nginx.com/) and complete the following tasks using yum:"  

  1. Check if NGINX repository enabled or not.  
  
```
vladimir@localhost:~$ ls -la /etc/yum.repos.d  
total 60  
drwxr-xr-x.  2 root root  262 Dec  4 11:14 ./  
drwxr-xr-x. 86 root root 8192 Dec 21 21:31 ../  
-rw-r--r--.  1 root root 1664 Nov 23  2020 CentOS-Base.repo  
-rw-r--r--.  1 root root 1309 Nov 23  2020 CentOS-CR.repo  
-rw-r--r--.  1 root root  649 Nov 23  2020 CentOS-Debuginfo.repo  
-rw-r--r--.  1 root root  314 Nov 23  2020 CentOS-fasttrack.repo  
-rw-r--r--.  1 root root  630 Nov 23  2020 CentOS-Media.repo  
-rw-r--r--.  1 root root 1331 Nov 23  2020 CentOS-Sources.repo  
-rw-r--r--.  1 root root 8515 Nov 23  2020 CentOS-Vault.repo  
-rw-r--r--.  1 root root  616 Nov 23  2020 CentOS-x86_64-kernel.repo  
-rw-r--r--.  1 root root 1358 Sep  4 20:37 epel.repo  
-rw-r--r--.  1 root root 1457 Sep  4 20:37 epel-testing.repo  
-rw-r--r--.  1 root root  573 Dec 21 23:18 nginx.repo  
  
  
\#  This is the default, if you make this bigger yum won't see if the metadata  
\# is newer on the remote and so you'll "gain" the bandwidth of not having to  
\# download the new metadata and "pay" for it by yum not having correct  
\# information.  
\#  It is esp. important, to have correct metadata, for distributions like  
\# Fedora which don't keep old packages around. If you don't like this checking  
\# interupting your command line usage, it's much better to have something  
\# manually check the metadata once an hour (yum-updatesd will do this).  
\# metadata_expire=90m  
  
\# PUT YOUR REPOS HERE OR IN separate files named file.repo  
\# in /etc/yum.repos.d  
```

  2. Install NGINX.  

```
vladimir@localhost:~$ sudo yum install nginx  
Loaded plugins: fastestmirror, product-id, search-disabled-repos, subscription-manager  
  
This system is not registered with an entitlement server. You can use subscription-manager to register.  
  
Loading mirror speeds from cached hostfile  
epel/x86_64/metalink                                                                             |  33 kB  00:00:00  
 * base: mirror.reconn.ru  
 * epel: mirror.cspacehostings.com  
 * extras: mirror.reconn.ru  
 * updates: mirrors.datahouse.ru  
base                                                                                             | 3.6 kB  00:00:00  
epel                                                                                             | 4.7 kB  00:00:00  
extras                                                                                           | 2.9 kB  00:00:00  
updates                                                                                          | 2.9 kB  00:00:00  
(1/2): epel/x86_64/updateinfo                                                                    | 1.0 MB  00:00:01  
(2/2): epel/x86_64/primary_db                                                                    | 7.0 MB  00:00:01  
Resolving Dependencies  
--> Running transaction check  
---> Package nginx.x86_64 1:1.20.1-9.el7 will be installed    
--> Processing Dependency: nginx-filesystem = 1:1.20.1-9.el7 for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Processing Dependency: libcrypto.so.1.1(OPENSSL_1_1_0)(64bit) for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Processing Dependency: libssl.so.1.1(OPENSSL_1_1_0)(64bit) for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Processing Dependency: libssl.so.1.1(OPENSSL_1_1_1)(64bit) for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Processing Dependency: nginx-filesystem for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Processing Dependency: redhat-indexhtml for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Processing Dependency: libcrypto.so.1.1()(64bit) for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Processing Dependency: libprofiler.so.0()(64bit) for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Processing Dependency: libssl.so.1.1()(64bit) for package: 1:nginx-1.20.1-9.el7.x86_64  
--> Running transaction check  
---> Package centos-indexhtml.noarch 0:7-9.el7.centos will be installed  
---> Package gperftools-libs.x86_64 0:2.6.1-1.el7 will be installed  
---> Package nginx-filesystem.noarch 1:1.20.1-9.el7 will be installed  
---> Package openssl11-libs.x86_64 1:1.1.1k-2.el7 will be installed  
--> Finished Dependency Resolution  
  
Dependencies Resolved  
  
========================================================================================================================  
 Package                           Arch                    Version                          Repository             Size  
========================================================================================================================  
Installing:  
 nginx                             x86_64                  1:1.20.1-9.el7                   epel                  587 k  
Installing for dependencies:  
 centos-indexhtml                  noarch                  7-9.el7.centos                   base                   92 k  
 gperftools-libs                   x86_64                  2.6.1-1.el7                      base                  272 k  
 nginx-filesystem                  noarch                  1:1.20.1-9.el7                   epel                   24 k  
 openssl11-libs                    x86_64                  1:1.1.1k-2.el7                   epel                  1.5 M  
  
Transaction Summary  
========================================================================================================================  
Install  1 Package (+4 Dependent packages)  
  
Total download size: 2.4 M  
Installed size: 6.7 M  
Is this ok \[y/d/N\]: y  
Downloading packages:  
(1/5): centos-indexhtml-7-9.el7.centos.noarch.rpm                                                |  92 kB  00:00:00  
(2/5): gperftools-libs-2.6.1-1.el7.x86_64.rpm                                                    | 272 kB  00:00:00  
(3/5): nginx-1.20.1-9.el7.x86_64.rpm                                                             | 587 kB  00:00:00  
(4/5): nginx-filesystem-1.20.1-9.el7.noarch.rpm                                                  |  24 kB  00:00:00  
(5/5): openssl11-libs-1.1.1k-2.el7.x86_64.rpm                                                    | 1.5 MB  00:00:00  
------------------------------------------------------------------------------------------------------------------------  
Total                                                                                   3.0 MB/s | 2.4 MB  00:00:00  
Running transaction check  
Running transaction test  
Transaction test succeeded  
Running transaction  
Warning: RPMDB altered outside of yum.  
** Found 1 pre-existing rpmdb problem(s), 'yum check' output follows:  
sysstat-10.1.5-19.el7.x86_64 has missing requires of libsensors.so.4()(64bit)  
  Installing : 1:openssl11-libs-1.1.1k-2.el7.x86_64                                                                 1/5  
  Installing : gperftools-libs-2.6.1-1.el7.x86_64                                                                   2/5  
  Installing : 1:nginx-filesystem-1.20.1-9.el7.noarch                                                               3/5  
  Installing : centos-indexhtml-7-9.el7.centos.noarch                                                               4/5  
  Installing : 1:nginx-1.20.1-9.el7.x86_64                                                                          5/5  
  Verifying  : centos-indexhtml-7-9.el7.centos.noarch                                                               1/5  
  Verifying  : 1:nginx-filesystem-1.20.1-9.el7.noarch                                                               2/5  
  Verifying  : gperftools-libs-2.6.1-1.el7.x86_64                                                                   3/5  
  Verifying  : 1:openssl11-libs-1.1.1k-2.el7.x86_64                                                                 4/5  
  Verifying  : 1:nginx-1.20.1-9.el7.x86_64                                                                          5/5  
  
Installed:  
  nginx.x86_64 1:1.20.1-9.el7  
  
Dependency Installed:  
  centos-indexhtml.noarch 0:7-9.el7.centos gperftools-libs.x86_64 0:2.6.1-1.el7 nginx-filesystem.noarch 1:1.20.1-9.el7  
  openssl11-libs.x86_64 1:1.1.1k-2.el7  
  
Complete!  
```
  
  3. Check yum history and undo NGINX installation.  
  
```
vladimir@localhost:~$ sudo yum history  
Loaded plugins: fastestmirror, product-id, search-disabled-repos, subscription-manager  
  
This system is not registered with an entitlement server. You can use subscription-manager to register.  
  
ID     | Command line             | Date and time    | Action(s)      | Altered    
-------------------------------------------------------------------------------    
    28 | install nginx            | 2021-12-21 21:31 | Install        |    5 P<  
    27 | update                   | 2021-12-21 00:11 | I, U           |    4 >  
    26 | install python3          | 2021-12-20 19:35 | Install        |    4  
    25 | install sg3_utils        | 2021-12-17 20:11 | Install        |    2  
    24 | install nc               | 2021-12-15 02:37 | Install        |    2  
    23 | autoremove monitorix     | 2021-12-14 23:23 | Erase          |  109 EE  
    22 | install monitorix        | 2021-12-14 22:46 | Install        |   82  
    21 | install mtr              | 2021-12-14 22:43 | Install        |    1  
    20 | install bind-utils       | 2021-12-14 22:30 | Install        |    6  
    19 | install htop             | 2021-12-07 21:38 | Install        |    1  
    18 | install kubernetes       | 2021-12-07 18:23 | Install        |   49  
    17 | install net-tools -y     | 2021-12-07 12:42 | Install        |    1  
    16 | install mc               | 2021-12-06 22:23 | Install        |    1  
    15 | remove kernel.x86_64 -y  | 2021-12-04 11:22 | Erase          |    1  
    14 | remove kernel-headers.x8 | 2021-12-04 11:21 | Erase          |    1  
    13 | remove kernel-devel.x86_ | 2021-12-04 11:19 | Erase          |    1  
    12 | -y install kernel-header | 2021-12-04 11:16 | Install        |   29  
    11 | update                   | 2021-12-04 11:12 | I, U           |  108  
    10 | install bzip2            | 2021-12-03 19:46 | Install        |    1  
     9 | install nfs-utils        | 2021-12-03 19:34 | Install        |   16  
history list  
```  
  
  4. Disable NGINX repository.  

```
vladimir@localhost:~$ sudo yum update --disablerepo=nginx
Loaded plugins: fastestmirror, product-id, search-disabled-repos, subscription-manager

This system is not registered with an entitlement server. You can use subscription-manager to register.

Loading mirror speeds from cached hostfile
 * base: mirror.tversu.ru
 * extras: mirror.axelname.ru
 * updates: mirrors.datahouse.ru
No packages marked for update
```
  
  5. Remove sysstat package installed in the first task.  

```
vladimir@localhost:~$ sudo yum erase sysstat
Loaded plugins: fastestmirror, product-id, search-disabled-repos, subscription-
              : manager

This system is not registered with an entitlement server. You can use subscripti                      on-manager to register.

Resolving Dependencies
--> Running transaction check
---> Package sysstat.x86_64 0:10.1.5-19.el7 will be erased
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package         Arch           Version                 Repository         Size
================================================================================
Removing:
 sysstat         x86_64         10.1.5-19.el7           installed         1.1 M

Transaction Summary
================================================================================
Remove  1 Package

Installed size: 1.1 M
Is this ok [y/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : sysstat-10.1.5-19.el7.x86_64                                 1/1
  Verifying  : sysstat-10.1.5-19.el7.x86_64                                 1/1

Removed:
  sysstat.x86_64 0:10.1.5-19.el7

Complete!
```
  
  6. Install EPEL repository and get information about it.  

```
  
vladimir@localhost:\~$ yum repoinfo epel  
Loaded plugins: fastestmirror, product-id, search-disabled-repos, subscription-manager  
Determining fastest mirrors  
 * base: mirror.sale-dedic.com  
 * epel: mirror.cspacehostings.com  
 * extras: mirror.axelname.ru  
 * updates: mirror.axelname.ru  
Repo-id      : epel/x86_64  
Repo-name    : Extra Packages for Enterprise Linux 7 - x86_64  
Repo-status  : enabled  
Repo-revision: 1640051136  
Repo-updated : Tue Dec 21 04:51:14 2021  
Repo-pkgs    : 13,694   
Repo-size    : 16 G  
Repo-metalink: https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=x86_64&infra=stock&content=centos  
  Updated    : Tue Dec 21 04:51:14 2021  
Repo-baseurl : https://mirror.cspacehostings.com/epel/7/x86_64/ (98 more)  
Repo-expire  : 21,600 second(s) (last: Tue Dec 21 21:31:29 2021)  
  Filter     : read-only:present  
Repo-filename: /etc/yum.repos.d/epel.repo  
  
repolist: 13,694 
```

  
  7. Find how much packages provided exactly by EPEL repository.  

```
...
Repo-pkgs    : 13,694
...
```
  
  8. Install ncdu package from EPEL repo.  
    
 ``` 
vladimir@localhost:~$ sudo yum repo-pkgs epel install ncdu  
Loaded plugins: fastestmirror, product-id, search-disabled-repos, subscription-manager  
  
This system is not registered with an entitlement server. You can use subscription-manager to register.  
  
Loading mirror speeds from cached hostfile  
 * base: mirror.tversu.ru  
 * epel: mirror.cspacehostings.com  
 * extras: mirror.axelname.ru  
 * updates: mirrors.datahouse.ru  
Resolving Dependencies  
--> Running transaction check  
---> Package ncdu.x86_64 0:1.16-1.el7 will be installed  
--> Finished Dependency Resolution  
  
Dependencies Resolved  
  
========================================================================================================================  
 Package                   Arch                        Version                          Repository                 Size  
========================================================================================================================  
Installing:  
 ncdu                      x86_64                      1.16-1.el7                       epel                       53 k  
  
Transaction Summary  
========================================================================================================================  
Install  1 Package  
  
Total download size: 53 k  
Installed size: 89 k  
Is this ok [y/d/N]: y  
Downloading packages:  
ncdu-1.16-1.el7.x86_64.rpm                                                                       |  53 kB  00:00:00  
Running transaction check  
Running transaction test  
Transaction test succeeded  
Running transaction  
  Installing : ncdu-1.16-1.el7.x86_64                                                                               1/1  
  Verifying  : ncdu-1.16-1.el7.x86_64                                                                               1/1  
  
Installed:  
  ncdu.x86_64 0:1.16-1.el7  
  
Complete!  
```  
    
## _Задача 2_  
  
- Вопрос 1:    
  "Find all regular files below 100 bytes inside your home directory"  
 
 ```
 vladimir@localhost:~$ find ~ -type f -size -100k -exec ls -lh {} +  
-rw-rw-r--. 1 vladimir vladimir    0 Dec  8 19:05 /home/vladimir/1out.txt  
-rw-rw-r--. 1 vladimir vladimir    0 Dec  8 19:05 /home/vladimir/2err.txt  
-rw-rw-r--. 1 vladimir vladimir   24 Dec  3 17:49 /home/vladimir/abs_path.txt  
-rw-rw-r--. 1 vladimir vladimir  777 Dec  8 17:49 /home/vladimir/awkENV.txt  
-rw-r--r--. 1 vladimir vladimir 3.3K Nov 29 22:35 /home/vladimir/.bashrc  
-rw-rw-r--. 1 vladimir vladimir  664 Dec  7 21:39 /home/vladimir/.config/htop/htoprc  
-rw-rw-r--. 1 vladimir vladimir 3.3K Dec  6 22:40 /home/vladimir/Download/Logs/test.log  
-rwxrwxr-x. 1 vladimir vladimir  120 Dec  8 20:10 /home/vladimir/echo_delay.sh  
-rwxrwxrwx. 1 vladimir vladimir   89 Dec  8 19:49 /home/vladimir/echo.sh  
-rw-rw-r--. 1 vladimir vladimir   58 Dec  8 17:59 /home/vladimir/err.log  
-rw-rw-r--. 1 vladimir vladimir   55 Dec  3 18:29 /home/vladimir/errors.txt  
-rw-------. 1 vladimir vladimir  234 Dec 20 22:07 /home/vladimir/.lesshst  
-rwxrwxr-x. 1 vladimir vladimir  642 Dec  8 18:14 /home/vladimir/ls_abs.sh  
-rw-rw-r--. 1 vladimir vladimir  169 Dec 14 20:50 /home/vladimir/.profile  
-rwxrwxr-x. 1 vladimir vladimir  320 Dec  3 17:26 /home/vladimir/script_up.sh  
-rw-------. 1 vladimir vladimir  118 Dec 15 00:45 /home/vladimir/.ssh/config  
-rw-------. 1 vladimir vladimir 1.7K Dec 15 00:03 /home/vladimir/.ssh/hw-5  
-rw-r--r--. 1 vladimir vladimir  412 Dec 15 00:03 /home/vladimir/.ssh/hw-5.pub  
-rw-r--r--. 1 vladimir vladimir  347 Dec 15 02:12 /home/vladimir/.ssh/known_hosts  
-rw-rw-r--. 1 vladimir vladimir    0 Dec  8 17:59 /home/vladimir/task2.txt  
-rw-rw-r--. 1 vladimir vladimir   24 Dec  8 18:00 /home/vladimir/Temp/err.log  
-rw-rw-r--. 1 vladimir vladimir  967 Dec  7 21:47 /home/vladimir/.toprc  
 ```   
    
- Вопрос 2:  
  "Find an inode number and a hard links count for the root directory. The hard link count should be about 17. Why?"  
    
```
vladimir@localhost:~$ ls -ia /  
      64 .         1025 dev         82 lib64         1 proc   8426163 share   8460952 usr  
      64 ..     4194369 etc   12583333 media   8409153 root   8460991 srv    12582977 var  
     120 bin    8460990 home        83 mnt        8060 run          1 sys  
      64 boot       124 lib    4195356 opt         125 sbin   4194376 tmp  
	    
vladimir@localhost:~$ stat /  
  File: ‘/’  
  Size: 237             Blocks: 0          IO Block: 4096   directory    
Device: fd00h/64768d    Inode: 64          Links: 18  
Access: (0555/dr-xr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)  
Context: system_u:object_r:root_t:s0  
Access: 2021-12-21 20:44:55.270405299 +0300  
Modify: 2021-12-08 15:33:01.204733328 +0300  
Change: 2021-12-08 15:33:01.204733328 +0300  
 Birth: -  
  _Answer:_     
  Each real directory is a hardlink by nature, so root directory has all hardlinks for subdirectories and hardlink to itself. Some sudirectories are soft links to other directories, so they are not counted as hardlinks.    
```  
   
- Вопрос 3:  
  "Check what inode numbers have "/" and "/boot" directory. Why?"  
    
```  
vladimir@localhost:~$ ls -ila /  
total 20  
      64 dr-xr-xr-x.  18 root root  237 Dec  8 15:33 .  
      64 dr-xr-xr-x.  18 root root  237 Dec  8 15:33 ..  
     120 lrwxrwxrwx.   1 root root    7 Nov 25 19:04 bin -> usr/bin  
      64 dr-xr-xr-x.   5 root root 4096 Dec 21 20:45 boot  
	  ....  
	    
vladimir@localhost:~$ findmnt    
TARGET                                SOURCE      FSTYPE     OPTIONS  
/                                     /dev/mapper/centos-root  
                                                  xfs        rw,relatime,seclabel,attr2,inode64,noquo  
├─/sys                                sysfs       sysfs      rw,nosuid,nodev,noexec,relatime,seclabel  
│ ├─/sys/kernel/security              securityfs  securityfs rw,nosuid,nodev,noexec,relatime  
│ ├─/sys/fs/cgroup                    tmpfs       tmpfs      ro,nosuid,nodev,noexec,seclabel,mode=755  
│ │ ├─/sys/fs/cgroup/systemd          cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/memory           cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/perf_event       cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/devices          cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/blkio            cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/hugetlb          cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/cpu,cpuacct      cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/cpuset           cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/net_cls,net_prio cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ ├─/sys/fs/cgroup/freezer          cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ │ └─/sys/fs/cgroup/pids             cgroup      cgroup     rw,nosuid,nodev,noexec,relatime,seclabel  
│ ├─/sys/fs/pstore                    pstore      pstore     rw,nosuid,nodev,noexec,relatime  
│ ├─/sys/kernel/config                configfs    configfs   rw,relatime  
│ ├─/sys/fs/selinux                   selinuxfs   selinuxfs  rw,relatime  
│ └─/sys/kernel/debug                 debugfs     debugfs    rw,relatime  
├─/proc                               proc        proc       rw,nosuid,nodev,noexec,relatime  
│ └─/proc/sys/fs/binfmt_misc          systemd-1   autofs     rw,relatime,fd=36,pgrp=1,timeout=0,minpr  
│   └─/proc/sys/fs/binfmt_misc        binfmt_misc binfmt_mis rw,relatime  
├─/dev                                devtmpfs    devtmpfs   rw,nosuid,seclabel,size=1928308k,nr_inod  
│ ├─/dev/shm                          tmpfs       tmpfs      rw,nosuid,nodev,seclabel  
│ ├─/dev/pts                          devpts      devpts     rw,nosuid,noexec,relatime,seclabel,gid=5  
│ ├─/dev/mqueue                       mqueue      mqueue     rw,relatime,seclabel  
│ └─/dev/hugepages                    hugetlbfs   hugetlbfs  rw,relatime,seclabel  
├─/run                                tmpfs       tmpfs      rw,nosuid,nodev,seclabel,mode=755  
│ └─/run/user/1000                    tmpfs       tmpfs      rw,nosuid,nodev,relatime,seclabel,size=3  
├─/boot                               /dev/sda1   xfs        rw,relatime,seclabel,attr2,inode64,noquo  
└─/var/lib/nfs/rpc_pipefs             sunrpc      rpc_pipefs rw,relatime  
  
   _Answer:_     
   These are different mount points for different devices/filesystems, so they can share same inode number without real cross.   
```  
    
- Вопрос 4:  
  "Check the root directory space usage by du command. Compare it with an information from df. If you find differences, try to find out why it happens."  
    
```
vladimir@localhost:~$ sudo du -sh /  
du: cannot access ‘/proc/5004/task/5004/fd/3’: No such file or directory  
du: cannot access ‘/proc/5004/task/5004/fdinfo/3’: No such file or directory  
du: cannot access ‘/proc/5004/fd/4’: No such file or directory  
du: cannot access ‘/proc/5004/fdinfo/4’: No such file or directory  
2.7G    /  
vladimir@localhost:~$ df -h /  
Filesystem               Size  Used Avail Use% Mounted on  
/dev/mapper/centos-root  6.2G  2.6G  3.7G  41% /  
```  
    
- Вопрос 5:  
  "Check disk space usage of /var/log directory using ncdu"  
    
```
vladimir@localhost:~$ ncdu /var/log  
ncdu 1.16 ~ Use the arrow keys to navigate, press ? for help  
--- /var/log ----------------------------------------------------------------------------------------  
    1.9 MiB \[##############] /anaconda  
    1.0 MiB \[#######       ]  messages-20211221  
  964.0 KiB \[######        ]  monitorix  
  308.0 KiB \[##            ]  messages-20211214  
  284.0 KiB \[##            ]  messages-20211203  
  116.0 KiB \[              ]  secure-20211221  
  104.0 KiB \[              ]  wtmp    
   92.0 KiB \[              ]  secure-20211214  
   64.0 KiB \[              ]  boot.log-20211220  
   36.0 KiB \[              ]  boot.log-20211217  
.....  
```
