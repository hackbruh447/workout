// Get references to the file input and profile image elements
const imageInput = document.getElementById("imageUpload");
const profileImg = document.getElementById("profileImg");

// Listen for a change event on the file input
imageInput.addEventListener("change", function () {
  const file = this.files[0]; // Get the first selected file
  if (file) {
    const reader = new FileReader();
    // When the file is read, set the profile image's src to the file data URL
    reader.addEventListener("load", function () {
      profileImg.src = reader.result;
    });
    reader.readAsDataURL(file); // Read the file as a Data URL (base64)
  }
});
