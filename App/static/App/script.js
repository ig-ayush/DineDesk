const profile_pic = ["image-1.jpg", "image-2.jpg"];
const pic_con = document.getElementById("pro-pic");

function switchImage() {
  const randomImage = Math.floor(Math.random() * profile_pic.length);
  console.log(profile_pic[randomImage]);
  pic_con.style.backgroundImage = `url(images/${profile_pic[randomImage]})`;
}

setInterval(switchImage, 5000);
