<script>
  import { createEventDispatcher } from "svelte";
  import logo from "../assets/company_logo.png";
  import userlogin from "../assets/user_login.png";
  import user_plus from "../assets/user-plus-solid-full.svg";
  import newlogin from "../assets/newlogin.png";

  const dispatch = createEventDispatcher();
  let titleValue = "",
    descValue = "",
    loading = false,
    errorMessage = "",
    showModal = false,
    showModal1 = false;

  function toggleModal() {
    showModal1 = !showModal1;
  }

  async function saveCard() {
    if (!titleValue.trim()) return;
    loading = true;
    errorMessage = "";
    try {
      dispatch("cardCreated", {
        title: titleValue,
        description: descValue,
        status: "Todo",
        added_by: "frontend",
      });
      titleValue = descValue = "";
      showModal = false;
    } catch (err) {
      errorMessage = err.message || "Failed to create card";
    } finally {
      loading = false;
    }
  }
</script>

<header class="header">
  <div class="logo"><img src={logo} alt="Logo" /></div>
  <div class="actions">
    <button class="addcart" on:click={() => (showModal = true)}
      >+ Add Card</button
    >
    <img
      src={userlogin}
      alt="Login"
      class="login_icon"
      on:click={toggleModal}
    />
  </div>
</header>

{#if showModal}
  <div class="modal-overlay" on:click={() => (showModal = false)}>
    <div class="modal" on:click|stopPropagation>
      <div class="cards">
        <div class="create-card">
          <h1>Create Card</h1>
          <button class="close-btn" on:click={() => (showModal = false)}
            >X</button
          >
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
          {#if errorMessage}<p class="error">{errorMessage}</p>{/if}
          <div class="modal-actions">
            <button class="save-btn" on:click={saveCard} disabled={loading}>
              {loading ? "Saving..." : "Save"}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}

{#if showModal1}
  <div class="modal1">
    <div class="login">
      <img src={newlogin} alt="Log in" class="icon" /><span>Log in</span>
    </div>
    <div class="signup">
      <img src={user_plus} alt="Sign up" class="icon" /><span>Sign up</span>
    </div>
  </div>
{/if}

<style>
  .header {
    display: flex;
    align-items: center;
    background: #0567a0;
    color: white;
    height: 10vh;
    width: 100vw;
    overflow: hidden;
  }
  .logo img {
    height: 7vh;
    width: 11vw;
    border-radius: 25%;
    margin: 20%;
  }
  .actions {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 1vw;
    padding: 0.5vw 2vw;
    margin-left: auto;
  }
  .addcart {
    background: rgb(194, 64, 17);
    color: white;
    font-weight: bold;
    cursor: pointer;
    padding: 0.5vw 1vw;
    border: none;
    border-radius: 0.5vw;
    font-size: 1vw;
    min-width: 8vw;
    height: 3vw;
  }
  .login_icon {
    height: 2vw;
    width: 2vw;
    border-radius: 50%;
    filter: invert(94%) sepia(96%) saturate(5500%) hue-rotate(2deg)
      brightness(100%) contrast(102%);
    cursor: pointer;
  }

  @media (max-width: 1024px) {
    .actions {
      gap: 2vw;
      padding: 0.5vw 1vw;
    }
    .addcart {
      font-size: 1.2vw;
      min-width: 10vw;
      height: 3.5vw;
      padding: 0.5vw 1.2vw;
    }
    .login_icon {
      height: 3vw;
      width: 3vw;
    }
  }
  @media (max-width: 768px) {
    .actions {
      gap: 3vw;
      padding: 1vw 1.5vw;
    }
    .addcart {
      font-size: 4vw;
      min-width: 17vw;
      height: 8vw;
      padding: 1vw 2vw;
    }
    .login_icon {
      height: 6.5vw;
      width: 6.5vw;
    }
    .logo img {
      height: 8vw;
      width: 21vw;
    }
  }

  .modal1 {
    position: absolute;
    top: 7vw;
    right: 0;
    margin-right: 2vw;
    background: white;
    border: 0.1vw solid #ccc;
    border-radius: 0.8vw;
    padding: 1vw 1.5vw;
    box-shadow: 0 0.4vw 0.8vw rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    gap: 1vw;
    z-index: 100;
    font-size: 1vw;
  }
  .modal1 .login,
  .modal1 .signup {
    display: flex;
    gap: 1vw;
  }
  .modal1 span {
    margin-top: 0.3vw;
  }
  .icon {
    height: 1.5vw;
    width: 1.5vw;
  }

  .modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 200;
  }
  .modal {
    background: white;
    padding: 2vw;
    border-radius: 1vw;
    min-width: 50vw;
    max-width: 60vw;
    min-height: 60vh;
    max-height: 70vh;
    text-align: center;
  }
  .modal input,
  .modal textarea {
    width: 90%;
    padding: 0.8vw;
    margin-bottom: 1.5vh;
    border-radius: 0.5vw;
    border: 0.1vw solid #303b52;
  }
  .modal input {
    height: 6vh;
    font-size: 2vh;
  }
  .modal textarea {
    height: 12vh;
    font-size: 2vh;
  }
  .modal label {
    display: block;
    text-align: left;
    margin: 1vh 0 1vh 2vw;
    font-weight: bold;
  }
  .title-label {
    font-size: 2vw;
  }
  .description-label {
    font-size: 1.5vw;
  }
  .modal-actions {
    display: flex;
    justify-content: flex-end;
    margin: 2vh 2vw;
  }
  .save-btn {
    background: #0567a0;
    color: white;
    border: none;
    border-radius: 0.5vw;
    cursor: pointer;
    height: 6vh;
    width: 10vw;
    font-size: 1.2vw;
  }
  .save-btn[disabled] {
    opacity: 0.6;
    cursor: not-allowed;
  }
  .create-card {
    display: flex;
    justify-content: space-between;
    padding: 0.5vw;
    margin-left: 2vw;
  }
  .close-btn {
    height: 2.5vh;
    width: 2.5vh;
    font-size: 1vw;
    line-height: 1;
    background: transparent;
    color: #f56c6c;
    border: 0.2vw solid #f56c6c;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
  }
  .close-btn:hover {
    background: #f56c6c;
    color: white;
  }
  .cards {
    border: 0.1vw solid lightblue;
    border-radius: 1vw;
    box-shadow: 0.2vw 0.2vw 0.8vw rgba(2, 51, 80, 0.5);
  }
  .error {
    color: red;
    margin-bottom: 1vh;
  }
</style>
