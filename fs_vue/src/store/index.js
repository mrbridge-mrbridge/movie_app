import { createStore } from 'vuex'

export default createStore({
  state: {
    viewed: {
      watched: false,
      count: 1,
    },
    isAuthenticated: false,
    token: '',
    isLoading: false
  },
  getters: {
  },
  mutations: {
    setIsLoading(state, status) {
      state.isLoading = status
    }
  },
  actions: {
  },
  modules: {
  }
})
