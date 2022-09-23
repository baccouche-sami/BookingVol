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
      let data = null;
      let dataExt =  null;
      let finalData = null;
      try {
        data = await axios.get("http://127.0.0.1:8000/booking/vols/");
      } catch (error) {
        console.log(error);
      }
      try {
        dataExt = await axios.get("http://127.0.0.1:8000/booking/external",{timeout: 1000});

      } catch (error) {
        console.log(error);
      }
      
      if (data && dataExt) {
        finalData = [...data.data,...dataExt.data] 
      }
      else if (data){
        finalData= data.data
      }
      else if (dataExt)
      {
        finalData = dataExt.data
      }
      commit("SET_VOLS", finalData);

      return finalData;
      
      
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
