import { createStore } from 'vuex'
import axios from "axios"
export default createStore({
    state: {
        vols: []
    },
    getters: {
        getVols: (state) => state.vols

    },
    actions: {
        async fetchVols({ commit }) {
            try {
              const data = await axios.get('https://localhost:8000/booking/vols')
                commit('SET_VOLS', data.data)
              }
              catch (error) {
                  //alert(error)
                  console.log(error)
              }
          }
    },
    mutations: {
        SET_VOLS(state, vols) {
            state.vols = vols
        }
    }
})