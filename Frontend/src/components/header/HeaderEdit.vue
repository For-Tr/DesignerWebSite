<template>
  <div>
    <v-app-bar class="header header-flat" height="90" flat>
      <div class="purchase-button" style="padding-right: 6vw;">
        <a target="_blank" @click="handleBack">HOME</a >
      </div>
      <h1 style="padding-right: 6vw;">Enter your Talent</h1>

      <div v-if="loading" class="spinner">
        <div class="ring"></div>
        <span>&nbsp; Generating...</span>
      </div>

      <div v-else class="purchase-button">
        <a target="_blank" @click="handleGenerate" :disabled="loading">generate</a >
      </div>
    

    </v-app-bar>
  </div>
</template>

<script>
import axios from 'axios';
import { useFormStore } from '../../stores/formStore';

export default {
  data() {
    return {
      loading: false
    }
  },
  methods: {
    handleBack() {
      this.$router.push({ name: 'home' });
    },
    async handleGenerate() {
      const formStore = useFormStore();
      const token = localStorage.getItem('access');
      this.loading = true; // Start loading

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
            'Authorization': 'Bearer ' + token,
          },
        });

        console.log('Post successful:', response.data);
        const currentPath = this.$router.currentRoute.path ;
        const newPath = currentPath.slice(0, -4) + 'Show'; 
        this.$router.push({path: newPath, query: {id: response.data.id}}); 
      } catch (error) {
        console.error('Post failed:', error);
      } finally {
        this.loading = false; // End loading
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

    .spinner {
  /* 外部容器，确保其居中 */
  display: flex;
  justify-content: center;
  align-items: center;
  height: 40px; /* 根据需要调整 */
  font-size: larger;
}

.ring {
  /* 内部环的样式 */
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  border-top-color: black;
  width: 40px; /* 根据需要调整 */
  height: 40px; /* 根据需要调整 */
  animation: spin 1s linear infinite; /* 只在环上应用旋转动画 */
}

@keyframes spin {
  to {
    transform: rotate(360deg); /* 旋转动画 */
  }
}


  </style>
  