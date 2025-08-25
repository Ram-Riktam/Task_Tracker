<script>
  import { createEventDispatcher } from "svelte";
  import loginIcon from "../Images/Login.jpg";
  import logo from "../Images/Logo.jpg";
  import signupIcon from "../Images/signup.jpg";

  const dispatch = createEventDispatcher();
  let showModal = false;
  let titleValue = "";
  let descValue = "";

  function saveCard() {
    if (!titleValue.trim()) return;

    // Always add new cards to "Todo"
    dispatch("addCard", {
      status: "Todo",
      title: titleValue,
      description: descValue,
    });

    titleValue = "";
    descValue = "";
    showModal = false;
  }
</script>

<header class="header">
  <div class="logo"><img src={logo} alt="Logo" /></div>
  <div class="actions">
    <button class="addcart" on:click={() => (showModal = true)}>Add Card</button
    >
    <img src={loginIcon} alt="Login" class="icon1" />
    <img src={signupIcon} alt="Signup" class="icon2" />
  </div>
</header>

{#if showModal}
  <div class="modal-overlay" on:click={() => (showModal = false)}>
    <div class="modal" on:click|stopPropagation>
      <div class="cards">
      <div class="create-card">
        <h1>Create Card</h1>
         <button class="close-btn" on:click={()=>(showModal=false)}>X</button>
      </div>
      <hr />
      <div class="card-data">
        <label class="title-label">Title</label>
        <input
          type="text"
          placeholder="Enter Title..."
          bind:value={titleValue}
        />
        <label class="description-label">Description</label>
        <textarea placeholder="Enter Description..." bind:value={descValue}
        ></textarea>
        <div class="modal-actions">
          <button class="save-btn" on:click={saveCard}>Save</button>
        </div>
      </div>
      </div>

    </div>
  </div>
{/if}

<style>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 24px;
    background: #0567a0;
    color: white;
  }
  .logo img {
    height: 60px;
    width: 80px;
    border-radius: 50%;
  }
  .actions {
    display: flex;
    gap: 16px;
    align-items: center;
  }
  .addcart {
    background: black;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
  }

  .icon2 {
    height: 30px;
    width: 80px;
    border-radius: 50%;
    cursor: pointer;
  }
  .icon1 {
    height: 70px;
    width: 90px;
    border-radius: 50%;
    cursor: pointer;
  }
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 200;
    /* height: 50px;
    width: 100px; */
  }
  .modal {
    background: white;
    padding: 24px;
    border-radius: 10px;
    min-width: 570px;
    max-width: 650px;
    text-align: center;
    min-height: 500px;
    max-height: 600px;
   
  }
  .modal textarea,
  .modal input {
    width: 100%;
    padding: 8px;
    margin-bottom: 16px;
    border-radius: 6px;
    border: 1px solid #303b52;
  }
  .modal input {
    height: 48px;
    width: 490px;
    font-size: 30px;
  }
  .modal textarea {
    height: 100px;
    width: 490px;
  }
  .modal label {
    padding: 10px;
    display: block;
    text-align: left;
    margin-bottom: 4px;
    font-weight: bold;
    margin-left: 20px;
  }
  .description-label{
    font-size: 25px;
  }
  .title-label{
    font-size: 30px;
  }
  .modal textarea{
    font-size: 20px;
  }
  .modal-actions {
    display: flex;
    justify-content: flex-end;
    margin-right: 30px;
    margin-bottom: 20px;
   
  }
  .save-btn {
    background: #0567a0;
    color: white;
    border-radius: 6px;
    border: none;
    cursor: pointer;
    height: 45px;
    width: 90px;
    font-size: 20px;
    
  }
  .create-card{
    display: flex;
    justify-content: space-between;
    padding: 5px;
    margin-left: 26px;
  }
  .close-btn{
    height: 30px;
    width: 30px;
    color: #f56c6c;
    border: 5px solid  #f56c6c;
    border-radius: 50%;
    margin-top: 10px;
    margin-right: 10px;
    font-weight: bold;

    
  }
 
 
  .cards{
    border: 1px solid lightblue;
    border-radius: 10px;
    box-shadow: 2px 2px 8px rgba(2, 51, 80, 0.5);

  }
  .close-btn {
  height: 30px;
  width: 30px;
  padding: 10px;              
  font-size: 16px;
  line-height: 1;
  background: transparent;    
  color: #f56c6c;
  border: 2px solid #f56c6c;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s ease, color 0.2s ease;
}

.close-btn:hover {
  background: #f56c6c;
  color: white;
}
</style>
