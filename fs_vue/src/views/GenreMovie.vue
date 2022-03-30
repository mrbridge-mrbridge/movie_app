<template>
  <div class="home">
    <div class="is-loading-bar has-text-centered" v-bind:class="{ 'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>
    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">{{ genre_name + " Movies"}}</h2>
      </div>

      <div class="column is-3" 
        v-for="movie in genreMov"
        v-bind:key="movie.uuid">
        <div class="box">
          <figure class="mb-4">
            <img :src="movie.get_thumbnail" class="thumbnail">
          </figure>
          <h3 class="is-size-6 thumb-font">{{ movie.title}}</h3>
          <h3 class="is-size-6 thumb-font"> Views: {{ " " + movie.views_count}}</h3>
          <router-link v-bind:to="{ name: 'Movie', params: { movie_id: movie.uuid }}" class="button is-black mt-4">More</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'GenreMovie',
  data() {
    return {
      genreMov: [],
    }
  },
  components: {
  },
  mounted() {
    this.getGenreMovies()
  },
  watch: {
    $route(to, from) {
      if (to.name === 'GenreMovie') {
        this.getGenreMovies()
      }
    }
  },
  methods: {
    async getGenreMovies() {
      const genre_name = this.$route.params.genre_name
      this.$store.commit('setIsLoading', true)
      await axios
        .get(`/api/v1/all-movies/genre/${genre_name}`)
        .then(response => {
          this.genreMov = response.data
        })
        .catch(error => {
          console.log(error)
        })
      document.title = genre_name + ' | FireSide'
      this.genre_name = genre_name
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
 .mb-4 {
   margin-bottom: 0.1rem;
}
 .columns .is-12 {
   display: flex;
   flex-wrap: wrap;
   justify-content: center;
 }
 .box {
   margin-left: 0.9rem;
   display: inline-block;
 }

 .thumb-font {
   font-family: Candara;
 }
</style>
