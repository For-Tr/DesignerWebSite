<template>

    <div>
    <HeaderThree />
 <div class="container">

    <div class="login-page pc-style">
      <img src="../assets/img/logo/logo.jpg" alt="logo" class="logo-icon">
      <div class="login-tab">
        <div class="tab-selected">
          <span class="title">REGISTER</span>
          <span class="tabline tabline-width"></span>
        </div>
      </div>
      <div class="mail-login" type="login">
        <div class="common-input">
          <img src='../assets/images/register-name.svg' class="left-icon">
          <div class="input-view">
            <input placeholder="Enter your username" v-model="pageData.loginForm.username" type="text" class="input">
            <p class="err-view">
            </p>
          </div>
          <!---->
        </div>
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
        <div class="common-input">
          <img src="../assets/images/pwd-icon.svg" class="left-icon">
          <div class="input-view">
            <input placeholder="Enter your password again" v-model="pageData.loginForm.repassword" type="password" class="input">
            <p class="err-view">
            </p>
          </div>
        </div>
        <div class="next-btn-view">
          <button class="next-btn btn-active" style="margin: 16px 0px;" @click="handleRegister" :disabled="registing">Register</button>
        </div>
      </div>
      <div class="operation">
        <a @click="handleLogin" class="forget-pwd" style="text-align: right;">Already have an account?Login now!</a>
      </div>
    </div>
  </div>

    </div>
 
</template>
<script>
import axios from "axios";
import HeaderThree from "../components/header/HeaderThree";

export default {
    components: {
        HeaderThree,
    },
    data() {
        return {
            registing: false,
            pageData: {
                loginForm: {
                    username: '',
                    email: '',
                    password: '',
                    repassword: '',
                }
            }
        };
    },
    methods: {
        validateForm() {
            if (!this.pageData.loginForm.username.trim()) {
                alert("Please enter username");
                return false;
            }
            if (!this.pageData.loginForm.email.trim()) {
                alert("Please enter email");
                return false;
            }
            if (!this.validateEmail(this.pageData.loginForm.email)) {
                alert("Invalid email format");
                return false;
            }
            if (!this.pageData.loginForm.password) {
                alert("Please enter password");
                return false;
            }
            if (this.pageData.loginForm.password !== this.pageData.loginForm.repassword) {
                alert("Passwords do not match");
                return false;
            }
            return true;
        },

        validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        },

        handleRegister() {
            if (this.registing) {
                return;
            }
            
            if (!this.validateForm()) {
                return;
            }

            this.registing = true;
            
            axios.post('/api/user/', {
                username: this.pageData.loginForm.username,
                email: this.pageData.loginForm.email,
                password: this.pageData.loginForm.password,
                repassword: this.pageData.loginForm.repassword
            }).then(response => {
              console.log(response)
                alert('Verification email has been sent! Please login after verify');
                this.$router.push({name: 'login'});
            }).catch(error => {
                let errorMessage = 'Registration failed.';
                
                if (error.response && error.response.data) {
                    if (typeof error.response.data === 'string') {
                        errorMessage = error.response.data;
                    } else if (typeof error.response.data === 'object') {
                        const firstError = Object.values(error.response.data)[0];
                        errorMessage = Array.isArray(firstError) ? firstError[0] : firstError;
                    }
                }
                
                alert(errorMessage);
            }).finally(() => {
                this.registing = false;
            });
        },

        handleLogin() {
            this.$router.push({name: 'login'});
        }
    }
};
</script>
<style scoped>
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
