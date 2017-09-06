 var maxweights = document.querySelectorAll(".maxweight");
  var currentweights = document.querySelectorAll(".currentweight");
  var overweights = document.querySelectorAll(".overweight");
  for(j = 0; j < currentweights.length; j++)
  {
  var maxweight = parseFloat(maxweights[j].innerHTML);
  var currentweight = parseFloat(currentweights[j].innerHTML);
  
  
  var overweight = Math.max(0.0, 100 * (currentweight - maxweight) / maxweight);
  overweights[j].innerHTML = overweight.toFixed(2).toString();
  }