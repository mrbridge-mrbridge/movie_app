<template>
  <div class="page-sign-up">
    <div class="columns">
      <div class="box column is-4 is-offset-4">
        <div class="txt-center">
          <h1 class="title">Sign Up</h1>
          <i class="small-font">Fields marked <h class="red-text">*</h> are required</i>
          <hr>
        </div>
        <div class="notification" v-if="errors.length">
          <p class="med-font red-text" v-for="error in errors" v-bind:key="error">{{ error }} &#128532</p>
        </div>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label class="focus">Username<h class="red-text">*</h></label>
            <div class="control">
              <input type="text" class="input" v-model="username">
            </div>
          </div>

          <div class="field">
            <label>Valid Email Address<h class="red-text">*</h></label>
            <div class="control">
              <input type="email" class="input" v-model="email">
            </div>
          </div>

          <div class="field">
            <label>Password<h class="red-text">*</h></label>
            <div class="control">
              <input type="password" class="input" v-model="password">
            </div>
          </div>

          <div class="field">
            <label>Confirm Password<h class="red-text">*</h></label>
            <div class="control">
              <input type="password" class="input" v-model="password2">
            </div>
          </div>
          
          <div class="field">
            <div class="control">
              <button class="button btn-is-wide">Sign Me Up</button>
            </div>
          </div>
          <hr>
          Already have an account? Then <router-link to="/log-in" class="bold-green">Log In</router-link>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      password2: '',
      errors: [],
    }
  },
  methods: {
    submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('Username is missing')
      }
      if (this.email === '') {
        this.errors.push('Email Address is missing')
      }
      if (this.password === '') {
        this.errors.push('Password is missing')
      }
      if ((this.username) && (this.username.length < 5)){
        this.errors.push('Username must have at least 5 characters')
      }
      if ((this.password) && (this.password.length < 5)){
        this.errors.push('Password is too short')
      }
      if (this.password !== this.password2) {
        this.errors.push('Passwords do not match')
      }

      if (!this.errors.length) {
        const userData = {
          username: this.username,
          email: this.email,
          password: this.password
        }
      }
      axios
        .post("/api/v1/users/create/", userData)
        .then(response => {
          toast({
            message: 'Account created successfully! You can LOG IN now',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right'
          })
          this.$router.push('/log-in')
        })
        .catch(error => {
          if (error.response) {
            for (const item in error.response.data) {
              this.errors.push(`${item}: ${error.response.data[item]}`)
            }
            console.log(JSON.stringify(error.response.data))
          } else if (error.message) {
              this.errors.push('Oops!! Something went wrong. Please try again')
              console.log(JSON.stringify(error))
          }
        })
    }
  }
}

</script>

<style scoped>
.red-text {
  color: red;
}
.small-font {
  font-size: 11px;
}
.med-font {
  font-size: 12px;
}
.bold-green {
  color: #48c78e;
  font-weight: bold;
}

.btn-is-wide {
  width: 100%;
  color: white;
  background: #48c78e;
  font-weight: bold;
}

.btn-is-wide:focus, .bold-green:focus {
  text-transform: uppercase;
  background: #99e5c3;
}
.txt-center {
  text-align: center;
  position: relative;
}
</style>
