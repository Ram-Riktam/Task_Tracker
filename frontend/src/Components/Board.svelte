<script>
  import Header from "./Header.svelte";
  import List from "./List.svelte";
  import {
    getCards,
    createCard,
    updateCard,
    deleteCard as apiDeleteCard,
  } from "$lib/api.js";
  import { onMount } from "svelte";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  let board = {
    Todo: [],
    "In Progress": [],
    Completed: [],
    Deployed: [],
    Cancelled: [],
  };

  const colors = {
    Todo: "#1E90FF",
    "In Progress": "#FF8C00",
    Completed: "#28A745",
    Deployed: "#6F42C1",
    Cancelled: "rgb(185,12,12)",
  };

 
  async function refreshBoard() {
    const cards = await getCards();
    const newBoard = {
      Todo: [],
      "In Progress": [],
      Completed: [],
      Deployed: [],
      Cancelled: [],
    };
    for (const c of cards) {
      if (!newBoard[c.status]) newBoard[c.status] = [];
      newBoard[c.status].push(c);
    }
    board = newBoard;
  }

async function handleCardCreated(event) {
  const card = event.detail;


  board = {
    ...board,
    [card.status]: [...board[card.status], card],
  };

  try {
    const created = await createCard(card); 
    await refreshBoard(); 
  } catch (err) {
    console.error("Create failed", err);
    await refreshBoard(); 
  }
}



  
  async function handleEditCard(event) {
    const card = event.detail;
    const newTitle =  card.title;
    const newDescription =card.description;

    await updateCard(card.id, {
      title: newTitle,
      description: newDescription,
      status: card.status,
      added_by: "frontend",
    });

    await refreshBoard();
  }

 
  async function handleDeleteCard(event) {
    const card = event.detail;
      {
      await apiDeleteCard(card.id);
      await refreshBoard();
    }
  }

  
  onMount(refreshBoard);
</script>

<Header on:cardCreated={handleCardCreated} />

<div class="board">
  {#each Object.entries(board) as [status, cards]}
    <List
      {cards}
      {status}
      color={colors[status]}
      on:editCard={handleEditCard}
      on:deleteCard={handleDeleteCard}
    />
  {/each}
</div>

<style>
 .board {
  display: flex;
  gap: 1%;
  padding: 1%;
  min-height: 80vh;
}


@media (max-width: 768px) {
  .board {
    
    gap: 2%;           
    padding: 2%;
    flex-wrap: wrap;        
  }
}

</style>
