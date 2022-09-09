import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    vols: [],
  },
  getters: {
    getVols: (state) => state.vols,
  },
  actions: {
    async fetchVols({ commit }) {
      try {
        const data = await axios.get("http://127.0.0.1:8000/booking/vols/");
        commit("SET_VOLS", data.data);

        return data.data;
      } catch (error) {
        //alert(error)
        console.log(error);
      }
    },
    ajoutReservation({ commit }, myReservation) {
      axios
        .post("http://127.0.0.1:8000/booking/reservations/", myReservation)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          console.log("impossible d'enregistrer cette reservation");
        });
    },
  },
  mutations: {
    SET_VOLS(state, vols) {
      state.vols = vols;
    },
  },
});
