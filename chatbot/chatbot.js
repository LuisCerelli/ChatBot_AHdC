const toggleBtn = document.getElementById('chatbot-toggle');
const chatbotWindow = document.getElementById('chatbot-window');
const userInput = document.getElementById('chatbot-user-input');
const messagesDiv = document.getElementById('chatbot-messages');

// // Mostrar/ocultar ventana
toggleBtn.addEventListener('click', () => {
  const isOpen = chatbotWindow.style.display === 'flex';
  chatbotWindow.style.display = isOpen ? 'none' : 'flex';
  toggleBtn.style.display = isOpen ? 'block' : 'none';
});

// Enviar mensaje (versión simulada)
async function sendMessage() {
  const mensaje = userInput.value.trim();
  if (!mensaje) return;

  // Mostrar mensaje del usuario
  const userDiv = document.createElement("div");
  userDiv.className = "user-message";
  userDiv.innerText = mensaje;
  messagesDiv.appendChild(userDiv);

  userInput.value = "";
  messagesDiv.scrollTop = messagesDiv.scrollHeight;

  // Mostrar mensaje de "escribiendo..."
  const botDiv = document.createElement("div");
  botDiv.className = "bot-message";
  botDiv.innerText = "⏳ Estoy pensando...";
  messagesDiv.appendChild(botDiv);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;

  try {
    const response = await fetch("https://luisdsai-chatbot-huella-backend-v2.hf.space/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: mensaje })
    });

    const data = await response.json();

    // Reemplazar texto del bot con respuesta real
    if (data.response) {
      botDiv.innerText = data.response;
    } else {
      botDiv.innerText = "❌ Hubo un error con la respuesta.";
    }
  } catch (error) {
    console.error("Error al contactar el backend:", error);
    botDiv.innerText = "🚫 No se pudo conectar al servidor.";
  }

  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}


// Opciones rápidas
function setQuickQuestion(texto) {
  userInput.value = texto;
  sendMessage();
}

// Burbuja de bienvenida
function openChatFromAvatar(event) {
  if (event.target.classList.contains('close-welcome')) return;
  document.getElementById('welcomeBubble').style.display = 'none';
  chatbotWindow.style.display = 'block';
  toggleBtn.style.display = 'none';
}

function closeWelcome(event) {
  event.stopPropagation();
  document.getElementById('welcomeBubble').style.display = 'none';
}

// Cerrar chat
function closeChatbox() {
  chatbotWindow.style.display = "none";
  toggleBtn.style.display = "block";
}

// Mostrar bienvenida solo una vez
window.addEventListener('DOMContentLoaded', () => {
  const bubble = document.getElementById('welcomeBubble');
  const saludoVisto = sessionStorage.getItem('saludoMostrado');

  if (!saludoVisto && bubble) {
    bubble.style.display = 'flex';
    sessionStorage.setItem('saludoMostrado', 'true');
  } else if (bubble) {
    bubble.style.display = 'none';
  }

  // Modo oscuro automático
  const bgColor = window.getComputedStyle(document.body).backgroundColor;
  const rgb = bgColor.match(/\d+/g)?.map(Number);
  const brightness = (rgb[0]*299 + rgb[1]*587 + rgb[2]*114) / 1000;
  if (brightness < 128) {
    chatbotWindow.classList.add('dark-mode');
  }

  // Enter para enviar
  userInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
      sendMessage();
    }
  });
});
