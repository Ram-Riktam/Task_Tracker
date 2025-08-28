<script>
  import { createEventDispatcher } from "svelte";
  import { fade, slide } from "svelte/transition";
  import Delete_icon from "../Images/delete_icon.jpg";
  import Card from "./Card.svelte";

  export let status;
  export let color = "#ccc";
  export let cards = []; 
  export let boardStatuses = ["Todo", "In Progress", "Completed", "Deployed", "Cancelled"];

  let expanded = false;
  let open = false;

  const dispatch = createEventDispatcher();

  let showCardModal = false;
  let showDeleteConfirm = false;
  let selectedCard = null;
  let editing = false;
  let selectedStatus = status;

  function toggleExpand() {
    expanded = !expanded;
  }

  function openCardModal(card) {
    selectedCard = { ...card };
    selectedStatus = card.status;
    editing = false;
    expanded = false;
    showCardModal = true;
  }

  function startEditing() {
    editing = true;
  }

 
  function saveCardEdit() {
    dispatch("editCard", { ...selectedCard, status: selectedStatus });
    showCardModal = false;
  }

  function confirmDelete() {
    showDeleteConfirm = true;
    showCardModal = false;
  }

  function deleteCard() {
    dispatch("deleteCard", selectedCard);
    showDeleteConfirm = false;
  }

  function selectStatus(s) {
    selectedStatus = s;
    open = false;
  }
</script>

