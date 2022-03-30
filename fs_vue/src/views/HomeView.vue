<template>
  <div class="home">
    <section class="hero is-medium is-black mb-12">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          FireSide
        </p>
        <p class="subtitle">
          Your World of Entertainment
        </p>
      </div>
    </section>

    <div class="columns is-multiline is-black">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Current Movies</h2>
      </div>

      <div class="column is-3" 
        v-for="movie in AllMovies"
        v-bind:key="movie.uuid">
        <div class="box">
          <figure class="mb-4">
            <img :src="movie.get_thumbnail" class="thumbnail">
          </figure>
          <h3 class="is-size-6">{{ movie.title}}</h3>
          <h3 class="is-size-6"> Views: {{ " " + movie.views_count}}</h3>
          <router-link v-bind:to="{ name: 'Movie', params: { movie_id: movie.uuid }}" class="button is-black mt-4">More</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      AllMovies: []
    }
  },
  components: {
  },
  mounted() {
    this.getAllMovies()
  },
  methods: {
    getAllMovies() {
      axios
        .get('/api/v1/all-movies/')
        .then(response => {
          this.AllMovies = response.data

          document.title = 'Home | FireSide'
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
.mb-4 {
   margin-bottom: 0.1rem !important;
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
</style>
