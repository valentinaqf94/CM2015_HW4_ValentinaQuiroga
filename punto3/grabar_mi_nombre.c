//script que recibe por parametro la entrada de un archivo de audio de duracion aproximada de 3 segundos, el computador debe tener instalado el paquete sox. La duracion esta sujeta a el eco generado por el emisor de la senial. 

#include <stdio.h>
#include <stdlib.h>

int main(){
	
	puts("Diga su nombre aca");
	char command[100];
	system("rec -c1 -b16 minombre.wav silence -l 0 1 00:00:3.00 1\%");
	return 0;
		

}
