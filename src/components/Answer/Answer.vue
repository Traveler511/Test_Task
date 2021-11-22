<template>
  <div class="content">
     {{$route.params.id}}
  </div>
</template>


<style lang="scss" scoped src="./style.scss">
</style>
<script>
import axios from "axios";

export default {
  name: "Answer",

  data() {
    return {};
  },
  methods: {
    getDat() {
      axios.get("http://127.0.0.1:5000/resultmain").then((res) => {
        this.result = res.data;
        // this.price_trade = this.portfolio[0].price_buy;
        // for (let i = 0; i < this.portfolio.length; i++) {
        //   this.portfolio[i].price_buy += " " + this.portfolio[i].currency;
        //   this.portfolio[i].result += " " + this.portfolio[i].currency;
        //   this.portfolio[i].actually_price += " " + this.portfolio[i].currency;
        //   this.portfolio[i].main_result += " " + this.portfolio[i].currency;
        // }
      });
    },
  },
};
</script>
