#Este script grafica datos de la NASA de temperaturas promedio en algunas capitales de Colombia
library(tidyr)
library(dplyr)
library(lubridate)
library(ggplot2)
#para efectuar las descargas se debe ingresar a cada url mientras se descarga

download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_14_0/station.txt', destfile = 'bog.txt', method = 'curl')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_14_0/station.txt', destfile = 'cali.txt', method = 'curl')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_14_0/station.txt', destfile = 'bucar.txt', method = 'curl')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_14_0/station.txt', destfile = 'ipiales.txt', method = 'curl')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_14_0/station.txt', destfile = 'bquilla.txt', method = 'curl')

#guarda los datos descargados en dataframes como se pide en a., header=True porque la primera columna no tiene nombre al inici

bogota = read.table("bog.txt", header = T)
cali = read.table("cali.txt", header = T)
bucaramanga = read.table("bucar.txt", header = T)
barranquilla = read.table("bquilla.txt", header = T)
ipiales = read.table("ipiales.txt", header = T)

#Crea un vector que guarda estas tres variables
datos <- c("año","mes", "temperatura")
bogota <- gather(bogota, mes, temperatura, JAN:DEC)
names(bogota)[1] <- "año"
bogota <- bogota[,datos,drop=FALSE]
cali <- gather(cali, mes, temperatura, JAN:DEC)
names(cali)[1] <- "año"
cali <- cali[,datos,drop=FALSE]
bucaramanga <- gather(bucaramanga, mes, temperatura, JAN:DEC)
names(bucaramanga)[1] <- "año"
bucaramanga <- bucaramanga[,datos,drop=FALSE]
barranquilla <- gather(barranquilla, mes, temperatura, JAN:DEC)
names(barranquilla)[1] <- "año"
barranquilla <- barranquilla[,datos,drop=FALSE]
ipiales <- gather(ipiales, mes, temperatura, JAN:DEC)
names(ipiales)[1] <- "año"
ipiales <- ipiales[,datos,drop=FALSE]


#Adicion datos  faltantes, como se dijo en clase se asumio que los que no tenian dia era 1 enero del respectivo anio, ademas se agregan columnas nuevas

llenar <- function(x) tolower(x) %in% tolower(month.abb)
bogota <- mutate(bogota, fecha = paste(año, llenar(mes), "1", sep="/"))
bogota <- mutate(bogota, ciudad = "Bogota")
print (bogota)
cali <- mutate(cali, fecha = paste(año, llenar(mes), "1", sep="/"))
cali <- mutate(cali, ciudad = "Cali")
print (cali)
bucaramanga <- mutate(bucaramanga, fecha = paste(año, llenar(mes), "1", sep="/"))
bucaramanga <- mutate(bucaramanga, ciudad = "Bucaramanga")
print (bucaramanga)
barranquilla <- mutate(barranquilla, fecha = paste(año, llenar(mes), "1", sep="/"))
barranquilla <- mutate(barranquilla, ciudad = "Barranquilla")
print (barranquilla)
ipiales <- mutate(ipiales, fecha = paste(año, llenar(mes), "1", sep="/"))
ipiales <- mutate(ipiales, ciudad = "Ipiales")
print (ipiales)
#armamos un dataset con solo dichas columnas, de aca sale el csv buscado, ademas se aplica tidy data 

df <- rbind(bogota, cali, bucaramanga, barranquilla, ipiales)
df <- df[c("anio", "mes", "fecha", "ciudad", "temperatura")]
df[df == 999.9] <- NA
#guardamos la grafica en un .png aunque tambien se puede visualizar en Rstudio

a <- ggplot(df, aes(x=fecha,y = temperatura, , color=ciudad)) + geom_point(size=3) 
a <- a + labs(title="Temperatura en algunas Capitales de Colombia 1967-2015") + facet_grid(~ ciudad, scales = "free")
ggsave(filename='temperaturas.png', plot = a)
print(a)

b <- ggplot(df, aes(x=fecha,y = temperatura)) + geom_point(size=3) 
b <- b + labs(title="Temperatura en algunas Capitales de Colombia 1967-2015") + facet_grid(~ ciudad, scales = "free")
ggsave(filename='temperaturasbn.png', plot = a)
print(b)

write.csv(df, file = "temperaturas.csv")
