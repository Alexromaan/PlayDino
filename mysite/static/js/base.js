function change_bg_stack_to_clean() {
    document.getElementById('waveWrapper').classList.add('is-hidden');
    document.getElementById('subcontainer').classList.add('bordered-light');
    document.getElementById('current_bg').innerText = "Fondo actual: Seo Clean";
    document.getElementById('username').classList.add('color-black');
    document.getElementById('password').classList.add('color-black');
    document.getElementById('username').classList.remove('color-white');
    document.getElementById('password').classList.remove('color-white');
}

function change_bg_stack_to_anim() {
    document.getElementById('waveWrapper').classList.remove('is-hidden');
    document.getElementById('subcontainer').classList.remove('bordered-light');
    document.getElementById('current_bg').innerText = "Fondo actual: Seo Wave";
    document.getElementById('username').classList.remove('color-black');
    document.getElementById('password').classList.remove('color-black');
    document.getElementById('username').classList.add('color-white');
    document.getElementById('password').classList.add('color-white');
}

document.getElementById('switch').onclick = function () {


    if (localStorage.bgCheck == 0) {
        localStorage.bgCheck = 1;
        change_bg_stack_to_clean()

    } else {
        localStorage.bgCheck = 0;
        change_bg_stack_to_anim()

    }

}

if (!localStorage.bgCheck) {
    localStorage.bgCheck = 0;
    console.log('Set bgCheck');
}
if (localStorage.bgCheck && localStorage.bgCheck == 1) {
    document.getElementById('switch').checked = false;
    change_bg_stack_to_clean();
} else {
    document.getElementById('switch').checked = true;
    change_bg_stack_to_anim();
}

const rmCheck = document.getElementById("rememberMe"),
    username = document.getElementById("username");

if (localStorage.checkbox && localStorage.checkbox !== "") {
    rmCheck.setAttribute("checked", "checked");
    username.value = localStorage.username;
} else {
    rmCheck.removeAttribute("checked");
    username.value = "";
}

function lsRememberMe() {
    if (rmCheck.checked && username.value !== "") {
        localStorage.username = username.value;
        localStorage.checkbox = rmCheck.value;
    } else {
        localStorage.username = "";
        localStorage.checkbox = "";
    }
}