<template>
  <div>

    <!-- MODAL NEW USER -->

    <div v-show="state.openUserModal" class="modal">
      <div 
        class="modal-background"
        @click="state.openUserModal = false"
      ></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Jogador</p>
          <button 
            class="delete" 
            aria-label="close"
            @click="state.openUserModal = false"
          ></button>
        </header>
        <section class="modal-card-body">

          <div class="field">
            <label class="label">Nome</label>
            <div class="control">
              <input v-model="playerData.name" class="input" type="text" placeholder="Ex: Neymar">
            </div>
          </div>

          <div class="field">
            <label class="label">Avaliação</label>
            <div class="control">
              <input v-model="playerData.rating" class="input" type="number" placeholder="Ex: 0.0  a 5.0">
            </div>
          </div>

          <div class="field">
            <label class="label">Camisa</label>
            <div class="control">
              <input v-model="playerData.shirt" class="input" type="number" placeholder="Ex: 10">
            </div>
          </div>

          <div class="field">
            <label class="label">Time</label>
            <div class="control">
              <input v-model="playerData.team" class="input" type="text" placeholder="Ex: Paris Saint-Germain">
            </div>
          </div>

          <div class="field">
            <label class="label">Nacionalidade</label>
            <div class="control">
              <input v-model="playerData.nacionality" class="input" type="text" placeholder="Ex: Brasileira">
            </div>
          </div>

          <div class="field">
            <label class="label">Gols</label>
            <div class="control">
              <input v-model="playerData.goals" class="input" type="number" placeholder="Ex: 496">
            </div>
          </div>

          <div class="field">
            <label class="label">Posição</label>
            <div class="control">
              <input v-model="playerData.position" class="input" type="text" placeholder="Ex: Atacante">
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button @click="postPlayer(), afterPost()" class="button is-success">
            Salvar
          </button>
          <button 
            class="button is-danger"
            @click="state.openUserModal = false">
            Cancelar
          </button>
        </footer>
      </div>
    </div>

    <!-- MODAL EDIT USER -->

    <div v-show="state.openEditModal" class="modal">
      <div 
        class="modal-background"
        @click="state.openEditModal = false"
      ></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Jogador</p>
          <button 
            class="delete" 
            aria-label="close"
            @click="state.openEditModal = false"
          ></button>
        </header>
        <section class="modal-card-body">

          <div class="field">
            <label class="label">Nome</label>
            <div class="control">
              <input v-model="playerData.name" class="input" type="text" placeholder="Ex: Neymar">
            </div>
          </div>

          <div class="field">
            <label class="label">Avaliação</label>
            <div class="control">
              <input v-model="playerData.rating" class="input" type="number" placeholder="Ex: 0.0  a 5.0">
            </div>
          </div>

          <div class="field">
            <label class="label">Camisa</label>
            <div class="control">
              <input v-model="playerData.shirt" class="input" type="number" placeholder="Ex: 10">
            </div>
          </div>

          <div class="field">
            <label class="label">Time</label>
            <div class="control">
              <input v-model="playerData.team" class="input" type="text" placeholder="Ex: Paris Saint-Germain">
            </div>
          </div>

          <div class="field">
            <label class="label">Nacionalidade</label>
            <div class="control">
              <input v-model="playerData.nacionality" class="input" type="text" placeholder="Ex: Brasileira">
            </div>
          </div>

          <div class="field">
            <label class="label">Gols</label>
            <div class="control">
              <input v-model="playerData.goals" class="input" type="number" placeholder="Ex: 496">
            </div>
          </div>

          <div class="field">
            <label class="label">Posição</label>
            <div class="control">
              <input v-model="playerData.position" class="input" type="text" placeholder="Ex: Atacante">
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button @click="putPlayer(), afterPost()" class="button is-success">
            Salvar
          </button>
          <button 
            class="button is-danger"
            @click="state.openEditModal = false">
            Cancelar
          </button>
        </footer>
      </div>
    </div>

    <section class="hero is-link">
      <div class="hero-body">
        <p class="title is-flex is-justify-content-space-between">
          CRUD Jogadores
          <button 
            class="button is-success"
            @click="state.openUserModal = true"
          >Cadastrar novo</button>
        </p>
        <p class="subtitle">
          HCosta
        </p>
      </div>
    </section>
    <div class="table-container is-flex is-justify-content-center">
      <table class="table is-bordered is-striped is-hoverable is-align-self-flex-start">
        <thead>
          <tr>
            <th>Nome</th>
            <th>Posição</th>
            <th>Camisa</th>
            <th>Time</th>
            <th>Gols</th>
            <th>Nacionalidade</th>
            <th>Avaliação</th>
            <th>Opções</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="player in state.playerList" :key="player.id">
            <td>{{ player.name }}</td>
            <td>{{ player.position }}</td>
            <td>{{ player.shirt }}</td>
            <td>{{ player.team }}</td>
            <td>{{ player.goals }}</td>
            <td>{{ player.nacionality }}</td>
            <td>{{ player.rating }}</td>
            <td>
              <i 
                class="fa-solid fa-pen is-clickable edit-item"
                @click="getPlayer(player.player_id), state.openEditModal = true"
              ></i>
              <div v-show="state.openDeleteModal" class="modal">
                <div
                class="modal-background"
                @click="state.openDeleteModal = false"
                ></div>
                <div class="modal-card">
                  <header class="modal-card-head"> 
                    <p class="modal-card-title">Você tem certeza que deseja excluir?</p>
                  </header>
                  <section class="modal-card-body">
                      <div class="field">
                        <button
                            class="button is-danger"
                            @click="deletePlayer(player.player_id), afterPost()"
                            >Excluir
                        </button>
                    </div>
                      <div class="field">
                        <button
                          class="button is-dark"
                          @click="state.openDeleteModal = false"
                          >Cancelar
                        </button>
                      </div>
                  </section>
                </div>
              </div>
              <i 
                  class="fa-solid fa-trash-can ml-4 is-clickable delete-item"
                 @click="state.openDeleteModal = true"
                ></i>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { reactive, onBeforeMount } from 'vue';

