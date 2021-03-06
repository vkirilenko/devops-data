## _Task 1: Users and groups_

- Вопрос:  
  "Создайте группу sales с GID 4000 и пользователей bob, alice, eve c основной группой sales. 
  Измените пользователям пароли.
  Все новые аккаунты должны обязательно менять свои пароли каждый 30 дней.
  Новые аккаунты группы sales должны истечь по окончанию 90 дней срока, а bob должен изменять его пароль каждые 15 дней.
  Заставьте пользователей сменить пароль после первого логина."  
  
  _Command:_ __sudo groupadd sales -g 4000__
                __sudo useradd -m alice; sudo useradd -m bob; sudo useradd -m eve__  
                __sudo passwd alice__  
                __sudo passwd bob__  
			      __sudo passwd eve__  
			      __sudo usermod -aG sales -e 2022-04-07 alice; sudo usermod -aG sales -e 2022-04-07 bob; sudo usermod -aG sales -e 2022-04-07 eve__  
			      __sudo shage -d0 alice; sudo shage -d0 bob; sudo shage -d0 eve__  
			      __sudo chage -M 15 bob__  
    
  _Result:_  
  ![1.1](img/1.1.png)
  ![1.2](img/1.2.png)
  ![1.3](img/1.3.png)
  ![1.4](img/1.4.png)
  ![1.5](img/1.5.png)
  ![1.6](img/1.6.png)
 
 
## _Task 2: Controlling access to files with Linux file system permissions_

- Вопрос:  
  "Создайте трёх пользователей glen, antony, lesly.
  У вас должна быть директория /home/students, где эти три пользователя могут работать совместно с файлами.
  Должен быть возможен только пользовательский и групповой доступ, создание и удаление файлов в /home/students. 
  Файлы, созданные в этой директории, должны автоматически присваиваться группе студентов students."  
  
  _Command:_ __sudo groupadd students__    
                     __sudo useradd -G students antony; sudo useradd -G students lesly; sudo useradd -G students glen__      
                     __sudo mkdir /home/students__    
					   __sudo chown :students /home/students ; sudo chmod g+sw /home/students__    
  
  _Result:_  
  ![2.1](img/2.1.png)
  ![2.2](img/2.2.png)
  ![2.3](img/2.3.png)
  ![2.4](img/2.4.png)
  
  
## _Task 3: Controlling access to files with Linux file system permissions_

- Вопрос:  
   - От суперпользователя создайте папку /share/cases и создайте внутри 2 файла murders.txt и moriarty.txt.
   - Создайте общую директорию /share/cases.
   - Создайте группу bakerstreet с пользователями holmes, watson.
   - Создайте группу scotlandyard с пользователями lestrade, gregson, jones.
   - Задайте всем пользователям безопасные пароли.
   - Директория и всё её содержимое должно принадлежать группе bakerstreet, при этом файлы должны обновляться для чтения и записи  для владельца и группы (bakerstreet). У других пользователей не должно быть никаких разрешений. 
   - Вам также необходимо предоставить доступы на чтение и запись для группы scotlandyard, за исключением Jones, который может только читать документы.
   - Убедитесь, что ваша настройка применима к существующим и будущим файлам. После установки всех разрешений в директории проверьте от каждого пользователя все его возможные доступы.   

  _Command:_ __sudo groupadd bakerstreet__   
                __sudo useradd -G bakerstreet holmes; sudo useradd -G bakerstreet watson__   
                __sudo groupadd scotlandyard__   
			      __sudo useradd -G scotlandyard lestrade; sudo useradd -G scotlandyard gregson; sudo useradd -G scotlandyard jones__  
                __sudo passwd holmes__  
                __sudo passwd watson__  
			      __sudo passwd lestrade__  
			      __sudo passwd gregson__   
			      __sudo passwd jones__    
			    
vladimir@localhost:\~$ getfacl /share/cases  
getfacl: Removing leading '/' from absolute path names  
\# file: share/cases  
\# owner: root  
\# group: bakerstreet  
user::rwx  
user:jones:r-x  
group::rwx  
group:scotlandyard:rwx  
mask::rwx  
other::---  
default:user::rwx  
default:group::rwx  
default:group:bakerstreet:rw-  
default:group:scotlandyard:rw-  
default:mask::rwx  
default:other::r--  
  

  			  
  _Result:_  
  ![3.1](img/3.1.png)
  ![3.2](img/3.2.png)
  ![3.3](img/3.3.png)
  ![3.4](img/3.4.png)
  ![3.5](img/3.5.png)



 