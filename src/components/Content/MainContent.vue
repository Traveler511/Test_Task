<template>
  <div class="content">
    <div v-on:change="CheckFields">
      <div class="form">
        <h1>Заголовок</h1>
        <div class="form__element">
          <p>Ваш филиал</p>

          <select id="selectFilial" required v-model="filial">
            <option v-for="city in cities" :key="city.title">
              {{ city.title }}
            </option>
          </select>
          <p>Онлайн</p>
          <input @click="CheckFilial" v-model="checkFilial" type="checkbox" />
        </div>

        <div class="form__element">
          <p>Тема обращения</p>
          <div class="theme">
            <select
              @change="ChangeTheme('select')"
              required
              v-model="themeSelect"
            >
              <option>Тема №1</option>
              <option>Тема №2</option>
              <option>Тема №3</option>
            </select>
            <div class="form__input-theme">
              <p>Указать самостоятельно</p>
              <input @change="ChangeTheme('input')" v-model="themeInput" />
            </div>
          </div>
        </div>

        <div class="form__element">
          <p>Описание проблемы</p>
          <textarea required v-model="problem"> </textarea>
        </div>

        <div class="form__element">
          <p>Загрузка документов</p>
          <div class="form__input">
            <div class="form__circle"></div>

            <input type="file" />
            <label>
              <p>Нажмите, для загрузки файла</p>
            </label>
          </div>
        </div>

        <div class="form__element">
          <button id="btn1" disabled v-on:click="TaskPost" type="submit">
            Отправить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from "axios";

export default {
  name: "MainContent",

  data() {
    return {
      filial: null,
      themeSelect: null,
      themeInput: "",
      problem: "",
      result: null,
      cities: null,
      checkFilial: null,
      params: null,
    };
  },
  methods: {
    TaskPost() {
      let theme = this.themeSelect;
      if (this.themeSelect == null) theme = this.themeInput;

      this.params = {
        filial: this.filial,
        theme: theme,
        problem: this.problem,
      };
      axios
        .post(
          "https://60254fac36244d001797bfe8.mockapi.io/api/v1/send-form",
          this.params
        )
        .then(function (response) {
          this.answer = response;
        });
      if (this.result == true) {
        this.filial = null;
        this.themeSelect = null;
        this.themeInput = null;
        this.problem = "";
        this.checkFilial = null;
      } else alert("Ошибка отправки заявки");
    },
    CheckFields() {
      if (
        (this.themeSelect != null || this.themeInput != "") &&
        (this.filial != null || this.checkFilial == true) &&
        this.problem != ""
      )
        document.getElementById("btn1").disabled = false;
      else document.getElementById("btn1").disabled = true;
    },
    CheckFilial() {
      if (this.checkFilial == true) {
        document.getElementById("selectFilial").disabled = false;
      } else {
        document.getElementById("selectFilial").disabled = true;
        this.filial = null;
      }
    },
    ChangeTheme(elem) {
      if (elem == "select") this.themeInput = "";
      if (elem == "input") this.themeSelect = null;
    },
  },

  beforeCreate: function () {
    axios
      .get("https://60254fac36244d001797bfe8.mockapi.io/api/v1/city")
      .then((res) => {
        this.cities = res.data;
      });
  },
};
</script>


<style lang="scss" scoped src="./style.scss">
</style>