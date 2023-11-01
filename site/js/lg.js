function cadastrarEmail() {
    var email = document.getElementById("email").value;

    let banco = {
        email
    }

    if (email === localStorage.getItem("email")) {
        alert("Já foi adicionada beleza a esse e-mail!")
    } else {

        let criaBanco = JSON.stringify(banco)

        localStorage.setItem("id", criaBanco)

        localStorage.setItem("email", banco.email)

        alert("Foi adicionada beleza ao seu e-mail com Sucesso!")

    }
}
