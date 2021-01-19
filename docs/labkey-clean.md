# Install LabKey-dev
*dicoba di Linux

## Install Required Prerequisites

### Create Folder Structure
```
sudo mkdir -p /usr/local/labkey/apps
sudo mkdir -p /usr/local/labkey/backups
sudo mkdir -p /usr/local/labkey/labkey
sudo mkdir -p /usr/local/labkey/labkey/externalModules
sudo mkdir -p /usr/local/labkey/src
sudo mkdir -p /usr/local/labkey/tomcat-tmp
```

### Java
```
cd /usr/local/labkey/src

sudo wget https://download.java.net/java/GA/jdk15.0.1/51f4f36ad4ef43e39d0dfdbaf6549e32/9/GPL/openjdk-15.0.1_linux-x64_bin.tar.gz

sudo tar -xvzf openjdk-15.0.1_linux-x64_bin.tar.gz -C /usr/local/labkey/apps/

sudo ln -s /usr/local/labkey/apps/jdk-15.0.1 /usr/local/java

sudo nano /etc/profile

# Add the following lines to the end of the file:

export JAVA_HOME="/usr/local/java"
export PATH=$PATH:$JAVA_HOME/bin

source /etc/profile

```


### Tomcat

```
cd /usr/local/labkey/src

sudo wget https://downloads.apache.org/tomcat/tomcat-9/v9.0.41/bin/apache-tomcat-9.0.41.tar.gz

sudo tar -xvzf apache-tomcat-9.0.41.tar.gz -C /usr/local/labkey/apps

sudo ln -s /usr/local/labkey/apps/apache-tomcat-9.0.41 /usr/local/tomcat

```
#Confirm the Java and Tomcat installations by runing the Tomcat startup script:
```
sudo /usr/local/labkey/apps/apache-tomcat-9.0.41/bin/startup.sh
```
Enter the following URL in a web browser:

http://localhost:8080

```
sudo /usr/local/labkey/apps/apache-tomcat-9.0.41/bin/shutdown.sh
```

### PostgreSQL
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
```

### Clone LabKey Source Files from GitHub



```
git clone https://github.com/LabKey/server.git labkeyHome

cd labkeyHome/server/modules/

git clone https://github.com/LabKey/platform.git

git clone https://github.com/LabKey/commonAssays.git

cd ../

git clone https://github.com/LabKey/testAutomation.git

cd modules/platform/

git checkout release21.1-SNAPSHOT

```

### Gradle Configuration


## Referensi

https://www.labkey.org/Documentation/wiki-page.view?name=devMachine

https://www.labkey.org/Documentation/wiki-page.view?name=simpleModules

https://www.labkey.org/Documentation/wiki-page.view?name=installComponents