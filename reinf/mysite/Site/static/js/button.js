document.getElementById("toggleButton").addEventListener("click", function() {
  document.getElementById("sidebar").classList.toggle("open");
});

document.getElementById("imageButton").addEventListener("click", function() {
  var image = document.getElementById("imageButton").querySelector("img");
  
  if (image.getAttribute("src") === "imagem1.jpg") {
    image.setAttribute("src", "imagem2.jpg");
    image.setAttribute("alt", "Imagem 2");
  } else {
    image.setAttribute("src", "imagem1.jpg");
    image.setAttribute("alt", "Imagem 1");
  }
});