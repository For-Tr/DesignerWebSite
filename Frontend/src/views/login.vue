<template>
  <div>
    <HeaderThree />
    <div class="container">
      <div class="login-page pc-style">
        <img src="../assets/img/logo/logo.jpg" alt="logo" class="logo-icon">
        <div class="login-tab">
          <div class="tab-selected">
            <span class="title">LOGIN</span>
            <span class="tabline tabline-width"></span>
          </div>
        </div>
        
        <!-- LinkedIn Login Button -->
        <div class="social-login">
          <button class="linkedin-btn" @click="handleLinkedInLogin">
            <i class="fab fa-linkedin"></i>
            Sign in with LinkedIn
          </button>
        </div>
        
        <div class="divider">
          <span>or</span>
        </div>

        <!-- Original login form -->
        <div class="mail-login" type="login">
 <div class="container">

    <div class="login-page pc-style">
      

      <div class="mail-login" type="login">
        <div class="common-input">
          <img src='../assets/images/mail-icon.svg' class="left-icon">
          <div class="input-view">
            <input placeholder="Enter your E-mail" v-model="pageData.loginForm.email" type="text" class="input">
            <p class="err-view">
            </p>
          </div>
          <!---->
        </div>
        <div class="common-input">
          <img src="../assets/images/pwd-icon.svg" class="left-icon">
          <div class="input-view">
            <input placeholder="Enter your password" v-model="pageData.loginForm.password" type="password" class="input">
            <p class="err-view">
            </p>
          </div>
        </div>
        <div class="next-btn-view">
          <button class="next-btn btn-active" style="margin: 16px 0px;" @click="handleLogin">Login</button>
        </div>
      </div>
      <div class="operation">
        <a @click="handleCreateUser" class="forget-pwd" style="text-align: right;">No account?Register now!</a>
      </div>
    </div>
  </div>

    </div>
  </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import HeaderThree from "../components/header/HeaderThree";
import {BASE_URL} from "../utils/BASE"
export default {
  components: {
    HeaderThree,
  },
  data() {
    return {
      pageData: {
        loginForm: {
          email: '',
          password: ''
        }
      }
    };
  },
  methods: {
    handleLinkedInLogin() {
      window.location.href = BASE_URL + '/social-auth/login/linkedin-oauth2/';
    },
    handleLogin() {
      // Validate form fields
      if (!this.pageData.loginForm.email || !this.pageData.loginForm.password) {
        alert('Please enter both email and password');
        return;
      }

      // Email format validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(this.pageData.loginForm.email)) {
        alert('Please enter a valid email address');
        return;
      }

      const that = this;
      axios.post('/api/token/', {
        email: this.pageData.loginForm.email,
        password: this.pageData.loginForm.password,
      }).then(function (response) {
        const storage = localStorage;
        const expiredTime = Date.parse(response.headers.date) + 60000;
        storage.setItem('access', response.data.access);
        storage.setItem('refresh', response.data.refresh);
        storage.setItem('expiredTime', expiredTime);
        storage.setItem('email', that.pageData.loginForm.email);
        storage.setItem('username', response.data.username)
        alert('Login successful! Welcome back.');
        that.$router.push({name: 'home'})
      }).catch((error) => {
        if (error.response) {
          // Server responded with error
          switch (error.response.status) {
            case 400:
              alert('Invalid credentials. Please check your email and password.');
              break;
            case 401:
              alert('Unauthorized access. Please check your credentials.');
              break;
            case 404:
              alert('Account not found. Please check your email or register.');
              break;
            case 429:
              alert('Too many login attempts. Please try again later.');
              break;
            case 500:
              alert('Server error. Please try again later.');
              break;
            default:
              alert('Login failed. Please try again.');
          }
        } else if (error.request) {
          // Request made but no response
          alert('Network error. Please check your internet connection.');
        } else {
          // Error in request configuration
          alert('An error occurred. Please try again.');
        }
        console.log(error);
      });
    },
    handleCreateUser() {
      this.$router.push({name: 'register'})
    }
  }
};
</script>
<style scoped>
.social-login {
  padding: 0 28px;
  margin-bottom: 20px;
}

