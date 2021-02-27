<style scoped>
h1 {
  font-size: 40px;
  font-family: "Montserrat", "Trebuchet MS", sans-serif;
  color: rgb(36, 36, 36);
}

h2 {
  font-size: 21px;
  font-family: "Ubuntu", "Verdana", sans-serif;
  color: black;
}

hr {
  border: 1px solid lightgray;
}

table {
  width: 80%;
}

th {
  height: 70px;
  padding: auto;
}

td {
  text-align: center;
  vertical-align: top;
}

.domain {
  font-size: 21px;
  font-weight: bold;
  text-align: center
}

.domainlist {
  font-size: 16px;
  font-weight: bold;
  text-align: center
}

.name {
  text-align: right;
}

.email{
  text-align: left;
}

.list {
  border-radius: 5px;
  list-style-type: none;
  font-family: "Ubuntu", "Verdana", sans-serif;
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

.center {
  margin-left: auto;
  margin-right: auto;
}

.inlist {
  border-radius: 3px;
  padding: 3px;
  margin-bottom: 30px;
  -webkit-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
  background-color: #f2f7fb;
}

.inlist tr:nth-child(odd){
  background-color: #e6f2fc;
}
</style>

<template>
  <section class="login-block">
    <div class="container-fluid">
      <h1 class="text-center">Super OrgContact</h1>
      <div>
          <table class="center list">
            <tr class="domain">
              <th>Domínio</th>
              <th><table>
                <tr><th class="email">Endereço de e-mail</th>
                <th class="name">Nome</th></tr>
                </table>
              </th>
            </tr>
            <tr v-for="(value, key) in msg" :key="value">
              <td class="domainlist">{{ key }}</td>
              <td>
                <table class="inlist">
                  <tr v-for="(item, ) in value" :key="item">
                    <td class="email">{{ item[1] }}</td>
                    <td class="name">{{ item[0] }}</td>
                  </tr>
                </table>
              </td>
            </tr>
          </table> 
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
        withCredentials: true,
      });
      const path = "https://super-org-flask.rj.r.appspot.com/home";
      axiosWithCookies
        .get(path)
        .then(res => {
          console.log(res)
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
