

function displayImage(){
    var selectedValue = document.getElementById("partnerSelect").value;
    var image1 = document.getElementById("image1");
    var image2 = document.getElementById("image2");
    var image3 = document.getElementById("image3");
    
    // Esconda todas as imagens
    image1.style.display = "none";
    image2.style.display = "none";
    image3.style.display = "none";

    // Exiba a imagem com base na opção selecionada
    if (selectedValue === "Saude infantil Global") {
        image1.style.display= "block";
        image1.src = img1;
    } else if (selectedValue === "Crianças Criativas") {
        image2.style.display= "block"
        image2.src = img2;
    } else if (selectedValue === "Crianças pela Igualdade") {
        image3.style.display= "block"
        image3.src = img3;
    } 
}
