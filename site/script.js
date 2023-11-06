// async function getCommits(){
//     let user = "insper-classroom"
//     let repo = "projeto-pygame-cinza"

//     let url = `https://api.github.com/repos/${user}/${repo}/commits?per_page=100`

//     let response = await fetch(url, {method: "GET", headers:{}})
//     let responseData = await response.json()

//     let container = document.querySelector("#commits")
//     for (let i in responseData){
//         container.innerHTML += `
//         <p>${responseData[i].commit.author.name} - ${responseData[i].commit.message} | ${responseData[i].commit.author.date}</p>
//         `

//     }

// }

// getCommits()

function gerarLogDeDesenvolvimento() {
    fetch('https://api.github.com/repos/insper-classroom/projeto-pygame-cinza/commits')
    .then(response => response.json())
    .then(commits => {
        const tbody = document.querySelector('#log-table tbody');

        for (const commit of commits) {
        const tr = document.createElement('tr');
        const autorTd = document.createElement('td');
        const dataTd = document.createElement('td');
        const mensagemTd = document.createElement('td');

        autorTd.textContent = commit.commit.author.name;
        dataTd.textContent = formatDate(commit.commit.author.date, 'dd/mm/aaaa');
        mensagemTd.textContent = commit.commit.message;

        tr.appendChild(autorTd);
        tr.appendChild(dataTd);
        tr.appendChild(mensagemTd);

        tbody.appendChild(tr);
        }
    });
}

function formatDate(string, format) {
    const map = {
        dd: string.slice(8,10),
        mm: string.slice(5,7),
        aaaa: string.slice(0,4)
    }

    return format.replace(/dd|mm|aaaa/gi, matched => map[matched])
}

// function scrollToContent(id) {
//     const contentSection = document.getElementById(id);
//     var menu = document.querySelector('header')
//     window.scrollTo({
//       top: contentSection.offsetTop - menu.offsetHeight,
//       behavior: 'smooth'
//     });
// }
// Chama a função para gerar a tabela quando a página é carregada
gerarLogDeDesenvolvimento();