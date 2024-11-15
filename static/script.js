t = 0;
  let time = setInterval(myTimer ,1000);
  function myTimer() {
    t = t + 1;
    document.getElementById("demo").innerHTML = t;
  }  
