<script>
  import { createEventDispatcher } from "svelte";
  export let card;
  export let status;
  export let index;
  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("click", card);
  }

  function handleDragStart(e) {
    e.dataTransfer.setData("cardId", card.id);
    e.dataTransfer.setData("fromStatus", status);
    e.dataTransfer.setData("fromIndex", index);
  }
</script>

<div
  class="card"
  draggable="true"
  on:click={handleClick}
  on:dragstart={handleDragStart}
>
  <p class="title">{card.task_number}</p> 
  {#if card.title}
    <p class="description">{card.title}</p>
  {/if}
</div>

<style>
  .card {
    background: white;
    padding: 8px;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    cursor: grab;
  }
  .card .title {
    font-weight: bold;
    font-size: 1.3em;
    margin-bottom: 4px;
    overflow: hidden;
  }
  .card .description {
    font-size: 1em;
    color: #555;
    overflow-x: hidden;
    margin-right: 10px;
  }
</style>
