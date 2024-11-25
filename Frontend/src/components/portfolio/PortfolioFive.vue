<template>
  <div class="masonry-wrapper">
    <div class="pt--45 pb--45 masonry-tabs">
      <v-tabs v-model="tab" centered flat hide-slider color="primary">
        <v-tab :ripple="false" v-for="item in tabItems" :key="item.id">{{
          item.name
        }}</v-tab>
      </v-tabs>
    </div>

    <v-tabs-items v-model="tab" no-animation>
      <v-tab-item
        v-for="item in tabContent"
        :key="item.id"
        transition="0"
        reverse-transition="0"
      >
        <vue-masonry-wall :items="item.content" :options="options">
          <template v-slot:default="{ item }">
            <div class="portfolio_style--3 Item">
              <div class="thumb">
                <router-link :to="{ name: 'PortfolioDetails', params: { id: item.noteId, type: item.noteType }}">
                  <img :src="item.src" alt="personal portfolio"
                /></router-link>
                <div class="port-hover-action">
                  <div class="content">
                    <h3>
                      <router-link :to="{ name: 'PortfolioDetails', params: { id: item.noteId, type: item.noteType, status: 'edit' }}">
                        Edit
                      </router-link>
                    </h3>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </vue-masonry-wall>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import VueMasonryWall from "vue-masonry-wall";
import axios from 'axios';
import {BASE_URL} from "../../utils/BASE"
import img from "../../assets/img/project/port-4/portfolio-5.jpg"
export default {
  components: { VueMasonryWall },
  data() {
    return {

      defaultImage: img,
      tab: null,
      index: null,
      options: {
        width: 535,
        padding: {
          default: 7.5,
        },
      },
      tabItems: [
        {
          id: 1,
          name: "All",
        },
        
      ],
      tabContent: []
    };
  },
  created() {
    this.fetchNotes();
  },
  methods: {
    getImageSrc(note) { 
      if (note.pic && note.pic.length > 0 && note.pic[0].pic) { 
        return BASE_URL + note.pic[0].pic; 
      } else {
              return this.defaultImage; 
      }

      },
      getUserName(note) { 
        if (note && note.user && note.user.nickname) { 
          return note.user.nickname; 
        } else if (note && note.user && note.user.username) {
          return note.user.username; 
        }
        return 'Unknown User'; 
      },
    async fetchNotes() {
      try {
        const token = localStorage.getItem('access');
        const response = await axios.get('api/notes',
          {headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer ' + token,
          }},
        );
        const notes = response.data;
        this.tabContent = this.tabItems.map(tab => ({
          id: tab.id,
          content: notes.map(note => ({

            src: this.getImageSrc(note), 
            title: this.getUserName(note),
            noteId: note.id,
            noteType: note.temp,
          }))
        }));
      } catch (error) {
        console.error('failed:', error);
      }
    }
  }
};
</script>

<style scoped lang="scss">
  .Item {
    overflow: hidden;
    width: 100%;
    background: #f5f5f5;
  }

  img {
    object-fit: cover;
    width: 100%;
    height: 100%;
    line-height: 0;
    display: block;
  }
  .portfolio_style--3 {
    margin-bottom: 0;
  }
  .masonry-wall {
    flex-wrap: wrap;
  }
</style>
