document.addEventListener("DOMContentLoaded", () => {
  const images = ["image-1.jpg", "image-2.jpg", "image-3.jpg"];

  const pic = document.getElementById("pro-pic");

  if (!pic) return;

  let index = 0;

  function changeImage() {
    console.log("first");
    pic.style.backgroundImage = `url(/static/App/images/${images[index]})`;
    index = (index + 1) % images.length;
  }

  changeImage();

  setInterval(changeImage, 5000);
});
