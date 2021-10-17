const input_fields = document.querySelectorAll('input');
const input_select = document.querySelectorAll('select');
const input_area =  document.querySelectorAll('textarea');




input_fields.forEach(field => {
    field.classList += "form-control";
});

input_select.forEach(field => {
    field.classList += "form-control";
});

input_area.forEach(field => {
    field.classList += "form-control";
});