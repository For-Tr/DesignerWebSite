<template>
    <div>
      <v-app-bar class="header header-flat" height="90" flat>
        <div class="header-buttons">

          <div class="purchase-button">
            <a target="_blank" @click="goNext">Contact Author</a >
          </div>
        </div>
      </v-app-bar>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      Email: String
    },
    methods: {
      handleBack() {

        this.$router.push({ name: 'portfolio' });
      },
      goNext() {
        this.$router.push({ name: 'Contact', params:{Email: this.Email} });
      }
    }
  };
  </script>
  
  <style scoped>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .header-buttons {
    display: flex;
    align-items: center;
  }
  
  .purchase-button {
    margin: 0 10px;
  }
  </style>