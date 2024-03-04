<template>
  <div id="app" class="app">
    <header>
      <nav
        class="navbar navbar-dark bg-info"
        aria-label="Dark offcanvas navbar"
      >
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
            <img src="./assets/logoMahtea.png" alt="LogoLetra" id="" />
            <img width="50" src="./assets/logoGato.png" alt="LogoGato" />
          </a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="offcanvas"
            data-bs-target="#offcanvasNavbarDark"
            aria-controls="offcanvasNavbarDark"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div
            class="offcanvas offcanvas-end text-bg-info"
            tabindex="-1"
            id="offcanvasNavbarDark"
            aria-labelledby="offcanvasNavbarDarkLabel"
          >
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="offcanvasNavbarDarkLabel">
                Menu
              </h5>
              <button
                type="button"
                class="btn-close btn-close-white"
                data-bs-dismiss="offcanvas"
                aria-label="Close"
              ></button>
            </div>
            <div class="offcanvas-body">
              <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                <li class="nav-item">
                  <a
                    class="nav-link"
                    aria-current="page"
                    href="#"
                    v-on:click="loadHome"
                    data-bs-dismiss="offcanvas"
                    >Quienes Somos</a
                  >
                </li>
                <li class="nav-item">
                  <a
                    class="nav-link"
                    aria-current="page"
                    v-if="!isAuth"
                    href="#"
                    v-on:click="loadLogIn"
                    data-bs-dismiss="offcanvas"
                    >Iniciar Sesión</a
                  >
                </li>
                <li class="nav-item">
                  <a
                    class="nav-link"
                    aria-current="page"
                    v-if="!isAuth"
                    href="#"
                    v-on:click="loadSignUp"
                    data-bs-dismiss="offcanvas"
                    >Registrarse</a
                  >
                </li>
                <li class="nav-item">
                  <a
                    class="nav-link"
                    aria-current="page"
                    v-if="isAuth"
                    href="#"
                    v-on:click="loadServices"
                    data-bs-dismiss="offcanvas"
                    >Servicios</a
                  >
                </li>
                <li class="nav-item">
                  <a
                    class="nav-link"
                    aria-current="page"
                    v-if="isAuth"
                    href="#"
                    v-on:click="logOut"
                    data-bs-dismiss="offcanvas"
                    >Salir</a
                  >
                </li>
              </ul>
              <!-- <form class="d-flex mt-3" role="search">
                <input
                  class="form-control me-2"
                  type="search"
                  placeholder="Search"
                  aria-label="Search"
                />
                <button class="btn btn-outline-success" type="submit">
                  Search
                </button>
              </form> -->
            </div>
          </div>
        </div>
      </nav>
    </header>

    <div class="main-component">
      <router-view
        v-on:completedSignUp="completedSignUp"
        v-on:completedLogIn="completedLogIn"
        v-on:logOut="logOut"
        v-on:loadPortatil="loadServices"
        v-on:loadHome="loadHome"
      ></router-view>
    </div>

    <footer class="container border-top border-2 mt-3 pt-4">
      <p class="float-end"><a href="#">Back to top</a></p>
      <p>
        &copy; 2023–2024 Company, Inc. &middot; <a href="#">Privacy</a> &middot;
        <a href="#">Terms</a>
      </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
  data: function () {
    return {
      isAuth: false,
      isSuper: false,
    };
  },

  components: {},

  mounted() {},

  methods: {
    verifyAuth: function () {
      this.$store.commit("setIsAuth", this.isAuth);
      if (this.isAuth) {
        this.$router.push({ name: "user-home" });
      } else {
        this.$router.push({ name: "home" });
      }
    },

    loadLogIn: function () {
      this.$router.push({ name: "login" });
    },

    loadSignUp: function () {
      this.$router.push({ name: "signup" });
    },

    loadHome: function () {
      if (this.isAuth) {
        this.$router.push({ name: "user-home" });
      } else {
        this.$router.push({ name: "home" });
      }
    },

    loadServices: function () {
      this.$router.push({ name: "user-services" });
    },

    completedLogIn: function (data) {
      this.isAuth = true;
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },

    completedSignUp: function (data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },

    logOut: function () {
      this.isAuth = false;
      alert("Sesión Cerrada");
      this.verifyAuth();
    },
  },

  created: function () {
    this.loadHome();
  },
};
</script>

<style>
footer,
header {
  margin: 0;
  padding: 0;
}

html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.navbar-brand img {
  max-width: 150px; /* Ancho máximo de la imagen */
  border-radius: 40%; /* Bordes redondeados */
  overflow: hidden; /* Asegura que la imagen redonda no se extienda más allá del círculo */
}
</style>
