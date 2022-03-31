#include <stdio.h>
#include <string.h>

#define TAM 20

struct persona{

	char Nombre[TAM];
	char Apellidos[TAM*2];
	int Edad;
	char Genero;
	char Accion_1[TAM];
	char Accion_2[TAM];
	char Accion_3[TAM];
	char Accion_4[TAM];

} Persona = {

	"Cristian Fernando",
	"Carillo Toribio ",
	20,
	'M',
	"Comiendo",
	"Caminando",
	"Hablando",
	"Durmiendo"

};

int main(void){

	printf("\n Persona");
	printf("\n Nombre: %s", Persona.Nombre);
	printf("\n Apellidos: %s", Persona.Apellidos);
	printf("\n Edad: %d", Persona.Edad);
	printf("\n Genero: %c", Persona.Genero);
	printf("\n");
	printf("\n Acciones");
	printf("\n %s esta %s", Persona.Nombre, Persona.Accion_1);
	printf("\n %s esta %s", Persona.Nombre, Persona.Accion_2);
	printf("\n %s esta %s", Persona.Nombre, Persona.Accion_3);
	printf("\n %s esta %s", Persona.Nombre, Persona.Accion_4);

return 0;

}
