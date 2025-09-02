
const BASE_URL = import.meta.env.VITE_BASE_URL_API;
console.log(BASE_URL,"BASE_URL")


async function handleResponse(res) {
  if (!res.ok) {
    const errMsg = await res.text();
    throw new Error(errMsg || `Request failed with status ${res.status}`);
  }
  
  const text = await res.text();
  return text ? JSON.parse(text) : { success: true };
}


export async function getCards() {
  const res = await fetch(`${BASE_URL}/cards`);
  return handleResponse(res);
}


export async function createCard(card) {
  const res = await fetch(`${BASE_URL}/cards`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: card.title,
      description: card.description,
      status: card.status || "todo",
      added_by: card.added_by || "frontend",
    }),
  });
  return handleResponse(res);
}


export async function updateCard(id, card) {
  const res = await fetch(`${BASE_URL}/cards/${id}`, {
    method: "PUT", 
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: card.title,
      description: card.description,
      status: card.status,
      added_by: card.added_by || "frontend",
    }),
  });
  return handleResponse(res);
}


export async function deleteCard(id) {
  const res = await fetch(`${BASE_URL}/cards/${id}`, {
    method: "DELETE",
  });
  return handleResponse(res);
}
