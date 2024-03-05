<template>
  <div
    class="form-signin w-100 m-auto bg-danger-subtle mt-3 mb-3 rounded text-center"
  >
    <form @submit.prevent="processLogInUser" class="formulario">
      <img src="../assets/mahtea.png" height="150" width="200" />
      <h1 class="mb-3 fw-normal">Iniciar sesión</h1>

      <div class="form-floating">
        <input
          type="text"
          v-model="user.username"
          id="usuario"
          class="form-control"
          placeholder="Usuario"
          autocomplete="current-user"
          required
        />
        <label for="usuario">Usuario</label>
      </div>
      <div class="form-floating">
        <input
          v-model="user.password"
          type="password"
          class="form-control"
          id="password"
          placeholder="Contraseña"
          autocomplete="current-password"
          required
        />
        <label for="password">Contraseña</label>
      </div>
      <button class="btn btn-primary w-100 py-2" type="submit">Ingresar</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogIn",

  emits: ["completedLogIn"],

  data: function () {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    processLogInUser: function () {
      axios
        .post("http://127.0.0.1:8000/login/", this.user, { headers: {} })
        .then((result) => {
          let dataLogIn = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          this.$emit("completedLogIn", dataLogIn);
        })
        .catch((error) => {
          if (error.response.status === 401)
            alert("ERROR 401: Credenciales Incorrectas.");
          this.user.username = "";
          this.user.password = "";
        });
    },
  },
};
</script>

<style>
html,
body {
  height: 100%;
}

.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
