# Penjelasan OpenDataKit (ODK)

[OpenDataKit](https://getodk.org/) (ODK) merupakan *open-source software* dan gratis yang membantu untuk mengumpulkan data dengan cepat, akurat, offline, dan dalam skala besar [[1]](#1).

[ODK Central](https://docs.getodk.org/central-intro/) adalah *data clearinghouse* berbasis cloud yang menggantikan software [ODK Aggregate](https://docs.getodk.org/aggregate-intro/). ODK Central mengelola akun pengguna dan izin, menyimpan definisi formulir, dan memungkinkan user pengumpulan data seperti ODK Collect.

![odk-central](./img/odk-central.png)

# Install ODK Central
## Install ODK Central di Local Linux [[2]](#2)

1. Download repository / software dari github

```
git clone https://github.com/getodk/central
```

Masuk ke folder odk central

```
cd central
```

Download komponen / submodul software

```
git submodule update -i
```

![install-odk-central](./img/install-odk-central-1.png)

2. Edit setting / environment docker untuk ODK Central

```
nano .env
```

Ubah settingan menjadi seperti di bawah ini
```
SSL_TYPE=selfsign
DOMAIN=localhost
SYSADMIN_EMAIL=okkymabrur@gmail.com
```

*SYSADMIN_EMAIL diisi email admin

![install-odk-central](./img/install-odk-central-2.png)



3. Menggabungkan semuanya dengan docker

```
docker-compose build
```
![install-odk-central](./img/install-odk-central-3.png)

Tunggu sampai semua terunduh dan terinstall

![install-odk-central](./img/install-odk-central-4.png)

Ketika semua sudah terinstall maka akan muncul teks **Successfully built**. Kemudian lakukan `docker compose`  tunggu prosesnya sampai selesai.

```
docker-compose up --no-start
```

![install-odk-central](./img/install-odk-central-5.png)
![install-odk-central](./img/install-odk-central-6.png)

Anda akan melihat terminal seperti gambar di atas jika `docker compose` telah selesai


4. Start ODK Central

```
docker-compose up -d
```

![install-odk-central](./img/install-odk-central-7.png)


5. Setting Akun Administrator

```
docker-compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-create

docker-compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-promote

```

Misalkan

```
docker-compose exec service odk-cmd --email okkymabrur@gmail.com user-create

docker-compose exec service odk-cmd --email okkymabrur@gmail.com user-promote

```

![install-odk-central](./img/install-odk-central-8.png)


6. Masuk ke ODK Central

Masuk ke https://localhost/

Jika muncul warning / peringatan, abaikan dan lanjutkan.

![install-odk-central](./img/install-odk-central-9.png)

Masukkan akun dan password

![install-odk-central](./img/install-odk-central-10.png)

ODK berhasil terinstall

![install-odk-central](./img/install-odk-central-11.png)



# Referensi
<a id="1">[1]</a> 
https://docs.ropensci.org/ruODK/

<a id="2">[2]</a> 
https://docs.getodk.org/central-install-digital-ocean/