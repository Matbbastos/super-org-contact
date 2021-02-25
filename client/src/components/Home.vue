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

li {
  marker: none;
  background: white;
}

li:nth-child(odd) {
  background: lightgray;
}

.list {
  border-radius: 5px;
  list-style-type: none;
  padding: 5px;
  -webkit-box-shadow: 0 0 5px 0 rgba(43, 43, 43, 0.1),
    0 11px 6px -7px rgba(43, 43, 43, 0.1);
  box-shadow: 0 0 5px 0 rgba(43, 43, 43, 0.1),
    0 11px 6px -7px rgba(43, 43, 43, 0.1);
  margin-bottom: 30px;
  -webkit-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
  background-color: white;
}
</style>

<template>
  <section class="login-block">
    <div class="container-fluid">
      <h1 class="text-center">Super OrgContact</h1>
      <div class="text-center">
        <ul class="list">
          <h2>Nome | Endereço de e-mail</h2>
          <li v-for="item in msg" :key="item.message">
            {{ item[0] }} | {{ item[1] }}
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      msg: ""
    };
  },
  methods: {
    getMessage() {
      const axiosWithCookies = axios.create({
        withCredentials: true
      });
      const path = "http://localhost:5000/home";
      axiosWithCookies
        .get(path)
        .then(res => {
          this.msg = res.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  created() {
    this.getMessage();
  }
};
</script>
