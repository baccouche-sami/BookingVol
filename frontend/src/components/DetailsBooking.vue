<template lang="">
  <div>
    <p>
      <span>Détails de la reservation n° {{ id }}</span> <br />
      <span>Vol: {{ vol.depart }} --> {{ vol.arrive }}</span> <br />
      <span
        >Nom et Prénom: {{ myReservation.nom }} {{ myReservation.prenom }}</span
      >
      <br />
      <span>Nombre de passagers: {{ myReservation.nb_place }}</span> <br />
      <span>Retour inclut: {{ myReservation.retour_inclut }} </span> <br />
      <span>Option Champagne Inclut: {{ myReservation.champagne }} </span>
      <br />
      <span
        >Montant: {{ myReservation.montant }} {{ myReservation.currency }}</span
      >
      <br />
    </p>
  </div>
  <button class="Button">
    <slot>Annuler</slot>
  </button>
  <button class="Button Button2">
    <slot>Modifier</slot>
  </button>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "DetailsBookingComponent",

  data() {
    return {
      id: this.$route.params.id,
      myReservation: {
        nom: "",
        prenom: "",
        nb_place: 0,
        champagne: false,
        currency: "",
        montant: 0,
        retour_inclut: false,
        transport: 0,
        first_class: false,
      },
      vol: {
        depart: "",
        arrive: "",
        places: 0,
      },
    };
  },
  async created() {
    const reservation = await this.$store.dispatch("getOneBooking", this.id);
    this.myReservation = reservation;
    console.log(reservation);
    const vol = await this.$store.dispatch(
      "getOneVol",
      this.myReservation.transport
    );
    this.vol = vol;
    // // console.log(vol);
  },
});
</script>
<style>
.Button {
  background-color: #E49439; /* Green */
  border: none;
  color: white;
  padding: 6px 8px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
.Button2 {
  background-color: #af9e4c; /* Green */
}
</style>