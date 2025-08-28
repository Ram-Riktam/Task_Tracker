<script>
  import { createEventDispatcher } from "svelte";
 
  import logo from "../Images/company_logo.png";

  import userlogin  from '../Images/user_login.png';
 
import  user_plus from '../Images/user-plus-solid-full.svg';
import newlogin from '../Images/newlogin.png'
  const dispatch = createEventDispatcher();
  let titleValue = "";
  let descValue = "";
  let loading = false;
  let errorMessage = "";
  let showModal = false;

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

     
      titleValue = "";
      descValue = "";
      showModal = false;
    } catch (err) {
      errorMessage = err.message || "Failed to create card";
    } finally {
      loading = false;
    }
  }
    let showModal1 = false;

  function toggleModal() {
    showModal1 = !showModal1;
  }

</script>

<header class="header">
  <div class="logo"><img src={logo} alt="Logo" /></div>
  <div class="actions">
    <button class="addcart" on:click={() => (showModal = true)}> + Add Card</button>
    <img src={userlogin} alt="Login" class="login_icon" on:click={toggleModal} />
   
  </div>
</header>

{#if showModal}
  <div class="modal-overlay" on:click={() => (showModal = false)}>
    <div class="modal" on:click|stopPropagation>
      <div class="cards">
        <div class="create-card">
          <h1>Create Card</h1>
          <button class="close-btn" on:click={() => (showModal = false)}>X</button>
        </div>
        <hr />
        <div class="card-data">
          <label class="title-label">Title</label>
          <input type="text" placeholder="Enter Title..." bind:value={titleValue} />
          <label class="description-label">Description</label>
          <textarea placeholder="Enter Description..." bind:value={descValue}></textarea>

          {#if errorMessage}
            <p style="color: red; margin-bottom: 10px;">{errorMessage}</p>
          {/if}

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
       <img src={newlogin} alt="Log in" class="loginimg"/>
     <span>Log in</span>
    </div>
   <div class="signup">
     <img src={user_plus} alt="sign up" class="signupimg"/>
    <span>Sign up</span>
   </div>
   
  </div>
{/if}

<style>
  .header {
    display: flex;
    /* justify-content: space-between; */
    align-items: center;
    /* padding: 12px 24px; */
    background: #0567a0;
    color: white;
    height: 10vh;
    width: 99vw;
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
  padding: 0.5vw 1vw;       
  border: none;
  border-radius: 0.5vw;
  cursor: pointer;
  font-weight: bold;
  font-size: 1vw;            
  width: auto;               
  min-width: 8vw;            
  height: 3vw;               
}


.login_icon {
  height: 2vw;               
  width: 2vw;
  border-radius: 50%;
  filter: invert(94%) sepia(96%) saturate(5500%) hue-rotate(2deg) brightness(100%) contrast(102%);
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
  .logo img{
    height: 8vw;
    width: 21vw;
  }
}




.modal1 {
  position: absolute;
  top: 7vw;                
  left: auto;              
  right: 0;
  background: white;
  border: 0.1vw solid #ccc;
  padding: 1vw 1.5vw;      
  box-shadow: 0 0.4vw 0.8vw rgba(0,0,0,0.2);
  border-radius: 0.8vw;
  display: flex;
  flex-direction: column;
  gap: 1vw;
  z-index: 100;
  margin-right: 2vw;
  font-size: 1vw;
}


.modal1 button {
  padding: 0.8vw 1.6vw;
  border: none;
  border-radius: 0.5vw;
  color: black;
  cursor: pointer;
  font-size: 1vw;
}


.loginimg, .signupimg {
  height: 1.5vw;
  width: 1.5vw;
}


.login {
  display: flex;

  gap: 1vw;
 
}
.login span{
  margin-top: 0.3vw;
}
.signup span{
  margin-top: 0.3vw;
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
  .description-label {
    font-size: 25px;
  }
  .title-label {
    font-size: 30px;
  }
  .modal textarea {
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
    width: 110px;
    font-size: 20px;
  }
  .save-btn[disabled] {
    opacity: 0.6;
    cursor: not-allowed;
  }
  .create-card {
    display: flex;
    justify-content: space-between;
    padding: 5px;
    margin-left: 26px;
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
    transition:
      background 0.2s ease,
      color 0.2s ease;
  }
  .close-btn:hover {
    background: #f56c6c;
    color: white;
  }
  .cards {
    border: 1px solid lightblue;
    border-radius: 10px;
    box-shadow: 2px 2px 8px rgba(2, 51, 80, 0.5);
  }
</style>
