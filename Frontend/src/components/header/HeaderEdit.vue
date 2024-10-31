<template>
    <div>
      <v-app-bar class="header header-flat" height="90" flat>
  
          <div class="purchase-button" style="padding-right: 6vw;">
          <a
            target="_blank"
            @click="handleBack"
            >HOME</a
          >
        </div>
        <h1 style="padding-right: 6vw;">Enter your Talent</h1>
        <div class="purchase-button">
          <a
            target="_blank"
            @click="goNext"
            >generate</a
          >
        </div>
  
        
        </v-app-bar>
    </div>
    
  </template>
  
  <script>
  
  
    export default {
  
      methods: {
        handleBack() {
          this.$router.push({name: 'home'})
        },
        goNext() {
          this.$router.push({path: `${this.$route.path}Edit`})
        }
      },
    };
  </script>
  
  
  <style scoped> 
  .header { 
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
  } 
  .purchase-button { 
    margin: 0 10px; 
    } 
  </style>
  