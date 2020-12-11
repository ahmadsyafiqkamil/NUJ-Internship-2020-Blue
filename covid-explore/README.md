# R

## Install ruODK

```
if (!requireNamespace("remotes")) install.packages("remotes")
remotes::install_github("ropensci/ruODK@main", dependencies = TRUE)
```
jika error, ganti menjadi force
```
install.packages("remotes")
remotes::install_github("ropensci/ruODK@main", force = TRUE)
```
