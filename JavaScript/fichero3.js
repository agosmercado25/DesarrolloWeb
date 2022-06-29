//codigo javascript

var valor = 0;

while (valor < 4){
  //codigo que se ejecuta de forma repetitiva hasta que ya no se cumpla
  //la condicion
  console.log("Valor es igual a " + valor);
  console.log("Valor es menor que 4, entonces le sumo 1 a la variable valor");

  if (valor == 2){
    console.log("Ahora valor es igual a 2 y quiero parar la ejecución del bucle");
    break;
  }
  valor = valor + 1;
}
