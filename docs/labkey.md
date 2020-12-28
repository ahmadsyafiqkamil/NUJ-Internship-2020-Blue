# Penjelasan Labkey

LabKey merupakan penyedia perangkat lunak dan layanan profesional yang terspesialisasi dalam membantu organisasi mengatasi manajemen data, kolaborasi, dan alur kerja dalam lingkungan penelitian ilmiah [[1]](#1).

[LabKey Server](https://www.labkey.com/products-services/labkey-server/) merupakan *open-source platform* yang dirancang untuk mengintegrasikan, menganalisis, dan berbagi data biomedis yang kompleks [[2]](#2).


![labkey-server](https://www.labkey.org/Documentation/wiki-download.view?entityId=ab437b7d-869b-1035-8b1a-fe851e083846&name=LabKey-Server-Graphic.png)

# Install Labkey Server
## Install Labkey Server di Local Linux [[3]](#3)

Menggunakan LabKey Server Community edition versi 20.7.

Ini hanya digunakan untuk testing.

1. Download repository dari github

```
git clone https://github.com/LabKey/samples
```
![install-labkey](./img/install-labkey-1.png)


2. Masuk ke folder samples/docker/labkey-20.7-community

```
cd samples/docker/labkey-20.7-community
```

3. Build software dengan docker

```
docker-compose up -d --build
```
![install-labkey](./img/install-labkey-2.png)


4. Buka Labkey di link http://localhost:8080/labkey dan buat akun

![install-labkey](./img/install-labkey-3.png)

5. Untuk stop LabKey service

```
docker-compose down
```



# Referensi
<a id="1">[1]</a> 
https://www.labkey.com/about/

<a id="2">[2]</a> 
https://www.labkey.com/products-services/labkey-server/

<a id="3">[3]</a>
https://github.com/LabKey/samples/tree/master/docker/labkey-20.7-community