import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    vols: [],
    bookings: [],
    currency: "EURO"
  },
  getters: {
    getVols: (state) => state.vols,
    getBookings: (state) => state.bookings,
    getCurrency: (state) => state.currency,


  },
  actions: {
    async fetchVols({ commit }) {
      try {
        const data = await axios.get("http://127.0.0.1:8000/booking/vols/");
        const dataExt = await axios.get("http://127.0.0.1:8000/booking/external");
        const finalData = dataExt.data ? [...data.data,...dataExt.data] : data.data;
        commit("SET_VOLS", finalData);

        return finalData;
      } catch (error) {
        //alert(error)
        console.log(error);
      }
    },
    async fetchBookings({ commit }) {
        try {
          const data = await axios.get("http://127.0.0.1:8000/booking/reservations/");
          commit("SET_BOOKINGS", data.data);
  
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
          return response.data;
        })
        .catch((error) => {
          return error
        });
    },
    ajoutReservationExternal({ commit }, myReservation) {
      axios
        .post("http://127.0.0.1:8000/booking/external", myReservation)
        .then((response) => {
          return response.data;
        })
        .catch((error) => {
          return error
        });
    },
  },
  mutations: {
    SET_VOLS(state, vols) {
      state.vols = vols;
    },
    SET_BOOKINGS(state, bookings) {
        state.bookings = bookings;
      },
    SET_DEVIS(state, currency) {
        state.currency = currency;
      },
  },
});
