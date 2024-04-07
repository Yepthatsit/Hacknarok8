const tabs = document.querySelectorAll('[data-tab-target]')
const tabContents = document.querySelectorAll('[data-tab-content]')

tabs[0].classList.add('active');
tabContents[0].classList.add('active');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = document.querySelector(tab.dataset.tabTarget)
    tabContents.forEach(tabContent => {
      tabContent.classList.remove('active')
    })
    tabs.forEach(tab => {
      tab.classList.remove('active')
    })
    tab.classList.add('active')
    target.classList.add('active')
  })
})


function dropHandler(event) {
    event.preventDefault();
    event.target.classList.remove('highlight');

    const file = event.dataTransfer.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const droppedImage = document.getElementById('droppedImage');
            droppedImage.src = e.target.result;
            document.getElementById('dropArea').style.display = 'none';
            document.getElementById('imageContainer').style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}
