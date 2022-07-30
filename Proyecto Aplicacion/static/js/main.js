const loginForm = document.getElementById("formularioDeLogueo");



loginForm.addEventListener("submit", async e => {
    e.preventDefault();

    const user = loginForm["user"].value;
    const pass = loginForm["pass"].value;

    const respuesta = await fetch("/api/users",{
        method:"POST",
        headers:{
        contentType: "aplication/json"
        },
        body: JSON.stringify({
            user,
            pass
        })
    })

})

const data = await respuesta.JSON();

console.log(data);

loginForm.reset()
