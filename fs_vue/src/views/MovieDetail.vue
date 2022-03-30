<template>
  <div class="page-movie">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="mb-6">
          <div class="is-loading-bar has-text-centered" v-bind:class="{ 'is-loading': $store.state.isLoading }">
            <div class="lds-dual-ring"></div>
          </div>
          <img :src="movie.get_image">
        </figure>
        <h1 class="title">{{ movie.title }}</h1>
        <router-link v-bind:to="movie" v-on:click="iView" class="button is-black mt-4">Watch Movie</router-link>
      </div>
      <div class="column is-3">
        <h2 class="subtitle"><strong>About This Movie</strong></h2>
        <p><strong>Status: </strong>{{ movie.status }}</p>
        <p><strong>Views: </strong>{{ movie.views_count }}</p>
        <p><strong>Year: </strong>{{ movie.year_of_production }}</p>
        <p> <strong>Genre: </strong>{{ movie.genre }} </p>
        <p v-if="watched"><strong>I've Opened Before? </strong>Yes</p>
        <p v-else><strong>I've Opened Before? </strong>No</p>
        <p> <strong>Description: </strong>{{ movie.description }} </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Movie',
  data() {
    return {
      movie: {},
      watched: false,
    }
  },
  mounted() {
    this.getMovie()
  },
  methods: {
    async getMovie() {
      this.$store.commit('setIsLoading', true)

      const movie_id = this.$route.params.movie_id

      await axios
        .get(`/api/v1/detail/${movie_id}`)
        .then(response => {
          this.movie = response.data

          document.title = this.movie.title + ' | FireSide'

        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    },
    iView() {
      this.watched = true
      this.movie.views_count += 1
    }
  }
}
</script>

<style lang="scss">


.lds-dual-ring {
  display: inline-block;
  width: 50px;
  height: 50px;
}

.lds-dual-ring:after {
  content: "";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid yellowgreen;
  border-color: yellowgreen transparent yellowgreen transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>