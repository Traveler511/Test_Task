<template>
  <div id="app">
    <div id="nav">
      <div class="menu">
        <router-link class='menu_text' to="/">1 страница</router-link>

        <router-link class='menu_text' to="Math">2 страница</router-link>
      </div>
      <!-- <hr /> -->
    </div>

    <router-view></router-view>
  </div>
</template>

<style lang="scss">

#app {

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: linear-gradient(135deg, rgb(119, 0, 255), rgb(0, 255, 149));
  animation: gradient 5s ease-in-out infinite;
  background-size: 200% 200%;
  height: 100vh;
  width: 100vw;

  hr {
    width: 2px;
    height: 25px;
    transform: rotate(180deg);
    background-color: white;
    border: 0;
    top: 4.6%;
    left: 50%;
    position: absolute;
  }
  .menu {
    display: grid;
    grid-template-columns: 30% 30%;
    text-align: center;
    // grid-column-gap: 10px;
    margin-left: 30%;
    // margin-right: 30%;
    text-decoration: none;
  }
  .menu_text {
    font-size: 20px;
    transition: 0.3s;
     text-decoration: none;
  }
  .menu_text:hover {
    color:#000000;
    transition: 0.3s;
  }

}

@keyframes gradient {
  0% {
    background-position: 0 20%;
  }
  20% {
    background-position: 20% 40%;
  }
  40% {
    background-position: 40% 60%;
  }
  60% {
    background-position: 60% 80%;
  }
  80% {
    background-position: 80% 100%;
  }
  // 100% {
  //   background-position: 100% 80%;
  // }
  // 80% {
  //   background-position: 80% 60%;
  // }
  // 60% {
  //   background-position: 60% 40%;
  // }
  // 40% {
  //   background-position: 40% 20%;
  // }
  // 20% {
  //   background-position: 20% 0%;
  // }
}
.logo {
  width: 120px;

  position: absolute;
   top:0.3%;
    left: 46%;
    position: absolute;
}
#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: white;
   
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
