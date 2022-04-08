<template>
  <div id="wrapper">
  <nav class="navbar is-black">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><strong>FireSide</strong></router-link>
      <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
      <div class="navbar-start">
        <div class="navbar-item">
          <form method="get" action="/search">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" placeholder="Search Movies..." name="query">
              </div>
              <div class="control">
                <button class="button is-success">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="navbar-end">
        <router-link to="/" class="navbar-item">Home</router-link>
        <router-link to="/movies" class="navbar-item">Movies</router-link>
        <router-link to="/tv-shows" class="navbar-item">TV Shows</router-link>
        <div>
          <div class="gen-re">
            <div class="navbar-item genre-style">Genre</div>
            <ul class="nav-popover box">
              <li class="nav-list-down"
               v-for="genre in genres"
               v-bind:key="genre"
              >
                <router-link v-bind:to="{ name:'GenreMovie', params: {genre_name: genre}}" class="nav-down" >{{ genre }}</router-link>
              </li>
            </ul>
          </div>
        </div>

        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/log-in" class="button is-light">Log In</router-link>
            <router-link to="/sign-up" class="button is-light">Sign Up</router-link>

            <router-link to="/profile" class="button is-success">
              <span class="icon"><i class="fas fa-tv"></i></span>
              <span>User</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <section class="section">
    <router-view/>
  </section>

  <footer class="footer">
    <p class="has-text-centered"><b>FireSide  Copyright (C) 2022</b></p>
  </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
      genres : [
        'Action',
        'Drama',
        'Horror',
        'Comedy',
        'Fiction',
        'Romance',
        'Documentary',
        'Animation',
        'Fantasy',
        'Sports',
        'Spirituality',
      ]
    }
  },
}
</script>


<style lang="scss">
@import '../node_modules/bulma';

.nav-down {
  font-family: Candara;
  color: black;
}
.nav-down:hover{
  color: rgb(53, 175, 100)
}

.thumb-font {
   font-family: Candara;
 }

.columns .is-12 {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .box {
    margin-left: 0.9rem;
  }

.gen-re {
	height: auto;
}

.nav-popover {
	visibility: hidden;
	transition-delay: 500ms;
  position: absolute;
  top: 60px;
  --stripe: #cfd8dc;
  --bg: #d4eef7;
}

li {
  color: black;
}
.gen-re:hover .nav-popover{
	visibility: visible;
	transition: transform 500ms;
	transform: translateY(-5px);
	transition-delay: 0ms;
}

.navbar, .navbar-menu, .navbar-start, .navbar-end {
  align-items: center;
}

.genre-style {
  color: white;
  background-color: black;
}

html, body {
  --stripe: #cfd8dc;
  --bg: #d4eef7;

  background: linear-gradient(135deg, var(--bg) 25%, transparent 25%) -50px 0,
    linear-gradient(225deg, var(--bg) 25%, transparent 25%) -50px 0,
    linear-gradient(315deg, var(--bg) 25%, transparent 25%),
    linear-gradient(45deg, var(--bg) 25%, transparent 25%);
  background-size: 100px 100px;
  background-color: var(--stripe);
}

  .thumbnail {
    border-radius: 8px;
    width: 150px;
    height: 200px;
    object-fit: cover;
  }

  .thumbnail:hover {
    box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
  }
</style>