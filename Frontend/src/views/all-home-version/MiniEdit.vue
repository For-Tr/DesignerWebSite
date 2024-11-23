<template>
  <div class="form-container">
    <div class="preview-section">
      <div class="preview-header">
        <h2>Live Preview</h2>
        <div class="device-buttons">
          <button 
            class="device-btn"
            :class="{ active: currentDevice === 'mobile' }"
            @click="changeDevice('mobile')"
          >
            <i class="fas fa-mobile-alt"></i>
          </button>
          <button 
            class="device-btn"
            :class="{ active: currentDevice === 'tablet' }"
            @click="changeDevice('tablet')"
          >
            <i class="fas fa-tablet-alt"></i>
          </button>
          <button 
            class="device-btn"
            :class="{ active: currentDevice === 'desktop' }"
            @click="changeDevice('desktop')"
          >
            <i class="fas fa-desktop"></i>
          </button>
        </div>
      </div>
      <div 
        class="iframe-container"
        :class="currentDevice"
      >
        <iframe 
          ref="previewIframe"
          src="http://localhost:8080/minimal-agencyPre" 
          frameborder="0"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          @load="iframeLoaded"
          :style="iframeStyle"
        ></iframe>
      </div>
    </div>
  
  
      <form @submit.prevent="submitForm">
        <!-- Section 1 -->
        <div class="form-section">
          <h2>Section 1</h2>
          <div class="upload-section">
            <v-file-input
              accept="image/*, video/*, application/pdf"
              label="Upload Files (Images/Videos/PDF)"
              placeholder="Pick files for section 1"
              @change="(file) => {beforeUpload(file, 'pic1')}"
              :show-size="true"
        
            ></v-file-input>
            
          </div>
          <div class="text-inputs">
            <div class="input-group">
              <label>Text 1</label>
              <input type="text" v-model="form.text1" @input="handleTextInput('text1', $event.target.value)" placeholder="Enter text 1" maxlength="500">
            </div>
            <div class="input-group">
              <label>Text 2</label>
              <input type="text" v-model="form.text2" @input="handleTextInput('text2', $event.target.value)" placeholder="Enter text 2" maxlength="500">
            </div>
            <div class="input-group">
              <label>Text 3</label>
              <input type="text" v-model="form.text3" @input="handleTextInput('text3', $event.target.value)" placeholder="Enter text 3" maxlength="500">
            </div>
          </div>
        </div>
  
        <!-- Section 2 -->
        <div class="form-section">
          <h2>Section 2</h2>
          <div class="upload-section">
            <v-file-input
              accept="image/*, video/*, application/pdf"
              label="Upload Files (Images/Videos/PDF)"
              placeholder="Pick files for section 2"
              @change="(file) => {beforeUpload(file, 'pic2')}"
              :show-size="true"
        
            ></v-file-input>
          </div>
          <div class="text-inputs">
            <div class="input-group">
              <label>Text 4</label>
              <input type="text" v-model="form.text4" @input="handleTextInput('text4', $event.target.value)" placeholder="Enter text 4" maxlength="500">
            </div>
            <div class="input-group">
              <label>Text 5</label>
              <input type="text" v-model="form.text5" @input="handleTextInput('text5', $event.target.value)" placeholder="Enter text 5" maxlength="500">
            </div>
            <div class="input-group">
              <label>Text 6</label>
              <input type="text" v-model="form.text6" @input="handleTextInput('text6', $event.target.value)" placeholder="Enter text 6" maxlength="500">
            </div>
          </div>
        </div>
  
        <!-- Section 3 -->
        <div class="form-section">
          <h2>Section 3</h2>
          <div class="upload-section">
            <v-file-input
              accept="image/*, video/*, application/pdf"
              label="Upload Files (Images/Videos/PDF)"
              placeholder="Pick files for section 3"
               @change="(file) => {beforeUpload(file, 'pic3')}"
              :show-size="true"
        
            ></v-file-input>
          </div>
          <div class="text-inputs">
            
            <div class="input-group">
              <label>Skill 1</label>
              <input type="text" v-model="form.text7" @input="handleTextInput('text7', $event.target.value)" placeholder="Enter text 7" maxlength="500">
            </div>
            <div class="input-group">
              <label>Skill 2</label>
              <input type="text" v-model="form.text8" @input="handleTextInput('text8', $event.target.value)" placeholder="Enter text 8" maxlength="500">
            </div>
            <div class="input-group">
              <label>Skill 3</label>
              <input type="text" v-model="form.text9" @input="handleTextInput('text9', $event.target.value)" placeholder="Enter text 9" maxlength="500">
            </div>
            
        
          </div>
          <div class="text-inputs">
          <div class="input-group">
              <label>Persentage 1</label>
              <input type="text" v-model="form.text10" @input="handleTextInput('text10', $event.target.value)" placeholder="Enter text 10" maxlength="500">
            </div>
            <div class="input-group">
              <label>Persentage 2</label>
              <input type="text" v-model="form.text11" @input="handleTextInput('text11', $event.target.value)" placeholder="Enter text 11" maxlength="500">
            </div>
            <div class="input-group">
              <label>Persentage 3</label>
              <input type="text" v-model="form.text12" @input="handleTextInput('text11', $event.target.value)" placeholder="Enter text 11" maxlength="500">
            </div>
            </div>
        </div>
  
  
        <div v-if="loading" class="spinner">
          <div class="ring"></div>
          <span>&nbsp; Generating...</span>
        </div>
  
        <div v-else class="purchase-button" style="display: flex; justify-content: center;">
          <a target="_blank" @click="handleGenerate" :disabled="loading">generate</a >
        </div>
      
      </form>
    </div>
  </template>
  
  <script>
  import { useFormStore } from '../../stores/formStore.js';
  import axios from 'axios';
  
  export default {
    data() {
      const formStore = useFormStore();
      return {
        formStore,
        form: formStore.form,
        loading: false,
        currentDevice: 'desktop',
        deviceSettings: {
          mobile: {
            width: '375px',
            height: '667px',
            scale: 1
          },
          tablet: {
            width: '768px',
            height: '1024px',
            scale: 1
          },
          desktop: {
            width: '100%',
            height: '100%',
            scale: 1
          }
        }
  
      };
    },
    computed: {
      containerStyle() {
        const settings = this.deviceSettings[this.currentDevice]
        return {
          width: settings.width,
          paddingBottom: this.currentDevice === 'desktop' ? '56.25%' : 'auto',
          height: this.currentDevice === 'desktop' ? '0' : settings.height
        }
      },
      iframeStyle() {
        const settings = this.deviceSettings[this.currentDevice]
        return {
          width: settings.width,
          height: this.currentDevice === 'desktop' ? '100%' : settings.height,
          transform: `scale(${settings.scale})`,
          transformOrigin: 'top left'
        }
      }
    },
    mounted() {
    this.form.temp = 'Mini'
    this.messageHandler = (event) => {
      if (event.origin !== 'http://localhost:8080') return;
      if (event.data.type === 'iframeReady') {
        this.iframeReady = true;
        this.sendDataToIframe(this.form);
      }
      console.log(1111)
    };
    window.addEventListener('message', this.messageHandler);
  },
  
  beforeUnmount() {
    window.removeEventListener('message', this.messageHandler);
  },
    methods: {
      messageHandler(){
        console.log(2222)
      },
      iframeLoaded() {
        this.iframeReady = true;
        // 初始化时发送完整的表单数据
        this.sendDataToIframe(this.form);
      },
      changeDevice(device) {
        this.currentDevice = device;
        // 触发iframe内容重新计算大小
        if (this.$refs.previewIframe) {
          this.$refs.previewIframe.contentWindow.postMessage('resize', '*');
        }
      },
  
      handleTextInput(field, value) {
        // 更新本地表单数据
        this.form[field] = value;
        
        // 更新 store
        this.formStore.updateTextField(field, value);
        
        // 发送数据到 iframe
        this.sendDataToIframe(this.form);
      },
  
      beforeUpload(file, picname) {
        const fileName = new Date().getTime().toString() + '.' + file.type.substring(6);
        const copyFile = new File([file], fileName);
        this.$pinia.use(() => ({
          formStore: useFormStore(),
        }));
        this.formStore.updatePicField(picname, copyFile);
        console.log(this.formStore)
      
        
        // 发送数据到 iframe
        this.sendDataToIframe(this.form);
      },
  
      sendDataToIframe(data) {
    if (!this.iframeReady) {
      console.warn('Iframe not ready yet');
      return;
    }
    
    const iframe = this.$refs.previewIframe;
    if (!iframe) {
      console.error('Iframe reference not found');
      return;
    }
    
    if (!iframe.contentWindow) {
      console.error('Iframe contentWindow not available');
      return;
    }
  
    try {
      iframe.contentWindow.postMessage({
        type: 'formUpdate',
        data: data
      }, 'http://localhost:8080');
      console.log('Message sent to iframe:', data);
    } catch (error) {
      console.error('Error sending message to iframe:', error);
    }
  },
  
      submitForm() {
        try {
          // Validate form data
          
          // Update store
          this.formStore.$patch({
            form: { ...this.form }
          });
          
  
          
        } catch (error) {
          console.error('Form submission error:', error);
          alert('Form submission error:', error)
        }
      },
  
      validateForm() {
        // Add your validation logic here
        const requiredFields = ['text1', 'text2', 'text3'];
        for (const field of requiredFields) {
          if (!this.form[field]) {
            throw new Error(`${field} is required`);
          }
        }
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
          const url = newPath + '?id=' + response.data.id
          const fullUrl = 'http://localhost:8080' + url;
  const result = confirm('🎉Your website is live!\nClick OK to view: \n' + fullUrl);
  if (result) {
      window.location.href = fullUrl;
  }
         
        } catch (error) {
          console.error(error)
          alert('Generate failed, please try again:', error.message);
        } finally {
          this.loading = false; // End loading
        }
  
      },
  
      async uploadFile(fileData, section) {
        // Add your file upload logic here
        console.log(`Uploading file for section ${section}:`, fileData);
      }
    },
    watch: {
      form: {
        deep: true,
        handler(newValue) {
          // Automatically update preview when form changes
          console.log('Form updated:', newValue);
        }
      }
    }
  };
  </script>
  
  <style lang="scss">
  .form-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    align-items: center;
  
  }
  .preview-section {
    margin-bottom: 2rem;
  }
  
  .preview-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  
    h2 {
      margin: 0;
    }
  }
  
  .device-buttons {
    display: flex;
    gap: 1rem;
  }
  
  .device-btn {
    background: none;
    border: none;
    padding: 0.5rem;
    cursor: pointer;
    font-size: 1.2rem;
    color: #666;
    transition: all 0.3s ease;
  
    &:hover {
      color: #333;
    }
  
    &.active {
      color: #1e90ff;
    }
  }
  
  .iframe-container {
    position: relative;
    overflow: hidden;
    background: #f5f5f5;
    border-radius: 8px;
    transition: all 0.3s ease;
    margin: 0 auto;
  
    &.mobile {
      width: 375px;
      height: 667px;
    }
  
    &.tablet {
      width: 768px;
      height: 1024px;
    }
  
    &.desktop {
      width: 100%;
      padding-bottom: 56.25%;
      height: 0;
    }
  
    iframe {
      position: absolute;
      top: 0;
      left: 0;
      border: none;
      transition: all 0.3s ease;
    }
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
  
  // 添加响应式布局
  @media screen and (max-width: 1200px) {
    .iframe-container {
      &.tablet {
        transform: scale(0.8);
        transform-origin: top center;
      }
    }
  }
  
  @media screen and (max-width: 800px) {
    .iframe-container {
      &.tablet {
        transform: scale(0.6);
      }
      &.mobile {
        transform: scale(0.8);
        transform-origin: top center;
      }
    }
  }
  .form-section {
    margin-bottom: 2rem;
    padding: 2rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    background: #fff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    
    h2 {
      margin-bottom: 1.5rem;
      color: #333;
      font-size: 1.5rem;
    }
  }
  
  .upload-section {
    margin-bottom: 1.5rem;
    
    .v-file-input {
      border-radius: 4px;
      
      &:hover {
        border-color: #666;
      }
    }
  }
  
  .text-inputs {
    display: grid;
    gap: 1rem;
    
    .input-group {
      label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 500;
        color: #444;
      }
      
      input {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 1rem;
        transition: border-color 0.3s ease;
        
        &:focus {
          outline: none;
          border-color: #666;
          box-shadow: 0 0 0 2px rgba(102,102,102,0.1);
        }
        
        &::placeholder {
          color: #999;
        }
      }
    }
  }
  
  .submit-btn {
    width: 100%;
    padding: 1rem;
    background: black;
    color: white;
    border: 1px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1.1rem;
    transition: background-color 0.3s ease;
    
    &:hover {
      background: white;
      color: black;
      border-color: black;
    }
    
    &:active {
      transform: translateY(1px);
    }
  }
  
  @media (max-width: 768px) {
    .form-container {
      padding: 1rem;
    }
    
    .form-section {
      padding: 1rem;
    }
    
    .text-inputs {
      grid-template-columns: 1fr;
    }
  }
  
  @media (min-width: 769px) {
    .text-inputs {
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    }
  }
  
  // Animation for form sections
  .form-section {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    
    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
  }
  
  // Custom styling for file input preview
  .v-file-input {
    .v-file-input__text {
      font-size: 0.9rem;
    }
    
    .v-file-input__counter {
      color: #666;
    }
  }
  </style>