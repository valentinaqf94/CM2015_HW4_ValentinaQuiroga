#Este script grafica datos de la NASA de temperaturas promedio en algunas capitales de Colombia
library(tidyr)
library(dplyr)
library(lubridate)
library(ggplot2)

#para efectuar las descargas se debe ingresar a cada url mientras se descarga

download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_14_0/station.txt', destfile = 'bog.txt', method = 'wget')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_14_0/station.txt', destfile = 'cali.txt', method = 'wget')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_14_0/station.txt', destfile = 'bucar.txt', method = 'wget')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_14_0/station.txt', destfile = 'ipiales.txt', method = 'wget')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_14_0/station.txt', destfile = 'bquilla.txt', method = 'wget')


#guarda los datos descargados en dataframes como se pide en a., header=True porque la primera columna no tiene nombre al inici

bogota = read.table("bog.txt", header = TRUE)
cali = read.table("cali.txt", header = TRUE)
bucaramanga = read.table("bucar.txt", header = TRUE)
barranquilla = read.table("bquilla.txt", header = TRUE)
ipiales = read.table("ipiales.txt", header = TRUE)


#Crea un vector que guarda estas tres variables

datos <- c("año","mes", "temperatura")
bogota <- gather(bogota, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(bogota)[1] <- "año"
bogota <- bogota[,datos,drop=FALSE]
cali <- gather(cali, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(cali)[1] <- "año"
cali <- cali[,datos,drop=FALSE]
bucaramanga <- gather(bucaramanga, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(bucaramanga)[1] <- "año"
bucaramanga <- bucaramanga[,datos,drop=FALSE]
barranquilla <- gather(barranquilla, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(barranquilla)[1] <- "año"
barranquilla <- barranquilla[,datos,drop=FALSE]
ipiales <- gather(ipiales, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(ipiales)[1] <- "año"
ipiales <- ipiales[,datos,drop=FALSE]


#Adicion datos  faltantes, como se dijo en clase se asumio que los que no tenian dia era 1 enero del respectivo anio, ademas se agregan columnas nuevas

llenar <- function(x) match(tolower(x), tolower(month.abb))
bogota <- mutate(bogota, fecha = paste(año, llenar(mes), "1", sep="/"))
bogota <- mutate(bogota, ciudad = "Bogota")
cali <- mutate(cali, fecha = paste(año, llenar(mes), "1", sep="/"))
cali <- mutate(cali, ciudad = "Cali")
bucaramanga <- mutate(bucaramanga, fecha = paste(año, llenar(mes), "1", sep="/"))
bucaramanga <- mutate(bucaramanga, ciudad = "Bucaramanga")
barranquilla <- mutate(barranquilla, fecha = paste(año, llenar(mes), "1", sep="/"))
barranquilla <- mutate(barranquilla, ciudad = "Barranquilla")
ipiales <- mutate(ipiales, fecha = paste(año, llenar(mes), "1", sep="/"))
ipiales <- mutate(ipiales, ciudad = "Ipiales")

#armamos un dataset con solo dichas columnas, de aca sale el csv buscado, ademas se aplica tidy data 

temperaturas <- rbind(bogota, cali, bucaramanga, barranquilla, ipiales)
temperaturas <- temperaturas[c("año", "mes", "fecha", "ciudad", "temperatura")]
temperaturas[temperaturas == 999.9] <- NA
write.csv(temperaturas, file = "temperaturas.csv")


#guardamos la grafica en un .png aunque tambien se puede visualizar en Rstudio

a <- ggplot(temperaturas, aes(x=fecha,y = temperatura, , color=ciudad)) + geom_point() 
a <- a + labs(title="Temperatura en algunas Capitales de Colombia 1967-2015") + facet_grid(~ ciudad, scales = "free")
ggsave(filename='temperaturas.png', plot = a)
print(a)