.linkedin-btn {
  width: 100%;
  padding: 10px;
  background-color: #0077b5;
  color: white;
  border: none;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: background-color 0.3s;
}

.linkedin-btn:hover {
  background-color: #006097;
}

.linkedin-btn i {
  margin-right: 10px;
  font-size: 18px;
}

.divider {
  text-align: center;
  margin: 20px 28px;
  position: relative;
}

.divider::before,
.divider::after {
  content: "";
  position: absolute;
  top: 50%;
  width: 45%;
  height: 1px;
  background-color: #c3c9d5;
}

.divider::before {
  left: 0;
}

.divider::after {
  right: 0;
}

.divider span {
  background-color: white;
  padding: 0 10px;
  color: #666;
  font-size: 12px;
}
div {
  display: block;
}

.title{
  font-size: x-large;
  font-weight: bold;
  color: black;
}

.container {

  background-size: cover;
  object-fit: cover;
  height: 100%;
  max-width: 100%;
  display:flex;
  justify-content: center;
  align-items:center;
}

.new-content {
  position: absolute;
  left: 0;
  right: 0;
  margin: 80px auto 0;
  width: 980px;
}

.logo-img {
  width: 125px;
  display: block;
  margin-left: 137.5px;
}

.login-page {
  overflow: hidden;
  background: #fff;

  .logo-icon {
    margin-top: 20px;
    margin-left: 175px;
    width: 48px;
    height: 48px;
  }
}

.pc-style {
  position: relative;
  width: 400px;
  height: 464px;
  background: #fff;
  border-radius: 4px;
  -webkit-box-shadow: 2px 2px 6px #aaa;
  box-shadow: 2px 2px 6px #aaa;
}

.login-tab {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  color: #1e1e1e;
  font-size: 14px;
  color: #1e1e1e;
  font-weight: 500;
  height: 46px;
  line-height: 44px;
  margin-bottom: 40px;
  border-bottom: 1px solid #c3c9d5;

  div {
    position: relative;
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    text-align: center;
    cursor: pointer;
  }

  .tabline {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    margin: 0 auto;
    display: inline-block;
    width: 0;
    height: 2px;
    background: #3d5b96;
    -webkit-transition: width .5s cubic-bezier(.46, 1, .23, 1.52);
    transition: width .5s cubic-bezier(.46, 1, .23, 1.52);
  }

  tab-selected {
    color: #1e1e1e;
    font-weight: 500;
  }

  .mail-login, .tel-login {
    padding: 0 28px;
  }

}

.mail-login {
  margin: 0px 24px;
}

.common-input {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;

  .left-icon {
    margin-right: 12px;
    width: 24px;
  }

  .input-view {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;

    .input {
      font-weight: 500;
      font-size: 14px;
      color: #1e1e1e;
      height: 26px;
      line-height: 26px;
      border: none;
      padding: 0;
      display: block;
      width: 100%;
      letter-spacing: 1.5px;
    }

    err-view {
      margin-top: 4px;
      height: 16px;
      line-height: 16px;
      font-size: 12px;
      color: #f62a2a;
    }
  }
}

.next-btn {
  background: #3d5b96;
  border-radius: 4px;
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  height: 40px;
  line-height: 40px;
  text-align: center;
  width: 100%;
  outline: none;
  cursor: pointer;
}

button {
  background: transparent;
  padding: 0;
  border-width: 0px;
}

button, input, select, textarea {
  margin: 0;
  padding: 0;
  outline: none;
}

.operation {
  display: flex;
  flex-direction: row;
  margin: 0 24px;
}

.forget-pwd {

  display: block;
  overflow: hidden;
  flex:1;
  margin: 0 auto;
  color: #3d5b96;
  font-size: 14px;
  cursor: pointer;
}

</style>
