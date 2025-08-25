const API_URL = import.meta.env.VITE_API_URL;
const CARDS_ENDPOINT = import.meta.env.VITE_CARDS_ENDPOINT;

export async function getCards() {
  const res = await fetch(`${API_URL}${CARDS_ENDPOINT}`);
  if (!res.ok) throw new Error("Failed to fetch cards");
  const result = await res.json();
  return result.data; 
}

export async function createCard(cardData) {
  const res = await fetch(`${API_URL}${CARDS_ENDPOINT}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(cardData),
  });
  if (!res.ok) throw new Error("Failed to create card");
  return await res.json();
}

export async function updateCard(id, cardData) {
  const res = await fetch(`${API_URL}${CARDS_ENDPOINT}${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(cardData),
  });
  if (!res.ok) throw new Error("Failed to update card");
  return await res.json(); 
}

export async function deleteCard(id) {
  const res = await fetch(`${API_URL}${CARDS_ENDPOINT}${id}`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete card");
  return true;
}
