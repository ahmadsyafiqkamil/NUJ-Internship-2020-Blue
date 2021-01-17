# Install LabKey-dev
*dicoba di Linux

## Install Required Prerequisites


### Java
```
sudo mkdir -p /usr/java/oracle

cd /usr/java/oracle

wget https://github.com/AdoptOpenJDK/openjdk15-binaries/releases/download/jdk-15.0.1%2B9/OpenJDK15U-jdk_x64_linux_hotspot_15.0.1_9.tar.gz

```


### Tomcat
```
# Install the OpenJDK
sudo apt update
sudo apt install default-jdk

# Create Tomcat User
sudo useradd -r -m -U -d /opt/tomcat -s /bin/false tomcat

wget http://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.27/bin/apache-tomcat-9.0.27.tar.gz -P /tmp

sudo tar xf /tmp/apache-tomcat-9*.tar.gz -C /opt/tomcat


```

### PostgreSQL


### Clone LabKey Source Files from GitHub

```
sudo mkdir -p /usr/local/labkey/apps
sudo mkdir -p /usr/local/labkey/backups
sudo mkdir -p /usr/local/labkey/labkey
sudo mkdir -p /usr/local/labkey/labkey/externalModules
sudo mkdir -p /usr/local/labkey/src
sudo mkdir -p /usr/local/labkey/tomcat-tmp
```

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

https://www.labkey.org/Documentation/wiki-page.view?name=installComponents#tom