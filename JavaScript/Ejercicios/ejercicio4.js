function media(array){
  media = 0;
  for (var i = 0; i < array.length; i++){
    media = media + array[i];
  }
  return (media/array.length)
}

numeros = [1,4,6,2,9,12,45]
resultado = media(numeros);
console.log("La media del Array es: " + resultado);