onBeforeMount(() => {
  getPlayers()
});

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000'
});

const state = reactive({
  playerList: [],
  selectedPlayer: undefined,
  openUserModal: false,
  openDeleteModal: false,
  openEditModal: false,
});

const playerData = reactive({
  name: '',
  rating: '',
  shirt: '',
  position: '',
  team: '',
  nacionality: '',
  goals: ''
})

const afterPost = () => {
  state.openUserModal = false
  window.location.reload()
}

const getPlayers = () => {
  api.get('/players/')
  .then(res => {
    state.playerList = res.data.players
  })
  .catch(err => console.log(err))
};

const getPlayer = (player_id) => {
  state.selectedPlayer = player_id
  api.get(`/players/${player_id}`)
  .then(res => {
    const player = res.data

    playerData.name = player.name
    playerData.rating = player.rating
    playerData.shirt = player.shirt
    playerData.position = player.position
    playerData.team = player.team
    playerData.nacionality = player.nacionality
    playerData.goals = player.goals
  })
}

const postPlayer = () => {
  const playerId = Math.round(Math.random() * 100000000)
  api.post(`/players/${playerId}`, {
    name: playerData.name,
    rating: playerData.rating,
    shirt: playerData.shirt,
    position: playerData.position,
    team: playerData.team,
    nacionality: playerData.nacionality,
    goals: playerData.goals
  })
  .then(function(res) {
    console.log(res)
  })
}

const putPlayer = (player_id) => {
  state.selectedPlayer = player_id
  api.put(`/players/${player_id}`, {
    name: playerData.name,
    rating: playerData.rating,
    shirt: playerData.shirt,
    position: playerData.position,
    team: playerData.team,
    nacionality: playerData.nacionality,
    goals: playerData.goals
  })
}

const deletePlayer = (player_id) => {
  state.selectedPlayer = player_id
  api.delete(`/players/${player_id}`)
  window.location.reload()
}

</script>

<style scoped>

.modal {
  display: block;
  display: flex;
}
.table-container {
  width: 100vw;
  height: 100vh;
  margin-top: 60px;
}

.edit-item {
  transition: .2s;
}

.edit-item:hover {
  color: #485fc7;
}

.delete-item {
  transition: .2s;
}

.delete-item:hover {
  color: #f14668;
}

.field {
  margin-bottom: 2em;
}

</style>
