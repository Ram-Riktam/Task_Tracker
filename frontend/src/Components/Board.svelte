<script>
  import {
      deleteCard as apiDeleteCard,
      updateCard as apiUpdateCard,
      createCard,
      getCards,
  } from "$lib/api.js";
  import { onMount } from "svelte";
  import Header from "./Header.svelte";
  import List from "./List.svelte";

  let board = {
    Todo: [],
    "In Progress": [],
    Completed: [],
    Deploy: [],
  };

  let newListName = "";

  const colors = {
    Todo: "#1E90FF",
    "In Progress": "#FF8C00",
    Completed: "#28A745",
    Deploy: "#6F42C1",
  };

  async function refreshBoard() {
    const cards = await getCards();
    let newBoard = { Todo: [], "In Progress": [], Completed: [], Deploy: [] };

    for (const c of cards) {
      if (!newBoard[c.status]) newBoard[c.status] = [];
      newBoard[c.status].push(c);
    }
    board = newBoard;
  }

  onMount(refreshBoard);

  async function addCard(event) {
    const { status, title, description } = event.detail;
    await createCard({
      Title: title,
      Description: description,
      status,
      added_by: "frontend",
    });
    await refreshBoard();
  }

  async function handleUpdateCard(event) {
    const { id, newTitle, newDescription, newStatus } = event.detail;
    await apiUpdateCard(id, {
      Title: newTitle,
      Description: newDescription,
      status: newStatus,
      added_by: "frontend",
    });
    await refreshBoard();
  }

  async function deleteCard(event) {
    const { id } = event.detail;
    await apiDeleteCard(id);
    await refreshBoard();
  }

  function addList() {
    if (!newListName.trim()) return;
    if (!board[newListName]) {
      board = { ...board, [newListName]: [] };
    }
    newListName = "";
  }
</script>

<Header on:addCard={addCard} />

<div class="add-list">
  <input type="text" placeholder="New List Name" bind:value={newListName} />
  <button on:click={addList}>Add List</button>
</div>

<div class="board">
  {#each Object.entries(board) as [status, cards]}
    <List
      {status}
      {cards}
      color={colors[status]}
      on:updateCard={handleUpdateCard}
      on:deleteCard={deleteCard}
    />
  {/each}
</div>

<style>
  .board {
    display: flex;
    gap: 20px;
    padding: 20px;
    min-height: 80vh;
    max-height: 120vh;
    min-width: 1340px;
    max-width: 2000px;
    background: #f6f4f4;
  }
  .add-list {
    display: flex;
    gap: 8px;
    margin: 12px 20px;
  }
  .add-list input {
    padding: 6px 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  .add-list button {
    padding: 6px 12px;
    background: #0567a0;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
</style>