<div class="list">
  <h3 class="partition" style="background:{color}">{status}</h3>

  {#each cards as card (card.id)}
    <Card {card} {status} on:click={() => openCardModal(card)} />
  {/each}
</div>

{#if showCardModal}
  <div class="modal-overlay" on:click={() => (showCardModal = false)}>
    <div class="modal" on:click|stopPropagation>
      {#if !editing}
        <div class="title-card">
          <div class="cancel-border">
            <h3 class="status">
              <strong>Status:</strong>
              <span
                class="status-value pill {selectedStatus.toLowerCase().replace(' ', '-')}">
                {selectedStatus}
              </span>
            </h3>

            <div class="btn-border">
              <button class="close-btn" on:click={() => (showCardModal = false)}>X</button>
            </div>
          </div>

          <div class="modal-header1">
            <h3>Title: {selectedCard.title}</h3>
            <div class="description-box">
              {#if expanded}
                {selectedCard.description}
                <span class="read-more" on:click={toggleExpand}>Read less</span>
              {:else}
                {selectedCard.description && selectedCard.description.length > 550
                  ? selectedCard.description.slice(0, 550) + "..."
                  : selectedCard.description}
                {#if selectedCard.description && selectedCard.description.length > 150}
                  <span class="read-more" on:click={toggleExpand}>Read more</span>
                {/if}
              {/if}
            </div>
          </div>

          <div class="modal-actions">
            <button class="edit-btn" on:click={startEditing}>Edit</button>
            <button class="delete-btn" on:click={confirmDelete}>Delete</button>
          </div>
        </div>
      {:else}
        <div class="modal-header">
          <h3>Edit Card</h3>
          <div class="btn-border">
            <button class="close-btn" on:click={() => (showCardModal = false)}>X</button>
          </div>
        </div>
        <div class="edit-modal">
          <label>Title:</label>
          <input type="text" bind:value={selectedCard.title} />

          <label>Description:</label>
          <textarea bind:value={selectedCard.description}></textarea>

          <label>Status:</label>
          <div class="status-dropdown">
            <div class="selected-wrapper" on:click={() => (open = !open)}>
              <div class="pill {selectedStatus.toLowerCase().replace(' ', '-')}">
                {selectedStatus}
              </div>
              <span class="arrow">{open ? "▲" : "▼"}</span>
            </div>

            {#if open}
              <ul
                class="options"
                in:slide={{ duration: 200 }}
                out:fade={{ duration: 150 }}>
                {#each boardStatuses as s}
                  <li class="option" on:click={() => selectStatus(s)}>
                    <div class="pill {s.toLowerCase().replace(' ', '-')}">{s}</div>
                  </li>
                {/each}
              </ul>
            {/if}
          </div>

          <div class="modal-actions">
            <button class="save-btn" on:click={saveCardEdit}>Save</button>
            <button class="cancel-btn" on:click={() => (showCardModal = false)}>Cancel</button>
          </div>
        </div>
      {/if}
    </div>
  </div>
{/if}

{#if showDeleteConfirm}
  <div class="modal-overlay" on:click={() => (showDeleteConfirm = false)}>
    <div class="modal" on:click|stopPropagation>
      <img class="delete-icon" src={Delete_icon} alt="Delete_icon" />
      <p class="delete-text">
        This action will permanently delete the card. Do you want to continue?
      </p>
      <div class="modal-actions">
        <button on:click={() => (showDeleteConfirm = false)} class="cancel-btn">Cancel</button>
        <button class="delete-btn" on:click={deleteCard}>OK</button>
      </div>
    </div>
  </div>
{/if}

<style>
  .list {
  background: #e0e0e0;
  padding: 12px;
  border-radius: 8px;
  width: 18%;
  display: flex;
  flex-direction: column;
  gap: 8px;
  Max-height: 600px;
  overflow-y: auto;
  margin-bottom: 2%;
  /* align-items: center; */
}


@media (max-width: 1024px) {
  .list {
    min-width: 15%;
    height: auto;
  }
}


@media (max-width: 600px) {
  .list {
    min-width: 100%;
    flex-direction: column;  
    height: auto;
  }
}

  .partition {
    text-align: center;
    font-weight: bold;
    color: white;
    padding: 8px;
    border-radius: 6px;
  }

  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .modal {
    position: relative;
    background: white;
    padding: 20px;
    border-radius: 10px;
    min-width: 350px;
    max-width: 800px;
    max-height: 700px;
    overflow-y: auto;
    margin-left: 35%;
  }

  .close-btn {
    padding: 7px;
    font-size: 18px;
    line-height: 1;
    background: transparent;
    color: #f56c6c;
    border: 2px solid #f56c6c;
    border-radius: 60%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition:
      background 0.2s ease,
      color 0.2s ease;
    font-weight: bolder;
  }

  .close-btn:hover {
    background: #f56c6c;
    color: white;
  }
  .btn-border {
    height: 30px;
    width: 30px;
    text-align: right;
  }
  .cancel-border {
    display: flex;
    justify-content: space-between;
  }

  .title-card {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .status {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .status-value {
    margin-left: 6px;
  }

  .modal-header1 h3 {
    margin: 0;
    font-size: 1.2rem;
  }

  .description-box {
    margin: 8px 0;
    line-height: 1.5;
    height: 11em;
    max-height: 11em;
    overflow-y: auto;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 6px;
    background: #f9f9f9;
    white-space: pre-wrap;
    word-wrap: break-word;
    font-size: 18px;
  }

  .description-box::-webkit-scrollbar {
    width: 6px;
  }
  .description-box::-webkit-scrollbar-thumb {
    background: #bbb;
    border-radius: 4px;
  }

  .read-more {
    color: #0567a0;
    font-size: 0.9rem;
    margin-left: 6px;
    cursor: pointer;
    text-decoration: underline;
  }

  .modal-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 12px;
  }

  .edit-btn {
    background: #0567a0;
    color: white;
    border: none;
    padding: 10px 25px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 17px;
    font-weight: 800;
  }

  .delete-btn {
    background: #e74c3c;
    color: white;
    border: none;
    padding: 10px 25px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 17px;
    font-weight: 800;
  }

  .edit-modal {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 16px;
    border: 1px solid lightblue;
    border-radius: 8px;
    background: #fdfdfd;
    box-shadow: 2px 2px 8px rgba(2, 51, 80, 0.5);
    width: 600px;
    height: 550px;
    margin: 0 auto;
    font-size: 20px;
  }
  .modal-header {
    display: flex;
    justify-content: space-between;
  }

  .edit-modal input,
  .edit-modal textarea {
    width: 97%;

    border: 1px solid #ccc;
    border-radius: 6px;
  }

  .edit-modal input {
    font-size: 25px;
    height: 55px;
  }
  .edit-modal textarea {
    resize: vertical;
    min-height: 130px;
    max-height: 500px;
    font-size: 16px;
  }

  .save-btn {
    background: #0567a0;
    color: white;
    border: none;
    padding: 12px 18px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
  }
  .save-btn:hover {
    background: #04507d;
  }

  .cancel-btn {
    background: #ccc;
    color: #050505;
    border: none;
    padding: 12px 18px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
  }
  .cancel-btn:hover {
    background: #a19f9f;
  }

  .status-dropdown {
    position: relative;
    display: flex;
    flex-direction: column;
    cursor: pointer;
  }

  .selected-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid #ccc;
    border-radius: 6px;
    padding: 10px;
    background: #fff;
  }

  .arrow {
    font-size: 14px;
    color: #555;
    margin-left: 8px;
  }

  .options {
    position: absolute;
    top: 100%;
    left: 0;
    list-style: none;
    margin: 6px 0 0;
    padding: 6px 0;
    border: 1px solid #ccc;
    background: #fff;
    border-radius: 6px;
    z-index: 10;
    width: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .option {
    display: flex;
    align-items: center;
    padding: 5px 10px;
    width: 100%;
    cursor: pointer;
  }
  .option:hover {
    background: #f5f5f5;
  }

  .pill {
    border-radius: 9999px;
    padding: 3px 10px;
    font-size: 17px;
    font-weight: 500;
    color: #fff;
    width: fit-content;
  }

  .todo {
    background: #1e90ff;
  }
  .in-progress {
    background: #ff8c00;
  }
  .completed {
    background: #28a745;
  }
  .deployed {
    background: #6f42c1;
  }
  .cancelled{
    background: rgb(185, 12, 12);
  }
  .delete-text {
    font-size: 20px;
    font-weight: bold;
  }
  .delete-icon {
    height: 100px;
    width: 100px;
    margin-left: 250px;
  }
</style>
