<template>
  <div class="container pt-5 px-5" style="max-width: 480px">
    <div class="card">
      <div class="card-header">
        <h2>Registro</h2>
      </div>
      <div class="card-body bg-danger-subtle">
        <form @submit.prevent="validarRegistro">
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              id="name"
              v-model="user.form.name"
              placeholder="Nombre"
              required
            />
            <label for="name">Nombre</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              v-model="user.form.last_name"
              placeholder="Apellido"
              required
            />
            <label for="lastName">Apellido</label>
          </div>
          <div class="form-check mb-3">
            <input
              type="radio"
              id="male"
              class="form-check-input"
              v-model="user.form.gender"
              value="Masculino"
            />
            <label class="form-check-label" for="male">Masculino</label>
          </div>

          <div class="form-check mb-3">
            <input
              type="radio"
              id="female"
              class="form-check-input"
              v-model="user.form.gender"
              value="Femenino"
            />
            <label class="form-check-label" for="female">Femenino</label>
          </div>

          <div class="form-check mb-3">
            <input
              type="radio"
              id="other"
              class="form-check-input"
              v-model="user.form.gender"
              value="Otro"
            />
            <label class="form-check-label" for="other">Otro</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="email"
              class="form-control"
              v-model="user.email"
              placeholder="Correo"
              required
            />
            <label for="email">Correo</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              v-model="user.username"
              placeholder="Usuario"
              required
            />
            <label for="username">Usuario</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              v-model="user.password"
              placeholder="Contraseña"
              required
            />
            <label for="password">Contraseña</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="number"
              class="form-control"
              v-model="user.form.phone"
              placeholder="Celular"
              required
            />
            <label for="phone">Celular</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="date"
              class="form-control"
              v-model="user.form.birthdate"
              required
            />
            <label for="birthday">Fecha de Nacimiento</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              v-model="user.form.adress"
              placeholder="Dirección"
              required
            />
            <label for="adress">Dirección</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              v-model="user.form.city"
              placeholder="Ciudad"
              required
            />
            <label for="city">Ciudad</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              v-model="user.form.occupation"
              placeholder="Ocupación"
              required
            />
            <label for="city">Ocupación</label>
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
  name: "SignUp",

  emits: ["loadHome", "processSignUp", "completedSignUp"],

  data() {
    return {
      user: {
        username: "Leydifranco40",
        email: "leydi@gmail.com",
        password: "LeydiFranco40*",
        form: {
          name: "Leydi",
          last_name: "Franco",
          gender: "Femenino",
          adress: "Cra 66 41B 145",
          city: "Rionegro",
          birthdate: "1996-10-04",
          phone: 3103816279,
          occupation: "Empleado",
        },
      },
    };
  },
  methods: {
    processSignUp: function () {
      axios
        .post("http://127.0.0.1:8000/user/", this.user, { headers: {} })
        .then((result) => {
          console.log("Llego al rseultado del post");

          let dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          this.$emit("completedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.log("No Llego al resultado");

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
      if (!correoRegExp.test(this.user.email)) {
        alert("Formato de correo incorrecto");
      }

      if (!passwordRegExp.test(this.user.password)) {
        alert(
          "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, un número y un carácter especial."
        );
      }

      if (
        correoRegExp.test(this.user.email) &&
        passwordRegExp.test(this.user.password)
      ) {
        this.processSignUp();
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
