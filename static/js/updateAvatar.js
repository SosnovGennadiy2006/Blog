var buttons = document.querySelectorAll('.input-file input[type=file]');
var texts = document.querySelectorAll('.input-file span');
var image = document.getElementById('image');
var ifImageEmpty = document.querySelector('.ifEmpty');
var result = document.querySelector('.result');

result.style.display = 'none';

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('change', () => {
        if (buttons[i].files.length != 0)
        {
            let file = buttons[i].files[0];
            texts[i].innerHTML = file.name;
            
            let reader = new FileReader();

            reader.readAsDataURL(file);

            reader.onload = () => {
                image.src = reader.result;
                result.style.display = 'block';
                ifImageEmpty.style.display = 'none';
            };
        }else
        {
            texts[i].innerHTML = 'Select file';
            result.style.display = 'none';
            ifImageEmpty.style.display = 'flex';
            image.src = '/media/profile/default.png';
        }
    });
}