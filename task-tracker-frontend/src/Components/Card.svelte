<script>
  import { createEventDispatcher } from "svelte";
  export let card, status;
  const dispatch = createEventDispatcher();
  const handleClick = () => dispatch("click", card);
</script>

<div class="card" draggable="true" on:click={handleClick}>
  <p class="title">{card.task_number}</p>
  {#if card.title}
    <p class="description">{card.title}</p>
  {/if}
</div>

<style>
  .card {
    background: white;
    padding: 0.6em;
    border-radius: 0.5em;
    box-shadow: 0 0.1em 0.3em rgba(0,0,0,.2);
    display: flex;
    flex-direction: column;
    cursor: grab;
  }
  .title {
    font-weight: bold;
    font-size: 1.3em;
    margin-bottom: 0.3em;
    overflow: hidden;
  }
  .description {
    font-size: 1em;
    color: #555;
    overflow-x: hidden;
    margin-right: 1em;
  }
</style>
