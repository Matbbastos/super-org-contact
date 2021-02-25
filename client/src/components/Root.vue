<style scoped>
h1 {
  font-size: 40px;
  font-family: "Montserrat", "Trebuchet MS", sans-serif;
  color: rgb(66, 66, 66);
}

h2 {
  font-size: 21px;
  font-family: "Ubuntu", "Verdana", sans-serif;
  color: black;
}

.login-block {
  min-height: 93.6vh;
}

.login-block .auth-box {
  margin: 20px auto 0;
  max-width: 450px !important;
}

.card {
  border-radius: 10px;
  -webkit-box-shadow: 0 0 5px 0 rgba(43, 43, 43, 0.1),
    0 11px 6px -7px rgba(43, 43, 43, 0.1);
  box-shadow: 0 0 5px 0 rgba(43, 43, 43, 0.1),
    0 11px 6px -7px rgba(43, 43, 43, 0.1);
  border: none;
  margin-bottom: 30px;
  -webkit-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
  background-color: white;
}

.card .card-block {
  padding: 1.25rem;
}

.btn {
  border-radius: 4px;
  position: relative;
  top: 15px;
  text-transform: capitalize;
  font-size: 15px;
  padding: 12px 19px;
  cursor: pointer;
}

#infoMessage p {
  color: red !important;
}

.btn-google {
  color: #545454;
  background-color: #ffffff;
  box-shadow: 0 1px 2px 1px #ddd;
}
</style>

<template>
  <section class="login-block">
    <div class="container-fluid">
      <h1 class="text-center">Super OrgContact</h1>
      <div class="text-center">
        <div class="auth-box card">
          <div class="card-block">
            <h2>
              Seja bem-vindo, para acessar o aplicativo, por favor, conecte-se:
            </h2>
            <a
              class="btn btn-lg btn-google btn-block text-uppercase btn-outline"
              href="http://localhost:5000/login"
              ><img
                src="https://img.icons8.com/color/16/000000/google-logo.png"
              />
              Entrar com o Google</a
            ><br />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
