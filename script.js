// script.js

document.getElementById('profileFile').addEventListener('change', function () {
  const fileName = this.files[0]?.name || "No file selected";
  document.getElementById('profilePreview').textContent = "Selected: " + fileName;
});

document.getElementById('resumeFile').addEventListener('change', function () {
  const fileName = this.files[0]?.name || "No file selected";
  document.getElementById('resumePreview').textContent = "Selected: " + fileName;
});

document.getElementById('jobDescFile').addEventListener('change', function () {
  const fileName = this.files[0]?.name || "No file selected";
  document.getElementById('jobDescPreview').textContent = "Selected: " + fileName;
});
