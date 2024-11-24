<template>
  <div>
      <HeaderThree />
      <div class="banner-content">
          <h1>
              Personal Info Studio: Tune and refine<br />
              your details with creative control. 
          </h1>
           <div class="content-list">
    <div class="list-title">Personal Info</div>
    <RouterLink to="portfolio">
      <a class="forget-pwd" >My Portfolio Web</a>
    </RouterLink>

      <div class="list-content">
        <div class="edit-view">
          <div class="item flex-view">
          <div class="label">Avatar</div>
          <div class="right-box avatar-box flex-view">

            <img v-if="tData.form && tData.form.avatar" :src="tData.form.avatar" class="avatar">
            <img v-else src="../assets/images/avatar.jpg" class="avatar">
            <div class="change-tips flex-view">
              <v-file-input
                  accept="image/png, image/jpeg, image/bmp"
                  label="Avatar"
                  placeholder="Pick an avatar"
                  @change="beforeUpload"
              ></v-file-input>
              <p class="tip">The image format supports GIF, PNG, JPEG, and the size is not less than 200 PX and less than 4 MB</p>
            </div>
          </div>
        </div>
          <div class="item flex-view">
            <div class="label">Name</div>
            <div class="right-box">
              <input type="text" v-model="tData.form.nickname" placeholder="Enter your name" maxlength="20" class="input-dom">

            </div>
          </div>
          <div class="item flex-view">
            <div class="label">Phone number</div>
            <div class="right-box">
              <input type="text" v-model="tData.form.mobile" placeholder="Enter your phone number" maxlength="100"
                class="input-dom web-input">
            </div>
          </div>
          <div class="item flex-view">
          <div class="label">Intro</div>
          <div class="right-box">
            <textarea v-model="tData.form.description" placeholder="Introduce yourself" maxlength="200" class="intro">
            </textarea>
            <p class="tip">Limited to 200 words</p>
          </div>
        </div>
          <div class="item flex-view">

          </div>
          <div class="purchase-button">
              <a
              target="_blank"
              @click="handleEdit"
              >Save</a
              >
          </div>
          <div class="operation">
            <a class="forget-pwd"  @click="handleChangepassword" style="text-align: right;">Change your password?Click here!</a>
          </div>
          
        </div>
        <div class="list-title" style="margin-top: 2vh;">Statics and Analytics</div>
  <div v-for="(note, index) in notes" :key="note.id" class="chart-container">
    <span>{{ note.temp }}</span>
    <div :ref="el => { if(el) chartRefs[index] = el }" 
         style="height: 300px;"
         :id="`chart-${note.id}`">
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
import authorization from "../utils/authorization"
import echarts from "echarts"
import { RouterLink } from "vue-router";

export default {
 components: {
     HeaderThree,
     RouterLink
 },
 data() {
   return {
    notes: [],
      visitCharts: {},  
      chartRefs: [],
      visitDataMap: {}, 
    loading: false,
    tabItems: [
        {
          id: 1,
          name: "All",
        },
        
      ],
    visit_data: [],
    tabContent: [],
    tData: {
      form: { 
        avatar: undefined,
        avatarFile: undefined,
        nickname: undefined,
        email: undefined,
        mobile: undefined,
        description: undefined,
      }
    },
   };
 },                              

 methods: {
  async fetchNotes() {
      try {
        const token = localStorage.getItem('access');
        const response = await axios.get('api/notes', {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer ' + token,
          }
        });
        this.notes = response.data;
        // 为每个 note 获取访问数据
        await Promise.all(this.notes.map(note => this.fetchVisitData(note.id)));
      } catch (error) {
        console.error('failed:', error);
      }
    },

    async fetchVisitData(noteId) {
      try {
        // 修改 API 调用，添加 noteId 参数
        const response = await axios.get(`/api/notes/count`);
        this.visitDataMap[noteId] = response.data.data.visit_data;
        // 获取数据后立即初始化该 note 的图表
        this.$nextTick(() => {
          this.initChart(noteId);
        });
      } catch (error) {
        console.error(`Failed to fetch visit data for note ${noteId}:`, error);
      }
    },
  getUserInfo() {
      this.loading = true
      let email = localStorage.getItem('email')
      axios.get("api/getuser/", {params : { email: email }}).then(res => {
          this.tData.form = res.data
          if (this.tData.form.avatar) {
            this.tData.form.avatar = BASE_URL + this.tData.form.avatar
            console.log(BASE_URL)
          }
          this.loading = false
      }).catch(err => {
          console.log(err)
          this.loading = false
      })
  },

  beforeUpload(file) {
    // 改文件名
    const fileName = new Date().getTime().toString() + '.' + file.type.substring(6)
    const copyFile = new File([file], fileName)
    console.log(copyFile)
    this.tData.form.avatarFile = copyFile
    return false
  },

  handleEdit() {
    const that = this
    authorization().then((response) => {
      if (response[0]) {
        let formData = new FormData()
        if (that.tData.form.avatarFile) {
          formData.append('avatar', that.tData.form.avatarFile)
        }
        if (that.tData.form.nickname) {
          formData.append('nickname', that.tData.form.nickname)
        }
        if (that.tData.form.email) {
          formData.append('email', that.tData.form.email)
        }
        if (that.tData.form.mobile) {
          formData.append('mobile', that.tData.form.mobile)
        }
        if (that.tData.form.description) {
          formData.append('description', that.tData.form.description)
        }
        const token = localStorage.getItem('access')
        let Data = formData

        axios.post('/api/edit_user/',Data, {
          headers:{Authorization: 'Bearer ' + token}
        }).then(function (response) {
          console.log(response)
          location.reload()
        }).catch((error) => {
          console.log(error)
          alert("Failed");
        }) 
      } else {
        alert('Auth information out of date,login again')
      }
    })
  },

  handleChangepassword() {
    this.$router.push({name: 'password'})
  },


 initChart(noteId) {
      // 获取对应的 DOM 元素
      const el = document.getElementById(`chart-${noteId}`);
      if (!el) return;

      // 如果已存在图表实例，先销毁
      if (this.visitCharts[noteId]) {
        this.visitCharts[noteId].dispose();
      }

      // 创建新的图表实例
      const chart = echarts.init(el);
      this.visitCharts[noteId] = chart;

      // 获取该 note 的访问数据
      const visitData = this.visitDataMap[noteId] || [];
      
      let xData = [];
      let uvData = [];
      let pvData = [];
      
      visitData.forEach((item) => {
        xData.push(item.day);
        uvData.push(item.uv);
        pvData.push(item.pv);
      });

      const option = {
        title: {
          text: `Statistics for Note ${noteId}`
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['IP', 'visit'],
          top: '90%',
          left: 'center'
        },
        grid: {
          top: '30px',
          left: '20px',
          right: '20px',
          bottom: '40px',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          axisLabel: {
            textStyle: {
              color: '#2F4F4F'
            }
          },
          axisLine: {
            lineStyle: {
              color: '#2F4F4F'
            }
          },
          data: xData
        },
        yAxis: {
          type: 'value',
          axisLine: { show: false },
          axisTick: { show: false },
          splitLine: {
            show: true,
            lineStyle: {
              color: 'rgba(10, 10, 10, 0.1)',
              width: 1,
              type: 'solid'
            }
          }
        },
        series: [
          {
            name: 'IP',
            type: 'line',
            stack: 'Total',
            data: uvData
          },
          {
            name: 'visit',
            type: 'line',
            stack: 'Total',
            data: pvData
          }
        ]
      };

      chart.setOption(option);
    },

    // 移除原来的 initCharts 方法，因为现在我们是单独初始化每个图表
  },

 mounted() {
    this.getUserInfo();
    this.fetchNotes(); 
 },


  beforeDestroy() {
    this.visitCharts.forEach(chart => {
      chart.dispose();
    });
  }
};
</script>

