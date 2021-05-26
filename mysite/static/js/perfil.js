let modal = document.getElementById("modal")
let modalpassword = document.getElementById("modalpassword")
let modalimage = document.getElementById("modalimage")

function modalTrigger(){
        if (modal.className === "modal is-active") {
            modal.className = "modal"
        } else {
            modal.className = "modal is-active";
        }
    }

function modalpasswordTrigger(){
        if (modalpassword.className === "modal is-active") {
            modalpassword.className = "modal"
        } else {
            modalpassword.className = "modal is-active";
        }
    }

function modalimageTrigger(){
        if (modalimage.className === "modal is-active") {
            modalimage.className = "modal"
        } else {
            modalimage.className = "modal is-active";
        }
    }

function toggle() {
    let field = document.getElementById("id_first_name")
    if (field.disabled === true){
        field.disabled = false;
        document.getElementById("id_last_name").disabled = false;
        document.getElementById("id_email").disabled = false;
        document.getElementById("cancel").style.display = 'inline-block';
        document.getElementById("save").style.display = 'inline-block';
        document.getElementById("editor").style.display = 'none';
    }
    else {
        field.disabled = true;
        document.getElementById("id_last_name").disabled = true;
        document.getElementById("id_email").disabled = true;

    }


}