<script>
  import { createEventDispatcher } from "svelte";
  export let card;
  export let status;
  export let index;
  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("click", card);
  }
</script>

<div class="card" draggable="true" on:click={handleClick}>
  <p class="title">{card.Title}</p>
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
    margin-bottom: 4px;
    overflow: hidden;
  }
  .card .description {
    font-size: 0.9em;
    color: #555;
  }
</style>
