const form = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const responseDiv = document.getElementById('response');
const teachForm = document.getElementById('teach-form');
const newResponseInput = document.getElementById('new-response');
const teachButton = document.getElementById('teach-button');
let lastQuestion = "";

form.onsubmit = async (e) => {
    e.preventDefault();  // Evita recarregar a página
    const formData = new FormData(form);
    lastQuestion = userInput.value;
    
    // Envia a pergunta para o backend e processa a resposta JSON
    const response = await fetch('/chatbot', {
        method: 'POST',
        body: formData
    });
    const botResponse = await response.json();

    // Exibe apenas o campo "answer" da resposta do bot
    responseDiv.innerText = `Bot: ${botResponse.answer}`;
    
    // Se o bot não conhece a resposta, mostra o campo de ensino
    if (!botResponse.known) {
        teachForm.style.display = "block";
    } else {
        teachForm.style.display = "none";
    }
};

teachButton.onclick = async () => {
    const newResponse = newResponseInput.value;
    if (newResponse) {
        const formData = new FormData();
        formData.append('pergunta', lastQuestion);
        formData.append('resposta', newResponse);

        const response = await fetch('/ensinar', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();


        responseDiv.innerText = `Bot: ${result.message}`;
        teachForm.style.display = "none";
        newResponseInput.value = "";
    } else {
        alert("Digite uma resposta para ensinar ao bot!");
    }
};
