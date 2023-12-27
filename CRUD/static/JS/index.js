let up_button = document.querySelector(".show_up_form")

let up_from = document.querySelector(".up_form")

let flag = 1
up_button.onclick = function()
{
    
    up_from.style.cssText = "display: flex"  
};

let add_button = document.querySelector(".show_add_form")
let add_from = document.querySelector(".add_form")

add_button.onclick = function()
{
    
    add_from.style.cssText = "display: flex"  
};