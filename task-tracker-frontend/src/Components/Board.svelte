<script>
  import Header from "./Header.svelte";
  import List from "./List.svelte";
  import {
    getCards,
    createCard,
    updateCard,
    deleteCard as apiDeleteCard,
  } from "../lib/api.js";
  import { onMount } from "svelte";

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

  const refreshBoard = async () => {
    board = {
      Todo: [],
      "In Progress": [],
      Completed: [],
      Deployed: [],
      Cancelled: [],
    };
    (await getCards()).forEach((c) => (board[c.status] ??= []).push(c));
  };

  const handleCardCreated = async (e) => {
    const card = e.detail;
    board = { ...board, [card.status]: [...board[card.status], card] };
    try {
      await createCard(card);
    } catch (err) {
      console.error("Create failed", err);
    }
    await refreshBoard();
  };

  const handleEditCard = async ({ detail }) => {
    const { id, title, description, status } = detail;
    await updateCard(id, { title, description, status, added_by: "frontend" });
    await refreshBoard();
  };

  const handleDeleteCard = async ({ detail }) => {
    await apiDeleteCard(detail.id);
    await refreshBoard();
  };

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
    overflow-x: hidden;
  }
  @media (max-width: 48rem) {
    .board {
      gap: 2%;
      padding: 2%;
      flex-wrap: wrap;
    }
  }
</style>
