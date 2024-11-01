<template>
  <div>
    <v-app-bar class="header header-flat" height="90" flat>
      <div class="purchase-button" style="padding-right: 6vw;">
        <a target="_blank" @click="handleBack">HOME</a >
      </div>
      <h1 style="padding-right: 6vw;">Enter your Talent</h1>
      <div class="purchase-button">
        <a target="_blank" @click="handleGenerate">generate</a >
      </div>
    </v-app-bar>
  </div>
</template>

<script>
import axios from 'axios';
import { useFormStore } from '../../stores/formStore';

export default {
  methods: {
    handleBack() {
      this.$router.push({ name: 'home' });
    },
    async handleGenerate() {
      const formStore = useFormStore();
      const token = localStorage.getItem('access')
      try {
        const formData = new FormData();

        Object.keys(formStore.form).forEach(key => {
          if (formStore.form[key] !== undefined) {
            formData.append(key, formStore.form[key]);
          }
        });

        const response = await axios.post('/api/notes/create', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer ' + token
          }
      });
        console.log('Post successful:', response.data);
        this.$router.push({ name: 'results', params: { data: response.data } });
      } catch (error) {
        console.error('Post failed:', error);
      }
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
  .purchase-button { 
    margin: 0 10px; 
    } 
  </style>
  