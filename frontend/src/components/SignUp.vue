<template>
  <div class="container pt-5 px-5 contenedor-general" style="max-width: 480px">
    <div class="card">
      <div class="card-header">
        <h2>Registro</h2>
      </div>
      <div class="card-body bg-danger-subtle">
        <form @submit.prevent="validarRegistro">
          <div class="form-group">
            <div class="form-group">
              <label for="name">Nombres:</label>
              <input
                type="text"
                class="form-control"
                v-model="user.name"
                required
              />
            </div>
            <div class="form-group">
              <label for="lastName">Apellidos:</label>
              <input
                type="text"
                class="form-control"
                v-model="user.lastname"
                required
              />
            </div>
            <div class="form-group">
              <label for="userName">Correo:</label>
              <input
                type="email"
                class="form-control"
                v-model="user.username"
                required
              />
            </div>
            <div class="form-group">
              <label for="password">Contraseña:</label>
              <input
                type="text"
                class="form-control"
                v-model="user.password"
                required
              />
            </div>
            <label for="phone">Teléfono:</label>
            <input
              type="number"
              class="form-control"
              v-model="user.phone"
              required
            />
          </div>
          <div class="form-group">
            <label for="birthday">Fecha de Nacimiento:</label>
            <input
              type="date"
              class="form-control"
              v-model="user.birthday"
              required
            />
          </div>
          <div class="form-group">
            <label for="adress">Dirección:</label>
            <input
              type="text"
              class="form-control"
              v-model="user.adress"
              required
            />
          </div>
          <div class="form-group">
            <label for="city">Ciudad:</label>
            <input
              type="text"
              class="form-control"
              v-model="user.city"
              required
            />
          </div>

          <!-- <div class="mb-3">
            <label class="form-label">Selecciona una opción:</label>
            <div class="form-check">
              <input
                type="radio"
                id="isclient"
                class="form-check-input"
                v-model="isclient"
                value="adquirir"
              />
              <label class="form-check-label" for="adquirirServicios"
                >Adquirir Servicios</label
              >
            </div>
            <div class="form-check">
              <input
                type="radio"
                id="isclient"
                class="form-check-input"
                v-model="isclient"
                value="ofrecer"
              />
              <label class="form-check-label" for="isclient"
                >Ofrecer Servicios</label
              >
            </div>
          </div> -->
          <div class="form-group"></div>
          <button type="submit" class="btn btn-primary">Guardar</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "NewPc",

  emits: ["loadHome", "processSignUp"],

  data() {
    return {
      user: {
        name: "",
        lastname: "",
        username: "",
        password: "",
        adress: "",
        city: "",
        birthday: "",
        phone: 0,
        // isclient: null,
      },
    };
  },
  methods: {

    processSignUp: function () {
      axios
        .post("http://127.0.0.1:8000/user/", this.user, { headers: {} })
        .then((result) => {
          let dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          this.$emit("completedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.log(error);
          alert("ERROR: Fallo en el registro.");
        });
    },

    validarRegistro() {
      // Expresión regular para validar el formato del correo electrónico
      const correoRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      // Validar la contraseña
      const passwordRegExp =
        /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;

      // Validar el formato del correo electrónico
      if (!correoRegExp.test(this.user.username)) {
        alert("Formato de correo incorrecto");
      }

      if (!passwordRegExp.test(this.user.password)) {
        alert(
          "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, un número y un carácter especial."
        );
      }

      // Asignar true o false a isclient según la opción seleccionada
      this.user.isclient = this.isclient === "adquirir" ? true : false;

      if (
        correoRegExp.test(this.user.username) &&
        passwordRegExp.test(this.user.password) &&
        this.aceptarTerminos
      ) {
        alert(
          "Registro Exitoso\nUsuario: " +
            this.user.username +
            "\nPassword: " +
            this.user.password
        );
      }
    },
  },
};
</script>

<style></style>
