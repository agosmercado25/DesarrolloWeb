var num1 = prompt("Introduce el primer número: ");
var num2 = prompt("Introduce el segundo número: ");
var operacion = prompt("Introduce la operación a realizar: ");

var numero1 = parseInt(num1);
var numero2 = parseInt(num2);

var resultado = null;
var texto = null;

if (operacion == '+'){
  resultado = numero1 + numero2;
  texto = "La operación es " + operacion + " para los números " + numero1 + " y " + numero2 + " y el resultado es " + resultado;
}
else if (operacion == '-') {
  resultado = numero1 - numero2;
  texto = "La operación es " + operacion + " para los números " + numero1 + " y " + numero2 + " y el resultado es " + resultado;
}
else if (operacion == '*') {
  resultado = numero1 * numero2;
  texto = "La operación es " + operacion + " para los números " + numero1 + " y " + numero2 + " y el resultado es " + resultado;
}
else if (operacion == '/') {
  resultado = numero1 / numero2;
  texto = "La operación es " + operacion + " para los números " + numero1 + " y " + numero2 + " y el resultado es " + resultado;
}
else {
  texto = "La operación " + operacion + " no está permitida";
}

alert(texto);
console.log(texto);
