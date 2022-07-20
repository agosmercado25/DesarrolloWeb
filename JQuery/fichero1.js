$('h1').click(function(){
  console.log("Se ha pulsado el titular h1");
})

$('li').click(function(){
  console.log("Se ha pulsado sobre algún elemento de la lista");
})

$('p').dblclick(function(){
  console.log("Se ha pulsado dos veces sobre el párrafo");
})

$('input').eq(0).keypress(function(){
  $(this).css('color','red');
  console.log(event);
  if (event.which === 100) {
    //El codigo 100 corresponde a la letra d
    $(this).css('color','green');
  }
})

$('li').eq(0).click(function(){
  //fadeOut() -> numero en milisegundos que se tarda en diseminarse
  $('#id1').fadeOut(2000);
  console.log("Se ha borrado el párrafo");
})

$('li').eq(1).click(function(){
  //fadeOut() -> numero en milisegundos que se tarda en diseminarse
  $('#id1').slideUp(2000);
  console.log("Se ha sobrepuesto con el párrafo");
})
