var maximo = prompt("Ingrese el valor máximo: ")

var max = parseInt(maximo);

var texto = "";

for (var i = 0; i < (max+1) ; i++){
  if (i % 2 == 0){
    texto = texto + " " + i
  }
}
textofinal = "Los números pares entre 0 y " + max + " son: \n" + texto;
alert(textofinal);
console.log(textofinal);
