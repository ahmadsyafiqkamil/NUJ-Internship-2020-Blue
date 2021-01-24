# Petunjuk Penggunaan

## Prerequisites
### Download repository

- Download Manual Repository https://github.com/NUJerman/NUJ-Internship-2020-Blue/archive/main.zip

atau

- Clone via CMD/Terminal

`git clone https://github.com/NUJerman/NUJ-Internship-2020-Blue`

Buka folder */pipeline*

via CMD/Terminal: `cd NUJ-Internship-2020-Blue/pipeline`

## Python

### Install package

via pip

`pip install -r requirements.txt`

via conda

`conda install --file requirements.txt`

### Jalankan program

Buka file [Py_pipeline.py](./Py_pipeline.py) atau [Py_pipeline.ipynb](./Py_pipeline.ipynb)

## R

### Install package
```{r}
if (!requireNamespace("remotes")) {
    install.packages("remotes")
}
remotes::install_github("ropensci/ruODK@main",
                        dependencies = TRUE,
                        force = TRUE)
install.packages(c("eeptools", "tidyverse", "ggplot2"))
```

### Jalankan program

Buka file [R_pipeline.rmd](./R_pipeline.rmd)