<style scoped>
input,
textarea {
border-style: none;
outline: none;
margin: 0;
padding: 0;
}
.chart-container {
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #eee;
  border-radius: 4px;
}

.flex-view {
display: -webkit-box;
display: -ms-flexbox;
display: flex;
}

.content-list {
-webkit-box-flex: 1;
-ms-flex: 1;
flex: 1;
margin-left: 5vw;
margin-top: 10vw;
margin-right: 5vw;
height: 100vh;
}

.content-list .list-title {
color: black;
font-weight: 600;
font-size: 18px;
line-height: 48px;
height: 48px;
margin-bottom: 4px;
border-bottom: 1px solid #cedce4;
}

.content-list .edit-view .item {
-webkit-box-align: center;
-ms-flex-align: center;
align-items: center;
margin: 24px 0;
}

.content-list .edit-view .item .label {
width: 100px;
color: black;
font-weight: 600;
font-size: 14px;
}

.content-list .edit-view .item .right-box {
-webkit-box-flex: 1;
-ms-flex: 1;
flex: 1;
}

.content-list .edit-view .item .avatar {
width: 64px;
height: 64px;
border-radius: 50%;
margin-right: 16px;
}

.content-list .edit-view .item .change-tips {
-webkit-box-align: center;
-ms-flex-align: center;
align-items: center;
-ms-flex-wrap: wrap;
flex-wrap: wrap;
}

.content-list .edit-view .item label {
color: #4684e2;
font-size: 14px;
line-height: 22px;
height: 22px;
cursor: pointer;
width: 100px;
display: block;
}

.content-list .edit-view .item .tip {
color: #6f6f6f;
font-size: 14px;
height: 22px;
line-height: 22px;
margin: 0;
width: 100%;
}

.content-list .edit-view .item .input-dom {
width: 400px;
background: #f8fafb;
border-radius: 4px;
height: 40px;
line-height: 40px;
font-size: 14px;
color: #152844;
padding: 0 12px;
}

.content-list .edit-view .item .tip {
font-size: 12px;
line-height: 16px;
color: #6f6f6f;
height: 16px;
margin-top: 4px;
}

.content-list .edit-view .item .intro {
resize: none;
background: #f8fafb;
width: 100%;
padding: 8px 12px;
height: 82px;
line-height: 22px;
font-size: 14px;
color: #152844;
}

.content-list .edit-view .save {
background: #4684e2;
border-radius: 32px;
width: 96px;
height: 32px;
line-height: 32px;
font-size: 14px;
color: #fff;
border: none;
outline: none;
cursor: pointer;
}

.content-list .edit-view .mg {
margin-left: 100px;
}

.operation {
display: flex;
flex-direction: row;
margin: 0 24px;
margin-top: 1vw;
}
</style>